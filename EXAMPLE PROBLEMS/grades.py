score = float(input("Enter the student's score: "))

if score >= 90:
    letter_grade = 'A'
elif score >= 60:
    letter_grade = 'B'
else:
    letter_grade = 'F'

print(f'Student\'s score: {score}')
print(f'Letter grade: {letter_grade}')
# f is used to format the output
