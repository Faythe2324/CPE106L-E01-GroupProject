import sqlite3

# Connect to SQLite database (creates lendy.db if not exists)
conn = sqlite3.connect("lendy.db")
cursor = conn.cursor()

# Drop tables if they exist (so script can be rerun)
cursor.execute("DROP TABLE IF EXISTS Item")
cursor.execute("DROP TABLE IF EXISTS Loan")
cursor.execute("DROP TABLE IF EXISTS Member")

# Create Item table
cursor.execute("""
CREATE TABLE Item (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Description TEXT,
    OwnerID INTEGER,
    Price INTEGER,
    Condition TEXT,
    DateRegistered TEXT
)
""")

# Create Loan table
cursor.execute("""
CREATE TABLE Loan (
    ID INTEGER PRIMARY KEY,
    ItemID INTEGER,
    MemberID INTEGER,
    DateOut TEXT,
    DateDue TEXT,
    DateReturned TEXT,
    FOREIGN KEY(ItemID) REFERENCES Item(ID),
    FOREIGN KEY(MemberID) REFERENCES Member(ID)
)
""")

# Create Member table
cursor.execute("""
CREATE TABLE Member (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT
)
""")

# Insert Item data
cursor.executemany("INSERT INTO Item VALUES (?, ?, ?, ?, ?, ?, ?)", [
    (1, 'Lawnmower', 'Tool', 1, 150, 'Excellent', '2012-01-05'),
    (2, 'Lawnmower', 'Tool', 2, 370, 'Fair', '2012-04-01'),
    (3, 'Bike', 'Vehicle', 3, 200, 'Good', '2013-03-22'),
    (4, 'Drill', 'Tool', 4, 100, 'Good', '2013-10-28'),
    (5, 'Scarifier', 'Tool', 5, 200, 'Average', '2013-09-14'),
    (6, 'Sprinkler', 'Tool', 1, 80, 'Good', '2014-01-06')
])

# Insert Loan data
cursor.executemany("INSERT INTO Loan VALUES (?, ?, ?, ?, ?, ?)", [
    (1, 1, 3, '2012-01-04', '2012-04-26', None),
    (2, 5, 2, '2012-09-07', '2013-01-05', None),
    (3, 4, 1, '2013-07-03', '2013-07-22', None),
    (4, 3, 1, '2013-11-19', '2013-11-29', None),
    (5, 5, 2, '2013-12-05', None, None)
])

# Insert Member data
cursor.executemany("INSERT INTO Member VALUES (?, ?, ?)", [
    (1, 'Fred', 'fred@lendylib.org'),
    (2, 'Mike', 'mike@gmail.com'),
    (3, 'Joe', 'joej@oesmail.com'),
    (4, 'Rob', 'rbj@scorp.com'),
    (5, 'Anne', 'annie@bigbiz.com')
])

# Commit changes and close
conn.commit()
conn.close()

print("lendy.db created successfully! Open in DB Browser and run:")
print("SELECT * FROM Item, Loan, Member;")
