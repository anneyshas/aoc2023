f = open("input-1.txt", "r")
entry = f.read()
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