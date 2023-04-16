DROP TABLE IF EXISTS tags
DROP TABLE IF EXISTS merchants
DROP TABLE IF EXISTS transactions
DROP TABLE IF EXISTS users

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    cost INT,
    merchant_id INT NOT NULL REFERENCES merchants(id),
    tag_id INT NOT NULL REFERENCES tags(id)
    user_id INT NOT NULL REFERENCES users(id)
)

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    transaction_id INT INT NOT NULL REFERENCES tags(id)
)

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    transaction_id INT INT NOT NULL REFERENCES merchants(id)
)


