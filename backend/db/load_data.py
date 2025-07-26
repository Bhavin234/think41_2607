import csv
import os
from config import get_connection

DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')

def load_csv_to_table(filename, table, columns):
    conn = get_connection()
    cursor = conn.cursor()
    path = os.path.join(DATA_DIR, filename)

    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values = [row.get(col, None) or None for col in columns]
            placeholders = ', '.join(['%s'] * len(columns))
            sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
            cursor.execute(sql, values)

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Loaded {filename} into {table}")

def main():
    load_csv_to_table('products.csv', 'products', [
        'id', 'cost', 'category', 'name', 'brand', 'retail_price', 'department', 'sku', 'distribution_center_id'
    ])

    load_csv_to_table('distribution_centers.csv', 'distribution_centers', [
        'id', 'name', 'latitude', 'longitude'
    ])

    load_csv_to_table('inventory_items.csv', 'inventory_items', [
        'id', 'product_id', 'created_at', 'sold_at', 'cost', 'product_category', 'product_name',
        'product_brand', 'product_retail_price', 'product_department', 'product_sku', 'product_distribution_center_id'
    ])

    load_csv_to_table('orders.csv', 'orders', [
        'order_id', 'user_id', 'status', 'gender', 'created_at', 'returned_at',
        'shipped_at', 'delivered_at', 'num_of_item'
    ])

    load_csv_to_table('order_items.csv', 'order_items', [
        'id', 'order_id', 'user_id', 'product_id', 'inventory_item_id',
        'status', 'created_at', 'shipped_at', 'delivered_at', 'returned_at'
    ])

    load_csv_to_table('users.csv', 'users', [
        'id', 'first_name', 'last_name', 'email', 'age', 'gender', 'state',
        'street_address', 'postal_code', 'city', 'country',
        'latitude', 'longitude', 'traffic_source', 'created_at'
    ])

if __name__ == '__main__':
    main()
