import sqlite3

#Połączenie z istniejącą bazą danych
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
# Wykonanie zapytania
cursor.execute("SELECT * FROM sales")
# Pobranie i wyświetlenie wyników
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

print("\n1A ↓\n")

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sales WHERE product = 'Laptop'")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()


print("\n1B ↓\n")

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sales WHERE date = '2025-05-07' OR date = '2025-05-08'")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

print("\n1C ↓\n")

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM sales WHERE price > 200")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()

print("\n1D ↓\n")

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT Product, SUM(Price)  FROM sales GROUP BY Product")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()


print("\n1E ↓\n")

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()
cursor.execute("SELECT date, MAX(PRICE) FROM (SELECT date, SUM(price) as PRICE FROM sales GROUP BY date)")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
