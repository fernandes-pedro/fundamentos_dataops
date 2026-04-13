import pandas as pd
from faker import Faker
import random
import os

fake = Faker('pt_BR')

def generate_ecommerce_data():
    os.makedirs('data/raw', exist_ok=True)
    
    customers = [{
        "customer_id": i,
        "customer_name": fake.name(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "signup_date": fake.date_between(start_date='-2y', end_date='today')
    } for i in range(1, 3001)]
    pd.DataFrame(customers).to_csv('data/raw/customers.csv', index=False)

    categories = ['Eletrônicos', 'Vestuário', 'Cozinha', 'Livros', 'Esportes']
    products = [{
        "product_id": i,
        "product_name": fake.catch_phrase(),
        "category": random.choice(categories),
        "price": round(random.uniform(10.0, 500.0), 2)
    } for i in range(1, 301)]
    df_products = pd.DataFrame(products)
    df_products.to_csv('data/raw/products.csv', index=False)

    orders = [{
        "order_id": i,
        "customer_id": random.randint(1, 3000),
        "order_date": fake.date_time_between(start_date='-1y', end_date='now'),
        "status": random.choice(['delivered', 'shipped', 'cancelled', 'processing'])
    } for i in range(1, 10001)]
    pd.DataFrame(orders).to_csv('data/raw/orders.csv', index=False)

    order_items = []
    for i in range(1, 20001):
        p_id = random.randint(1, 300)
        u_price = df_products.loc[df_products['product_id'] == p_id, 'price'].values[0]
        order_items.append({
            "order_item_id": i,
            "order_id": random.randint(1, 10000),
            "product_id": p_id,
            "quantity": random.randint(1, 5),
            "unit_price": u_price
        })
    pd.DataFrame(order_items).to_csv('data/raw/order_items.csv', index=False)
    
    print("Sucesso: data/raw/")

if __name__ == "__main__":
    generate_ecommerce_data()