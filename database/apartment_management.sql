CREATE DATABASE IF NOT EXISTS apartment_management CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE apartment_management;

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    full_name VARCHAR(100),
    role_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (role_id) REFERENCES roles(id)
);

CREATE TABLE rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(20) NOT NULL UNIQUE,
    floor INT,
    area FLOAT,
    rent_price DECIMAL(10, 2),
    status ENUM('Available', 'Rented', 'Maintenance') DEFAULT 'Available'
);

CREATE TABLE residents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    identity_card VARCHAR(20) NOT NULL UNIQUE,
    date_of_birth DATE,
    phone_number VARCHAR(20),
    email VARCHAR(100),
    move_in_date DATE,
    room_id INT,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE contracts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contract_code VARCHAR(50) NOT NULL UNIQUE,
    resident_id INT NOT NULL,
    room_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    deposit DECIMAL(10, 2),
    status ENUM('Active', 'Expired', 'Terminated') DEFAULT 'Active',
    FOREIGN KEY (resident_id) REFERENCES residents(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE electricity_water (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    old_electricity INT,
    new_electricity INT,
    electricity_price DECIMAL(10, 2),
    old_water INT,
    new_water INT,
    water_price DECIMAL(10, 2),
    recorded_date DATE,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE invoices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    rent_amount DECIMAL(10, 2),
    electricity_amount DECIMAL(10, 2),
    water_amount DECIMAL(10, 2),
    service_fee DECIMAL(10, 2),
    total_amount DECIMAL(10, 2),
    status ENUM('Unpaid', 'Paid') DEFAULT 'Unpaid',
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE payments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    invoice_id INT NOT NULL,
    amount_paid DECIMAL(10, 2),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method VARCHAR(50),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10, 2),
    expense_date DATE,
    category VARCHAR(50)
);
