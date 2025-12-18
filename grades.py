
score1 = float(input("Enter first exam score: "))
score2 = float(input("Enter second exam score: "))
score3 = float(input("Enter third exam score: "))

average = (score1 + score2 + score3) / 3
print(f"Average score: {average:.2f}")

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")
