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
    name VARCHAR(255),
    merchant_id INT NOT NULL REFERENCES tags(id),
    tag_id INT INT NOT NULL REFERENCES merchants(id)
)

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
)


