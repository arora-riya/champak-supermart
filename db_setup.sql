-- Create the database
CREATE DATABASE project_champak;

-- Use the created database
USE project_champak;

-- Create the 'staff' table
CREATE TABLE staff (
    staff_id INT(3) PRIMARY KEY,
    staff_name VARCHAR(25)
);

-- Describe the 'staff' table
DESCRIBE staff;

-- Insert data into the 'staff' table
INSERT INTO staff VALUES 
    (101, 'Georgina'),
    (102, 'Manan'),
    (103, 'Florence'),
    (104, 'Prabhu Dasgupta'),
    (105, 'Mridula Sharma'),
    (106, 'Shubhansh Garg'),
    (107, 'Padma Patil'),
    (108, 'Parvati Patil'),
    (109, 'Abdullah Khan'),
    (110, 'Sukhpreet Kaur');

-- Select all records from the 'staff' table
SELECT * FROM staff;

-- Create the 'stock' table
CREATE TABLE stock (
    item_code CHAR(3) PRIMARY KEY,
    item_name VARCHAR(30),
    company VARCHAR(30),
    availability BOOLEAN,
    price DECIMAL(10, 2)
);

-- Describe the 'stock' table
DESCRIBE stock;

-- Insert data into the 'stock' table
INSERT INTO stock VALUES 
    ('a11', 'Shampoo', 'Moha', TRUE, 500);

INSERT INTO stock VALUES 
    ('a12', 'Soap', 'Pears', TRUE, 50),
    ('b12', 'Noodles', 'Yippee', FALSE, 45),
    ('c13', 'Crockery Set', 'Prestige', TRUE, 670.50),
    ('d01', 'Choco Powder', 'Nestle', TRUE, 150);

INSERT INTO stock VALUES 
    ('d13', 'Ball Pen', 'NATARAJ', TRUE, 10),
    ('c22', 'Chips', 'Lays-PepsiCo', FALSE, 30);

-- Select all records from the 'stock' table
SELECT * FROM stock;

-- Create the 'members' table
CREATE TABLE members (
    First_Name VARCHAR(40),
    Last_Name VARCHAR(40),
    DOB DATE,
    Address VARCHAR(100),
    Phone CHAR(10)
);

-- Describe the 'members' table
DESCRIBE members;
