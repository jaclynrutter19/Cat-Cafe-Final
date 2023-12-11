-- Cat Cafe by Olivia Russell and Jaclyn Rutter
-- CS 340
-- Project Step 2 Draft


-- Creating entities

-- CREATE Customers table 
CREATE OR REPLACE TABLE Customers (
  customer_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  first_name VARCHAR(45),
  last_name VARCHAR(45),
  email VARCHAR(45),
  phone VARCHAR(12),
  PRIMARY KEY (customer_id)
);

-- CREATE Employees table 
CREATE OR REPLACE TABLE Employees (
  employee_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  email VARCHAR(70) NOT NULL,
  phone VARCHAR(12),
  hourly_salary DECIMAL(10, 2),
  PRIMARY KEY (employee_id)
);

-- CREATE Foster_Parents Table 
CREATE OR REPLACE TABLE Foster_Parents (
  foster_parent_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  email VARCHAR(90) NOT NULL,
  phone VARCHAR(12),
  PRIMARY KEY (foster_parent_id)
);

-- CREATE Cats table 
CREATE OR REPLACE TABLE Cats (
  cat_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  name VARCHAR(45) NOT NULL,
  date_of_birth DATE,
  weight DECIMAL(10,2),
  color VARCHAR(45),
  sex VARCHAR(10),
  adoptable VARCHAR(10),
  last_vet_check DATE,
  PRIMARY KEY (cat_id)
);

-- CREATE Cafe_Products table
CREATE OR REPLACE TABLE Cafe_Products (
  product_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  name VARCHAR(45) NOT NULL,
  price DECIMAL(19,2),
  quantity INT,
  product_type VARCHAR(45) NOT NULL DEFAULT 'Other',
  PRIMARY KEY (product_id)
);

-- CREATE Adoptions table
CREATE OR REPLACE TABLE Adoptions (
  adoption_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  customer_id INT,
  cat_id INT,
  foster_parent_id INT,
  employee_id INT,
  date DATE,
  PRIMARY KEY (adoption_id),
  FOREIGN KEY (customer_id) REFERENCES Customers (customer_id) ON DELETE SET NULL,
  FOREIGN KEY (cat_id) REFERENCES Cats (cat_id) ON DELETE SET NULL,
  FOREIGN KEY (foster_parent_id) REFERENCES Foster_Parents (foster_parent_id) ON DELETE SET NULL,
  FOREIGN KEY (employee_id) REFERENCES Employees (employee_id) ON DELETE SET NULL
);

-- CREATE Cafe_Transactions Table
CREATE OR REPLACE TABLE Cafe_Transactions (
  transaction_id INT AUTO_INCREMENT UNIQUE NOT NULL,
  customer_id INT NOT NULL,
  employee_id INT,
  order_date DATE,
  total_price DECIMAL(19,2),
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (customer_id) REFERENCES Customers (customer_id) ON DELETE SET NULL,
  FOREIGN KEY (employee_id) REFERENCES Employees (employee_id) ON DELETE SET NULL
);

-- CREATE Product_Orders table to facilitate M:N relationship between Cafe_Transactions and Cafe_Products
CREATE OR REPLACE TABLE Product_Orders (
  product_order_id INT AUTO_INCREMENT NOT NULL,
  transaction_id INT,
  product_id INT,
  quantity INT,
  PRIMARY KEY (product_order_id),
  FOREIGN KEY (transaction_id) REFERENCES Cafe_Transactions (transaction_id) ON DELETE SET NULL,
  FOREIGN KEY (product_id) REFERENCES Cafe_Products (product_id) ON DELETE SET NULL
);

-- CREATE Foster parent and cat relationship to facilitate the M:N relationship between Foster Parents and Cats
CREATE OR REPLACE TABLE Foster_Cat_Relationships (
  relationship_id INT AUTO_INCREMENT NOT NULL,
  cat_id INT,
  foster_parent_id INT,
  PRIMARY KEY (relationship_id),
  FOREIGN KEY (cat_id) REFERENCES Cats (cat_id) ON DELETE SET NULL,
  FOREIGN KEY (foster_parent_id) REFERENCES Foster_Parents (foster_parent_id) ON DELETE SET NULL
);

-- Inserting data into entities

-- INSERT Pedro, Bella, and Gabriel into Customers
INSERT INTO Customers (first_name, last_name, email, phone)
VALUES ('Pedro', 'Pascal', 'ppascal@gmail.com', '541-123-4567'),
('Bella', 'Ramsey', 'bramsey@gmail.com', '541-890-1234'),
('Gabriel', 'Luna', 'gluna@gmail.com', '541-982-1235');

