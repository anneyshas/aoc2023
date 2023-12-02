import re

f = open("input-1.txt", "r")
entry = f.read()

entry = entry.replace('one', 'o1e')
entry = entry.replace('two', 't2o')
entry = entry.replace('three', 't3e')
entry = entry.replace('four', 'f4r')
entry = entry.replace('five', 'f5e')
entry = entry.replace('six', 's6x')
entry = entry.replace('seven', 's7n')
entry = entry.replace('eight', 'e8t')
entry = entry.replace('nine', 'n9e')

lines = entry.count("\n")
i = 0
num_list = []

while i < len(entry):
    first = second = ""
    while entry[i] != "\n":
        if ord(entry[i]) >= 48 and ord(entry[i]) <= 57:
            if first == "":
                first = entry[i]
                second = entry[i]
            else:
                second = entry[i]
        i+=1
    num_list.append(int(first+second))
    i+=1

print(sum(num_list))