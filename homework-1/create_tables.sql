-- SQL-команды для создания таблиц
CREATE TABLE employees (
    employee_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(50) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
);

ALTER TABLE employee RENAME TO employees;
ALTER TABLE employees
ADD PRIMARY KEY (employee_id);

CREATE TABLE customers (
    customer_id VARCHAR(10),
    company_name VARCHAR(50),
    contact_name VARCHAR(50)
);

ALTER TABLE customers
ADD PRIMARY KEY (customer_id);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(10) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date varchar(10) NOT NULL,
	ship_city varchar(30) NOT NULL
);