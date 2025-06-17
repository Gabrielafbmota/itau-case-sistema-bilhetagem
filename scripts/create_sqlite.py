import sqlite3
from datetime import datetime
import bcrypt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../event_ticketing.db")

# Conectar ao banco
conn = sqlite3.connect("../event_ticketing.db")
cursor = conn.cursor()

# Criar tabelas com created_at e updated_at
cursor.executescript(
    """
-- users
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME
);

-- events
CREATE TABLE IF NOT EXISTS events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    location TEXT,
    capacity TEXT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    created_by INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(created_by) REFERENCES users(user_id)
);

-- tickets
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    type TEXT,
    price REAL NOT NULL,
    quantity_total INTEGER NOT NULL,
    quantity_available INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(event_id) REFERENCES events(event_id)
);

-- reservations
CREATE TABLE IF NOT EXISTS reservations (
    reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    ticket_id INTEGER,
    quantity INTEGER NOT NULL,
    reserved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    is_confirmed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(ticket_id) REFERENCES tickets(ticket_id)
);

-- orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    total REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

-- order_items
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    ticket_id INTEGER,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(ticket_id) REFERENCES tickets(ticket_id)
);

-- products
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME
);

-- order_products
CREATE TABLE IF NOT EXISTS order_products (
    order_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
"""
)

# Inserir usuária com senha hash
senha_plana = "senha123"
hashed = bcrypt.hashpw(senha_plana.encode(), bcrypt.gensalt()).decode()

cursor.execute(
    """
INSERT INTO users (name, email, hashed_password)
VALUES (?, ?, ?)
""",
    ("Gabriela Mota", "gabriela@gmail.com", hashed),
)

# Inserir evento
user_id = cursor.lastrowid
cursor.execute(
    """
INSERT INTO events (title, location, start_time, end_time, created_by)
VALUES (?, ?, ?, ?, ?)
""",
    (
        "Rock in Rio",
        "Rio de Janeiro",
        "2025-09-15 20:00:00",
        "2025-09-15 23:00:00",
        user_id,
    ),
)

event_id = cursor.lastrowid

# Inserir produtos
cursor.executemany(
    """
INSERT INTO products (name, price, stock)
VALUES (?, ?, ?)
""",
    [("Pipoca", 10.00, 100), ("Refrigerante", 8.00, 100)],
)

# Inserir ingresso
cursor.execute(
    """
INSERT INTO tickets (event_id, type, price, quantity_total, quantity_available)
VALUES (?, ?, ?, ?, ?)
""",
    (event_id, "Inteira", 150.00, 100, 100),
)

# Finaliza
conn.commit()
conn.close()

print("Banco criado e populado com created_at e updated_at em todas as tabelas ✅")
