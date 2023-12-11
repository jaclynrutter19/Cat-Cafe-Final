-- CS340 - Introduction to Databases
-- Team Members: Jaclyn Rutter & Olivia Russell
-- Group 150
-- Data Manipulation Queries

-- Query for add a new character functionality with colon : character being used to 
-- denote the variables that will have data from the backend programming language

--------- Customers -----------

-- SHOW all Customers
SELECT * FROM Customers;

-- Create a new Customer
INSERT INTO Customers(first_name, last_name, email, phone)
VALUES (:first_name_input, :last_name_input, :email_input, :phone_input);

-- Update Customer
UPDATE Customers
SET first_name = :first_name_input, last_name = :last_name_input, email = :email_input, phone = :phone_input
WHERE customer_id = :customer_id_input;

-- Delete Customer
DELETE FROM Customers WHERE customer_id = :customer_id_selected;

--------- Employees -----------

-- SHOW all Employees First and Last Name.
SELECT first_name, last_name FROM Employees;

-- Create a new Employee
INSERT INTO Employees(first_name, last_name, email, phone, hourly_salary)
VALUES (:first_name_input, :last_name_input, :email_input, :phone_input, :hourly_salary);

-- Update Employee
UPDATE Employees
SET first_name = :first_name_input, last_name = :last_name, email = :email_input, phone = :phone_input, hourly_salary = :hourly_salary_input
WHERE employee_id = :employee_id_input;

-- Delete Employee
DELETE FROM Employees WHERE employee_id = :employee_id_selected;

--------- Foster_Parents -----------

-- SHOW all Foster_Parents
SELECT * FROM Foster_Parents;

-- Create a new Foster_Parent
INSERT INTO Foster_Parents(first_name, last_name, email, phone)
VALUES(:first_name_input, :last_name_input, :email_input, :phone_input);

-- Update Foster_Parents
UPDATE Foster_Parents
SET first_name = :first_name_input, last_name = :last_name_input, email = :email_input, phone = :phone_input
WHERE foster_parent_id = :foster_parent_id_input;

-- DELETE Foster_Parent 
DELETE FROM Foster_Parents WHERE foster_parent_id = :foster_parent_id_selected;

--------- Cats -----------

-- SHOW all Cats
SELECT * FROM Cats;

-- SHOW only Adoptable Cats
SELECT * FROM Cats
WHERE adoptable = "yes";

-- Create a new cat
INSERT INTO Cats(name, date_of_birth, weight, color, sex, adoptable, last_vet_check)
VALUES(:name, :date_of_birth, :weight, :color, :sex, :adoptable, :last_vet_check);

-- Update Cats
UPDATE Cats
SET name = :name_input, date_of_birth = :date_of_birth_input, weight = :weight_input, color = :color_input, sex = :sex_input, adoptable = :adoptable_input, last_vet_check = :last_vet_check_input
WHERE cat_id = :cat_id;

-- DELETE cat
DELETE FROM Cats WHERE cat_id = :cat_id_selected;

--------- Cafe_Products -----------

-- SHOW all Cafe_Products
SELECT * FROM Cafe_Products;

-- Create a new Cafe_Product
INSERT INTO Cafe_Products(name, price, quantity, product_type)
VALUES(:name, :price_input, :quantity_input, :product_type_input);

-- Update Cafe_Product
UPDATE Cafe_Products
SET name = :name_input, price = :price_input, quantity = :quantity_input, product_type = :product_type_input
WHERE product_id = :product_id_input;

-- DELETE Cafe_Product
DELETE FROM Cafe_Products WHERE product_id = :product_id_selected;

--------- Adoptions -----------

-- SHOW all Adoptions
SELECT * FROM Adoptions;

-- Create a new Adoption
INSERT INTO Adoptions(customer_id, cat_id, foster_parent_id, employee_id, date)
VALUES(:customer_id_input, :cat_id_input, :foster_parent_id_input, :employee_id, :date_input);

-- Update Adoptions
UPDATE Adoptions
SET customer_id = :customer_id_input, cat_id = :cat_id_input, foster_parent_id = :foster_parent_id_input, employee_id = :employee_id_input, date = :date_input
WHERE adoption_id = :adoption_id_input;

-- DELETE Adoption
DELETE FROM Adoptions WHERE adoption_id = :adoption_id_selected;

--------- Cafe_Transactions -----------

-- SHOW all Cafe_Transactions
SELECT * FROM Cafe_Transactions
  
-- Create a new Cafe_Transaction
INSERT INTO Cafe_Transactions(customer_id, employee_id, order_date, total_price)
VALUES(:customer_id_input, :employee_id_input, :order_date_input, :total_price_input)

-- UPDATE a Cafe_Transaction
UPDATE Cafe_Transactions
SET customer_id = :customer_id_input, employee_id = :employee_id_input, order_date = :order_date_input, total_price = :total_price_input
WHERE transaction_id = :transaction_id_input;

-- DELETE a Cafe_Transaction
DELETE FROM Cafe_Transactions WHERE transaction_id = :transaction_id_selected;

--------- Product_Orders -----------

-- Create a Product_Orders Certificate
INSERT INTO Product_Orders(transaction_id, product_id, quantity)
VALUES(:transaction_id_input, :product_id_input, quantity_input);

-- DELETE Product_Orders (Certificate)
DELETE FROM Product_Orders WHERE transaction_id = :transaction_id_selected AND product_id = :product_id_selected;

--------- Foster_Cat_Relationships -----------

-- Create a Foster_Cat_Relationship Certificate
INSERT INTO Foster_Cat_Relationships(cat_id, foster_parent_id)
VALUES(:cat_id_dropdown, :foster_parent_id_dropdown);

-- Delete a Foster_Cat_Relationship Certificate
DELETE FROM Foster_Cat_Relationships WHERE cat_id = :cat_id_dropdown AND foster_parent_id = :foster_parent_id_dropdown;