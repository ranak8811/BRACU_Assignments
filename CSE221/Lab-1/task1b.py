f1 = open('input1b.txt', 'r')
f2 = open('output1b.txt', 'w')

T = int(f1.readline().strip())

for i in range(T):
    curr_ope = f1.readline().strip()

    lst = curr_ope.split(' ')
    if lst[2] == '+':
        add = int(lst[1]) + int(lst[3])
        f2.write(f"The result of {lst[1]} + {lst[3]} is {add}\n")
    elif lst[2] == '-':
        sub = int(lst[1]) - int(lst[3])
        f2.write(f"The result of {lst[1]} - {lst[3]} is {sub}\n")
    elif lst[2] == '*':
        mul = int(lst[1]) * int(lst[3])
        f2.write(f"The result of {lst[1]} * {lst[3]} is {mul}\n")
    elif lst[2] == '/':
        div = int(lst[1]) / int(lst[3])
        f2.write(f"The result of {lst[1]} / {lst[3]} is {div}\n")

f1.close()
f2.close()