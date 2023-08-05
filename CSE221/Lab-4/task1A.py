# Sub task - A

inp = open('input1a_2.txt', 'r')
out = open('output1a_2.txt', 'w')

v, e = map(int, inp.readline().strip().split())

a = []
max_index = 0

for i in range(e):
    row = list(map(int, inp.readline().strip().split()))
    c1, c2, v = row
    a.append([c1, c2, v])
    max_index = max(max_index, c1, c2)
# print(a)
# print(max_index)

farr = [[0] * (max_index + 1) for _ in range(max_index + 1)]
# print(farr)

for i in range(e):
    c1, c2, v = a[i]
    farr[c1][c2] = v
# print(farr)

f = ''
for i in range(max_index + 1):
    for j in range(max_index + 1):
        f += str(farr[i][j]) + ' '
    f += '\n'

out.write(f)

inp.close()
out.close()