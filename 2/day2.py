#!/usr/bin/python

import sys
import string

path = "input.txt"

def day2():
    count2 = 0
    count3 = 0
    for line in open(path):
        control = dict.fromkeys(string.ascii_lowercase, 0)
        line = line.replace("\n", "")
        for letter in line:
            control[letter] += 1
        if 2 in control.values():
            count2 += 1
        if 3 in control.values():
            count3 += 1
        # print('control: {0} value: {1} : {2}'.format(control,count2, count3))
    print('{0} x {1} = {2}'.format(count2,count3,count2*count3))

def day2_2():
    data = [line.strip() for line in open(path)]
    for line, index in zip(data, range(len(data))):
        for comp in data[index:]:
            diff, result = compare(line, comp)
            if diff == 1:
                print(result)
    set(line)

def compare(str1, str2):
    diff = 0
    for letter1, letter2, ind in zip(str1, str2, range(len(str1))):
        if letter1 != letter2:
            diff += 1
            str1 = str1[:ind]+str1[ind+1:]
    return diff, str1

if __name__ == "__main__":
    day2()
    day2_2()
