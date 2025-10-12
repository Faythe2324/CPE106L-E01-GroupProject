import sqlite3

# Connect to SQLite database (creates employee.db if not exists)
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

# Drop tables if they exist (to allow re-run)
cursor.execute("DROP TABLE IF EXISTS Employee")
cursor.execute("DROP TABLE IF EXISTS Salary")
cursor.execute("DROP TABLE IF EXISTS test")

# Create Employee table
cursor.execute("""
CREATE TABLE Employee (
    EmpID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    HireDate TEXT,
    Grade TEXT,
    ManagerID INTEGER
)
""")

# Create Salary table
cursor.execute("""
CREATE TABLE Salary (
    SalaryID INTEGER PRIMARY KEY,
    Grade TEXT NOT NULL,
    Amount INTEGER
)
""")

# Create test table
cursor.execute("""
CREATE TABLE test (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER
)
""")

# Insert Employee data
cursor.executemany("INSERT INTO Employee VALUES (?, ?, ?, ?, ?)", [
    (1, 'John Brown', '20030623', 'Foreman', None),
    (2, 'Fred Smith', '20040302', 'Labourer', 1),
    (3, 'Anne Jones', '19991125', 'Labourer', 1)
])

# Insert Salary data
cursor.executemany("INSERT INTO Salary VALUES (?, ?, ?)", [
    (1, 'Foreman', 60000),
    (2, 'Labourer', 35000)
])

# Insert test data
cursor.executemany("INSERT INTO test VALUES (?, ?, ?)", [
    (1, 'Alan', 24),
    (2, 'Heather', 42),
    (3, 'Laura', None)
])

# Commit changes and close connection
conn.commit()
conn.close()

print("employee.db created successfully! Open in DB Browser and run:")
print("SELECT * FROM Employee, Salary, test;")
