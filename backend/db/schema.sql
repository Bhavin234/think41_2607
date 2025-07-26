-- products.csv
CREATE TABLE products(
    id VARCHAR(50) PRIMARY KEY,
    cost DECIMAL(10, 2),
    category VARCHAR(100),
    name VARCHAR(255),
    brand VARCHAR(100),
    retail_price DECIMAL(10, 2),
    department VARCHAR(100),
    sku VARCHAR(100),
    distribution_centre_id VARCHAR(50)
);

-- distribution_centres.csv
CREATE TABLE distribution_centres(
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
);

-- inventory_items.csv
CREATE TABLE inventory_items(
    id VARCHAR(50) PRIMARY KEY,
    product_id VARCHAR(50),
    created_at DATETIME,
    sold_at DATETIME,
    cost DECIMAL(10, 2),
    product_category VARCHAR(100),
    product_name VARCHAR(255),
    product_brand VARCHAR(100),
    product_retail_price DECIMAL(10, 2),
    product_department VARCHAR(100),
    product_sku VARCHAR(100),
    distribution_centre_id VARCHAR(50),
);

-- orders.csv
CREATE TABLE orders(
    order_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    status VARCHAR(50),
    gender VARCHAR(10),
    created_at DATETIME,
    returned_at DATETIME,
    shipped_at DATETIME,
    delivered_at DATETIME,
    number_of_items INT,
);

-- order_items.csv
CREATE TABLE order_items(
    id VARCHAR(50) PRIMARY KEY,
    order_id VARCHAR(50),
    uder_id VARCHAR(50),
    product_id VARCHAR(50),
    inventory_item_id VARCHAR(50),
    status VARCHAR(50),
    created_at DATETIME,
    shipped_at DATETIME,
    delivered_at DATETIME,
    returned_at DATETIME,
);

-- users.csv
CREATE TABLE users(
    id VARCHAR(50) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(150),
    age INT,
    gender VARCHAR(10),
    state VARCHAR(100),
    street_address VARCHAR(255),
    postal_code VARCHAR(20),
    city VARCHAR(100),
    country VARCHAR(100),
    latitude DECIMAL(10, 6),
    longitude DECIMAL(10, 6),
    traffic_source VARCHAR(100),
    created_at DATETIME,
);

-- Conversation Schema
CREATE TABLE conversations(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
);

CREATE TABLE messages(
    id INT AUTO_INCREMENT PRIMARY KEY,
    conversation_id INT,
    sender ENUM('user', 'ai'),
    messages TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
        ON DELETE CASCADE
);