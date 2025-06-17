-- users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ
);

-- events
CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    location VARCHAR(255),
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ NOT NULL,
    created_by INTEGER REFERENCES users(user_id)
);

-- tickets
CREATE TABLE tickets (
    ticket_id SERIAL PRIMARY KEY,
    event_id INTEGER REFERENCES events(event_id),
    type VARCHAR(50),
    price NUMERIC(10, 2) NOT NULL,
    quantity_total INTEGER NOT NULL,
    quantity_available INTEGER NOT NULL
);

-- reservations
CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    ticket_id INTEGER REFERENCES tickets(ticket_id),
    quantity INTEGER NOT NULL,
    reserved_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMPTZ,
    is_confirmed BOOLEAN DEFAULT FALSE
);

-- orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    total NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- order_items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    ticket_id INTEGER REFERENCES tickets(ticket_id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);

-- products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price NUMERIC(10, 2) NOT NULL,
    stock INTEGER NOT NULL
);

-- order_products
CREATE TABLE order_products (
    order_product_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(order_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER NOT NULL,
    unit_price NUMERIC(10, 2) NOT NULL
);


-- Inserir usuário
INSERT INTO users (name, email, hashed_password, created_at)
VALUES ('Gabriela Mota', 'gabriela@gmail.com', 'senha123', NOW());

-- Inserir evento
INSERT INTO events (name, location, date, created_at)
VALUES ('Rock in Rio', 'Rio de Janeiro', '2025-09-15 20:00:00', NOW());

-- Inserir produtos
INSERT INTO products (name, price, created_at)
VALUES 
  ('Pipoca', 10.00, NOW()),
  ('Refrigerante', 8.00, NOW());

-- Inserir ingresso
-- Substitua 1 pelo ID real do evento, se necessário
INSERT INTO tickets (event_id, type, price, quantity, created_at)
VALUES (1, 'Inteira', 150.00, 100, NOW());

