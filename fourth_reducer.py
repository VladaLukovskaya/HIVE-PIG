from sys import stdin
import string

emp = last_emp = ''

for line in stdin:
    data = line.strip().split(',')

    if last_emp != emp and last_emp != '':
        print(f'{head_surname},{head_name},{emp_position}')

    if data[1] in string.digits:
        head_surname = data[2]
        head_name = data[3]
        last_emp = ''
        emp = 'new'
    else:
        last_emp = emp
        emp = data[2]
        emp_position = data[1]

print(f'{head_surname},{head_name},{emp_position}')
