student_scores = {
    "Harry": 81.0,
    "Ron": "78.0",
    "Hermione": "99.0",
    "Draco": "74.0",
    "Neville": "62.0"
}

student_grades = {}

for student in student_scores:
    score = float(student_scores[student])
    grade = ''

    if score > 90:
        grade = 'Outstanding'
    elif score > 80:
        grade = 'Exceeds Expectations'
    elif score > 70:
        grade = 'Acceptable'
    else:
        grade = 'Fail'

    student_grades[student] = grade

print(student_grades)
