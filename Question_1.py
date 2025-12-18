
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# Task A:
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    city VARCHAR(100)
)
""")

# Task B:
cursor.execute("INSERT INTO students (name, age, city) VALUES ('John', 20, 'New York')")
cursor.execute("INSERT INTO students (name, age, city) VALUES ('Sarah', 22, 'Boston')")

conn.commit()

# Task C:
cursor.execute("SELECT * FROM students WHERE age > 21")
results = cursor.fetchall()

print("Students older than 21:")
for row in results:
    print(row)

cursor.close()
conn.close()
