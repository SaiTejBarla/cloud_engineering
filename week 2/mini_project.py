import sqlite3

# Connect (creates student.db if not exists)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        grade TEXT
    )
""")

# Insert data
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", ("Alice", 20, "A"))

# Save changes
conn.commit()

# Fetch and print data
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print("All students:")
for row in rows:
    print(row)

# Close connection
conn.close()
