# SQLITE DATABASE

# <-------------------- CREATE SQLITE CONNECTION ----------------------->
import sqlite3

# Data will save temporary
# after close app all the previous data will be loss
# con = sqlite3.connect(':memory:') <--- !this line

# Connect to database
conn = sqlite3.connect("ICS2.db")  # <----- ! IC2.db (database name)
# <-------------------- CREATE SQLITE CONNECTION ----------------------->

# <-------------------- CREATE CURSOR ----------------------->
c = conn.cursor()
# <-------------------- CREATE CURSOR ----------------------->

# <-------------------- CREATE CURSOR ----------------------->
# <-------------------- CREATE TABLE ----------------------->

# using triple quotations, enable us to write db query in multiple line
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text,
#     )""")

# using single quotations, disable us to write db query in multiple line
# c.execute("CREATE TABLE customers (first_name DATATYPE,last_name DATATYPE,email DATATYPE)")

# <-------------------- CREATE TABLE ----------------------->

# <-------------------- DATATYPE ----------------------->

# DATATYPE use in sqlite
# null
# INTEGER
# REAL
# TEXT
# BLOB

# <-------------------- DATATYPE ----------------------->

# <-------------------- INSERT ----------------------->

# c.execute("INSERT INTO customers VALUES ('user1', '_u', 'user1@gmail.com')")

# <-------------------- INSERT ----------------------->

# <-------------------- INSERT MANY ----------------------->

# DATA
manyCustomers = [
    ('user3', '_u', 'user3@gmail.com'),
    ('user4', '_u', 'user4@gmail.com'),
    ('user5', '_u', 'user5@gmail.com')
]

# INSERT MULTIPLE DATA
c.executemany("INSERT INTO customers VALUES (?,?,?)", manyCustomers)

# <-------------------- INSERT MANY ----------------------->

# <-------------------- QUERY AND FETCH ALL ----------------------->

# Query the database
c.execute("SELECT * FROM customers")

# Three ways to fetch data from table
# c.fetchone()
# c.fetchmany(3)
# c.fetchall()

# FETCH ALL
# _one = c.fetchone()
# print('Ony a row \n', _one) # <---- !print first record from database save data

# _many = c.fetchmany(3)
# print("depends on parameter \n", _many)  # <- !print rows a/c to parameter

# _all = c.fetchall()
# print('ALL DATA \n', _all)  # <---- !print all database save data

# <-------------------- QUERY AND FETCH ALL ----------------------->


# <-------------------- get specific ----------------------->

# <-------------------- get specific ----------------------->

# After Success
print("Command successfully exceed!")

# <-------------------- COMMIT AND CLOSE ----------------------->

# Commit our command
conn.commit()

# Close the connection
conn.close()

# <-------------------- COMMIT AND CLOSE ----------------------->



