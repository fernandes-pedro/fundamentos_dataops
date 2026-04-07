from __future__ import annotations

import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from app.activities import (
    aggregate_orders_activity,
    generate_csv_activity,
    load_csv_to_mongodb_activity,
)
from app.workflows import OrdersPipelineWorkflow


async def main() -> None:
    print("🔌 Conectando ao Temporal...", flush=True)

    client = await Client.connect("localhost:7233")

    print("✅ Conectado ao Temporal!", flush=True)

    worker = Worker(
        client,
        task_queue="orders-task-queue",
        workflows=[OrdersPipelineWorkflow],
        activities=[
            generate_csv_activity,
            load_csv_to_mongodb_activity,
            aggregate_orders_activity,
        ],
    )

    print("🚀 Worker started. Waiting for workflows...", flush=True)

    await worker.run()


if __name__ == "__main__":
    print("⚙️ Iniciando worker...", flush=True)
    asyncio.run(main())