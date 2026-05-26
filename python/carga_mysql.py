import pandas as pd
import mysql.connector
import os

# conexão com MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Ana240512",
    database="comercial"
)

cursor = conn.cursor()

# caminho da pasta dos CSV
pasta = "./dados"

# =====================================================
# PEDIDOS
# =====================================================

arquivo = os.path.join(pasta, "olist_orders_dataset.csv")
df = pd.read_csv(arquivo)

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    order_id VARCHAR(50),
    customer_id VARCHAR(50),
    order_status VARCHAR(20),
    order_purchase_timestamp DATETIME
)
""")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO pedidos (
            order_id,
            customer_id,
            order_status,
            order_purchase_timestamp
        )
        VALUES (%s, %s, %s, %s)
    """, (
        row['order_id'],
        row['customer_id'],
        row['order_status'],
        row['order_purchase_timestamp']
    ))

conn.commit()

print("Pedidos inseridos!")

# =====================================================
# PAGAMENTOS
# =====================================================

arquivo_pag = os.path.join(pasta, "olist_order_payments_dataset.csv")
df_pag = pd.read_csv(arquivo_pag)

cursor.execute("""
CREATE TABLE IF NOT EXISTS pagamentos (
    order_id VARCHAR(50),
    payment_type VARCHAR(20),
    payment_value FLOAT
)
""")

for _, row in df_pag.iterrows():
    cursor.execute("""
        INSERT INTO pagamentos (
            order_id,
            payment_type,
            payment_value
        )
        VALUES (%s, %s, %s)
    """, (
        row['order_id'],
        row['payment_type'],
        row['payment_value']
    ))

conn.commit()

print("Pagamentos inseridos!")

# =====================================================
# CLIENTES
# =====================================================

arquivo_cli = os.path.join(pasta, "olist_customers_dataset.csv")
df_cli = pd.read_csv(arquivo_cli)

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    customer_id VARCHAR(50),
    customer_city VARCHAR(100),
    customer_state VARCHAR(10)
)
""")

for _, row in df_cli.iterrows():
    cursor.execute("""
        INSERT INTO clientes (
            customer_id,
            customer_city,
            customer_state
        )
        VALUES (%s, %s, %s)
    """, (
        row['customer_id'],
        row['customer_city'],
        row['customer_state']
    ))

conn.commit()

print("Clientes inseridos!")

# =====================================================
# ITENS
# =====================================================

arquivo_itens = os.path.join(pasta, "olist_order_items_dataset.csv")
df_itens = pd.read_csv(arquivo_itens)

cursor.execute("""
CREATE TABLE IF NOT EXISTS itens (
    order_id VARCHAR(50),
    product_id VARCHAR(50),
    price FLOAT
)
""")

for _, row in df_itens.iterrows():
    cursor.execute("""
        INSERT INTO itens (
            order_id,
            product_id,
            price
        )
        VALUES (%s, %s, %s)
    """, (
        row['order_id'],
        row['product_id'],
        row['price']
    ))

conn.commit()

print("Itens inseridos!")

# =====================================================
# PRODUTOS
# =====================================================

arquivo_prod = os.path.join(pasta, "olist_products_dataset.csv")
df_prod = pd.read_csv(arquivo_prod)

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    product_id VARCHAR(50),
    product_category_name VARCHAR(100)
)
""")

for _, row in df_prod.iterrows():

    categoria = row['product_category_name']

    # tratar valores vazios
    if pd.isna(categoria):
        categoria = None

    cursor.execute("""
        INSERT INTO produtos (
            product_id,
            product_category_name
        )
        VALUES (%s, %s)
    """, (
        row['product_id'],
        categoria
    ))

conn.commit()

print("Produtos inseridos!")

# =====================================================
# CATEGORIAS
# =====================================================

arquivo_cat = os.path.join(
    pasta,
    "product_category_name_translation.csv"
)

df_cat = pd.read_csv(arquivo_cat)

cursor.execute("""
CREATE TABLE IF NOT EXISTS categorias (
    product_category_name VARCHAR(100),
    product_category_name_english VARCHAR(100)
)
""")

for _, row in df_cat.iterrows():

    categoria = row['product_category_name']
    categoria_en = row['product_category_name_english']

    if pd.isna(categoria):
        categoria = None

    if pd.isna(categoria_en):
        categoria_en = None

    cursor.execute("""
        INSERT INTO categorias (
            product_category_name,
            product_category_name_english
        )
        VALUES (%s, %s)
    """, (
        categoria,
        categoria_en
    ))

conn.commit()

print("Categorias inseridas!")

# =====================================================

cursor.close()
conn.close()

print("Carga finalizada com sucesso!")