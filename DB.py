import psycopg2

conn = psycopg2.connect(database="ClientsDB", user="postgres", password="19102016")


def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE clients(
        clients_id SERIAL PRIMARY KEY,
        first_name VARCHAR(60) NOT NULL,
        last_name VARCHAR(60) NOT NULL,
        e-mail VARCHAR(60) NOT NULL UNIQUE,
        phone VARCHAR(60)
        );
        """)

        cur.execute("""
        CREATE TABLE phone_clients(
        phone_clients_id SERIAL PRIMARY KEY,
        phone INTEGER NOT NULL UNIQUE,
        client_id INTEGER REFERENCES clients(clients_id)
        );
        """)

def add_client(conn, first_name, last_name, email, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO clients(first_name, last_name,email, phone=None) VALUES()
        );
        """)

def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO clients(client_id, phone) VALUES()
        );
        """)

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE clients SET first_name = %s, last_name = %s, email = %s, phone = %s WHERE client_id = %s
        ); 
        """)

def delete_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM clients WHERE client_id=%s, phone=%s
        ); 
        """)
def delete_client(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM clients WHERE client_id=%s
        );
        """)
        pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT first_name, last_name, email, phone
        FROM clients
        );
        """)
conn.close()
