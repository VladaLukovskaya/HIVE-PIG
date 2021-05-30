#!/usr/bin/python3
from sys import stdin

for line in stdin:
    data = line.strip().split(',')
    if data[1] == '3':
        print(f'{data[2]},{data[3]}')
