from sys import stdin
import string

for line in stdin:
    data = line.strip().split(',')
    if data[1] in string.digits:
        print(f'{data[1]},{data[0]},{data[2]},{data[3]}')
    else:
        data = ','.join(data)
        print(data)
