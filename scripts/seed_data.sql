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
