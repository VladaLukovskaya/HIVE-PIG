from sys import stdin
import string

key = last_key = ''

for line in stdin:
    data = line.strip().split(',')
    last_key = key
    key = data[0]

    if last_key != '' and last_key != key:
        print(f'{last_key},{dep_name},{num_of_emp},{head_surname},{head_name}')

    if data[1] in string.digits:
        head_surname = data[2]
        head_name = data[3]
    else:
        dep_name = data[1]
        num_of_emp = data[2]

print(f'{last_key},{dep_name},{num_of_emp},{head_surname},{head_name}')
