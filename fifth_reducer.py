from sys import stdin

last_emp = emp_id = ''

for line in stdin:
    data = line.strip().split(',')

    if last_emp != '' and last_emp != emp_id:
        print(f'{emp_id},{emp_surname},{emp_name},{position},{dep_id},{dep_id},{dep_name},{num_of_emp},{head}')

    if len(data) == 5:
        last_emp = emp_id
        emp_id = data[1]
        dep_id = data[0]
        emp_surname = data[2]
        emp_name = data[3]
        position = data[4]
    else:
        dep_name = data[3]
        num_of_emp = data[1]
        head = data[2]
        if last_emp == emp_id == '':
            # last_emp = ''
            emp_id = 'new'
        else:
            last_emp = ''
            emp_id = 'new'

print(f'{emp_id},{emp_surname},{emp_name},{position},{dep_id},{dep_id},{dep_name},{num_of_emp},{head}')
