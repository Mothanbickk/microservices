import psycopg2

from repairing import Repairing

conn = psycopg2.connect(
    host="test.dsacademy.kz",
    database="fortesting",
    user="testing",
    password="testing123"
)


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS repairings_askar (
        id SERIAL PRIMARY KEY,
        description VARCHAR(255) NOT NULL,
        city VARCHAR(255) NOT NULL,
        price INTEGER NOT NULL,
        loss_estimate INTEGER NOT NULL,
        amount INTEGER,
        created DATE DEFAULT NOW(),
        status VARCHAR(255) DEFAULT 'new'
        )
    """

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def insert_repairing(repairing: Repairing):
    query = """
    INSERT INTO repairings_askar (description, city, price, loss_estimate, amount)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor = conn.cursor()
    cursor.execute(query, (repairing.description, repairing.city, repairing.price, repairing.loss_estimate, repairing.amount))
    conn.commit()


def update_repairing():
    query = "UPDATE repairings_askar SET amount=price*loss_estimate, status='paid' WHERE status='new';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def complete_repairing():
    query = "UPDATE repairings_askar SET status='done' WHERE status='paid';"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


