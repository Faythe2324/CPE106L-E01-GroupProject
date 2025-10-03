import sqlite3

# Connect to SQLite database (creates books.db if it doesn't exist)
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Drop tables if they exist (for re-run convenience)
cursor.execute("DROP TABLE IF EXISTS Employee")
cursor.execute("DROP TABLE IF EXISTS Salary")
cursor.execute("DROP TABLE IF EXISTS Author")
cursor.execute("DROP TABLE IF EXISTS Book")
cursor.execute("DROP TABLE IF EXISTS Book_Author")

# Create tables
cursor.execute("""
CREATE TABLE Employee (
    EmpID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    HireDate TEXT,
    Grade TEXT,
    ManagerID INTEGER
)
""")

cursor.execute("""
CREATE TABLE Salary (
    SalaryID INTEGER PRIMARY KEY,
    Grade TEXT NOT NULL,
    Amount INTEGER
)
""")

cursor.execute("""
CREATE TABLE Author (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE Book (
    ID INTEGER PRIMARY KEY,
    Title TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE Book_Author (
    BookID INTEGER,
    AuthorID INTEGER,
    FOREIGN KEY(BookID) REFERENCES Book(ID),
    FOREIGN KEY(AuthorID) REFERENCES Author(ID)
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

# Insert Author data
cursor.executemany("INSERT INTO Author VALUES (?, ?)", [
    (1, 'Jane Austin'),
    (2, 'Grady Booch'),
    (3, 'Ivar Jacobson'),
    (4, 'James Rumbaugh')
])

# Insert Book data
cursor.executemany("INSERT INTO Book VALUES (?, ?)", [
    (1, 'Pride & Prejudice'),
    (2, 'Emma'),
    (3, 'Sense & Sensibility'),
    (4, 'Object Oriented Design with Applications'),
    (5, 'The UML User Guide')
])

# Insert Book_Author data
cursor.executemany("INSERT INTO Book_Author VALUES (?, ?)", [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (5, 3),
    (5, 4)
])

# Commit and close
conn.commit()
conn.close()

print("Database created successfully! Open books.db in DB Browser and run:")
print("SELECT * FROM Employee, Salary, Author, Book, Book_Author;")
