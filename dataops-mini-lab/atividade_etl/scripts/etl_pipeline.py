import pandas as pd
import duckdb
import os

def run_pipeline():
    os.makedirs('data/gold', exist_ok=True)
    
    df_cust = pd.read_csv('data/raw/customers.csv')
    df_prod = pd.read_csv('data/raw/products.csv')
    df_ord = pd.read_csv('data/raw/orders.csv')
    df_items = pd.read_csv('data/raw/order_items.csv')

    df_ord['order_date'] = pd.to_datetime(df_ord['order_date'])
    df_items['total_item_price'] = df_items['quantity'] * df_items['unit_price']
    
    df_merged = df_items.merge(df_ord, on='order_id') \
                        .merge(df_cust, on='customer_id') \
                        .merge(df_prod, on='product_id')
    
    con = duckdb.connect('data/gold/analytics.db')
    
    con.execute("CREATE OR REPLACE TABLE raw_orders AS SELECT * FROM df_ord")
    con.execute("CREATE OR REPLACE TABLE raw_items AS SELECT * FROM df_items")
    con.execute("CREATE OR REPLACE TABLE treated_customers AS SELECT * FROM df_cust")
    con.execute("CREATE OR REPLACE TABLE fct_sales AS SELECT * FROM df_merged")
    
    print("Pipeline finalizado.")
    return con

if __name__ == "__main__":
    run_pipeline()

# Adicione isso ao final do etl_pipeline.py
con = duckdb.connect('data/gold/analytics.db')

print("\n--- FATURAMENTO POR CATEGORIA ---")
print(con.execute("""
    SELECT category, SUM(total_item_price) as total 
    FROM fct_sales 
    GROUP BY category 
    ORDER BY total DESC
""").df())