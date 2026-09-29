import sqlite3

DATABASE = "products.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def create_product(name, category, price):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO products (name, category, price)
        VALUES (?, ?, ?)
        """,
        (name, category, price)
    )

    connection.commit()
    product_id = cursor.lastrowid
    connection.close()

    return product_id


def get_products():
    connection = get_connection()

    rows = connection.execute(
        "SELECT id, name, category, price FROM products"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]

def get_product(product_id):
    connection = get_connection()

    row = connection.execute(
        "SELECT id, name, category, price FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    connection.close()

    if row is None:
        return None

    return dict(row)