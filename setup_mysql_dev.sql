-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;

-- Crear una tabla de ejemplo (puedes personalizar según tus modelos)
CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
);

-- Insertar datos de ejemplo
INSERT INTO states (id, name, created_at, updated_at)
VALUES
    ('421a55f4-7d82-47d9-b54c-a76916479545', 'Alabama', NOW(), NOW()),
    ('421a55f4-7d82-47d9-b54c-a76916479546', 'Arizona', NOW(), NOW());
