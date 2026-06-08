# GRADE CONVERSION - NUMERIC TO ALPHABETIC

marks = int(input("Enter your Marks: "))

if marks > 90:
    grade = 'O'
elif marks >= 80:
    grade = 'A'
elif  marks >= 70:
    grade = 'B'
elif  marks >= 60:
    grade = 'C'
elif  marks >= 35:
    grade = 'D'
else:
    grade = 'F'

print(f'Your Grade is {grade}')
    
