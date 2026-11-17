# Task 9: grades dictionary

grades = {"Математика": 5, "Физика": 4, "Химия": 3}

for subject, grade in grades.items():
    print(f"{subject}: {grade}")

average = sum(grades.values()) / len(grades)

print("Средняя оценка:", average)

