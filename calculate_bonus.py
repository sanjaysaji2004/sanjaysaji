def calculate_bonus(salary: float, grade: str) -> float:
    bonus = 0
    if salary < 10000:
        bonus += 0.02 * salary
    if grade == 'A':
        bonus += 0.05 * salary
    elif grade == 'B':
        bonus += 0.10 * salary
    return salary + bonus

salary = float(input("Enter salary: "))
grade = input("Enter grade (A or B): ")

print("Total salary:", calculate_bonus(salary, grade))
