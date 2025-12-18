from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# Task A:
cursor.execute("""
UPDATE students
SET age = 23
WHERE name = 'Sarah'
""")
conn.commit()
print(f"{cursor.rowcount} record(s) updated successfully.\n")

# Task B:
cursor.execute("""
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city
""")

print("Number of students per city: ")
for city, count in cursor.fetchall():
    print(f"{city}: {count}")

# Task C:
cursor.execute("""
SELECT name
FROM students
ORDER BY name ASC
""")
print(" Students names in alphabetical order: ")
for (name,) in cursor.fetchall():
    print(name)

cursor.close()
conn.close()
