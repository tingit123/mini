USE apartment_management;

INSERT INTO roles (name) VALUES ('Admin'), ('Manager'), ('Resident');

INSERT INTO users (username, password, full_name, role_id) VALUES 
('admin', 'scrypt:32768:8:1$K1$b', 'System Admin', 1); -- You should generate proper hash

INSERT INTO rooms (room_number, floor, area, rent_price, status) VALUES 
('101', 1, 25.5, 3000000, 'Available'),
('102', 1, 30.0, 3500000, 'Available'),
('201', 2, 25.5, 3000000, 'Available');