-- INSERT Arya, Sansa, and Jon into Employees
INSERT INTO Employees (first_name, last_name, email, phone, hourly_salary)
VALUES ('Arya', 'Stark', 'astark@gmail.com', '541-212-2121', 30.00),
('Sansa', 'Stark', 'sstark@gmail.com', '541-434-4343', 34.50),
('Jon', 'Snow', 'jsnow@gmail.com', '541-111-5555', 29.75);

-- INSERT Ian, Patrick, and Scarlet into Foster_Parents 
INSERT INTO Foster_Parents (first_name, last_name, email, phone)
VALUES ('Ian', 'McKellen', 'ikellen@gmail.com', '541-989-9898'),
('Patrick', 'Stewart', 'pstewart@gmail.com', '541-767-7676'),
('Scarlet', 'Johansson', 'sjohansson@gmail.com', '541-656-2121');

-- INSERT Lilly, Jasper, Pumpkin, Bean, and Juniper into Cats
INSERT INTO Cats (name, date_of_birth, weight, color, sex, adoptable, last_vet_check)
VALUES ('Lilly', '2006-08-27', 6.0, 'gray', 'female', 'yes', '2023-10-03'),
('Jasper', '2015-05-12', 9.2, 'black', 'female', 'yes', '2023-02-05'),
('Pumpkin', '2020-11-10', 11.6, 'orange', 'male', 'no', '2023-04-11'),
('Bean', '2009-06-07', 13.4, 'calico', 'female', 'yes', '2023-07-25'),
('Juniper', '2023-04-15', 4.0, 'tabby', 'male', 'no', '2023-09-23');

-- INSERT Vanilla Latte, Plain Bagel, Blueberry Muffin, and Green Tea into Cafe_Products table
INSERT INTO Cafe_Products (name, price, quantity, product_type)
VALUES ('Vanilla latte', 3.75, 110, 'beverage'),
('Plain bagel', 2.50, 35, 'food'),
('Blueberry muffin', 3.00, 42, 'food'),
('Green tea', 3.25, 203, 'beverage');

-- INSERT Adoption transactions into Adoptions table
INSERT INTO Adoptions (customer_id, cat_id, foster_parent_id, employee_id, date)
VALUES ((SELECT customer_id FROM Customers WHERE customer_id = 2), (SELECT cat_id FROM Cats WHERE cat_id = 3), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 2), (SELECT employee_id FROM Employees WHERE employee_id = 1), '2023-10-15'),
((SELECT customer_id FROM Customers WHERE customer_id = 1), (SELECT cat_id FROM Cats WHERE cat_id = 4), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 1), (SELECT employee_id FROM Employees WHERE employee_id = 2), '2023-10-20'),
((SELECT customer_id FROM Customers WHERE customer_id = 3), (SELECT cat_id FROM Cats WHERE cat_id = 2), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 3), (SELECT employee_id FROM Employees WHERE employee_id = 3), '2023-09-22');

-- INSERT cafe transaction into Cafe_Transactions table
INSERT INTO Cafe_Transactions (customer_id, employee_id, order_date, total_price)
VALUES ((SELECT customer_id FROM Customers WHERE customer_id = 1), (SELECT employee_id FROM Employees WHERE employee_id = 1), '2023-08-21', 6.00),
((SELECT customer_id FROM Customers WHERE customer_id = 2), (SELECT employee_id FROM Employees WHERE employee_id = 2), '2023-10-15', 3.25),
((SELECT customer_id FROM Customers WHERE customer_id = 3), (SELECT employee_id FROM Employees WHERE employee_id = 2), '2023-09-22', 7.50);

-- INSERT order into Product_Orders table
INSERT INTO Product_Orders (transaction_id, product_id, quantity)
VALUES ((SELECT transaction_id FROM Cafe_Transactions WHERE transaction_id = 2), (SELECT product_id FROM Cafe_Products WHERE product_id = 3), 2),
((SELECT transaction_id FROM Cafe_Transactions WHERE transaction_id = 1), (SELECT product_id FROM Cafe_Products WHERE product_id = 4), 1),
((SELECT transaction_id FROM Cafe_Transactions WHERE transaction_id = 3), (SELECT product_id FROM Cafe_Products WHERE product_id = 2), 3);

-- INSERT foster-cat-relationship into Foster_Cat_Relationship Table
INSERT INTO Foster_Cat_Relationships (cat_id, foster_parent_id)
VALUES ((SELECT cat_id FROM Cats WHERE cat_id = 1), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 2)),
((SELECT cat_id FROM Cats WHERE cat_id = 2), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 1)),
((SELECT cat_id FROM Cats WHERE cat_id = 3), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 2)),
((SELECT cat_id FROM Cats WHERE cat_id = 4), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 1)),
((SELECT cat_id FROM Cats WHERE cat_id = 5), (SELECT foster_parent_id FROM Foster_Parents WHERE foster_parent_id = 3));