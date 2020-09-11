import sqlite3

# connect to database
conn = sqlite3.connect('customer.db')

# create a cursor
cursor = conn.cursor()

# create a table
# cursor.execute("""CREATE TABLE customers (
#       first_name text,
#        last_name text,
#        email text
#    )""")

# Insert row into the table
# cursor.execute("INSERT INTO customers VALUES ('Cyrus', 'Jonker', 'cyrus.jonker@gmail.com')")

# Insert many into a table
# many_customers = [
#                  ('mom', 'angie', 'mom@angie.com'),
#                 ('dad', 'johan', 'dad@johan.com'),
#                ('lizzy', 'Jonker', 'lizzy@jonker.com')
#        ]

# cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# cursor.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

# different data-types
# null
# integer
# real
# text
# blob

cursor.execute("SELECT * FROM customers WHERE last_name = 'Jonker'")
rows = cursor.fetchall()

for row in rows:
    print(row)

print('Commited successfully')

# commit our command
conn.commit()

# close our connection
conn.close()