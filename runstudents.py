from com.abc.lib.student_ops import get_details, print_grade

name = input('Enter name: ')
gender = input('Enter gender: ')
roll = int(input('Enter roll: '))
marks = float(input('Enter marks: '))

print(get_details(name=name, roll=roll, gender=gender, marks=marks))
print_grade(marks)

