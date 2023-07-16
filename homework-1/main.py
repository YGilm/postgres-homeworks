"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='north',
    user='postgres',
    password='12345'
)

try:
    # Создание курсора
    cur = conn.cursor()

    # Заполнение таблицы employees данными из файла CSV
    with open('north_data/employees_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)", row)

    # Заполнение таблицы customers данными из файла CSV
    with open('north_data/customers_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)", row)

    # Заполнение таблицы orders данными из файла CSV
    with open('north_data/orders_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)", row)

    # Коммит
    conn.commit()

except (Exception, psycopg2.Error) as error:
    print("Ошибка при работе с PostgreSQL:", error)

finally:
    # Закрытие соединения
    if conn:
        conn.close()
