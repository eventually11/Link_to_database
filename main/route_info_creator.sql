CREATE TABLE route_info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitude DECIMAL(10, 7) NOT NULL,
    longitude DECIMAL(10, 7) NOT NULL,
    distance_km DECIMAL(10, 2),
    duration_min DECIMAL(10, 2),
    type VARCHAR(255),
    address TEXT
);