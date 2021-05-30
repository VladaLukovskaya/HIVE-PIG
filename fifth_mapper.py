from sys import stdin

for line in stdin:
    data = line.strip().split(',')
    if len(data) == 5:
        print(f'{data[4]},{data[0]},{data[1]},{data[2]},{data[3]}')
    else:
        print(f'{data[0]},{data[2]},{data[3]},{data[1]}')
