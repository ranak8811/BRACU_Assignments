inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

n, m = map(int, inp.readline().strip().split())
l = [list(map(int, inp.readline().strip().split())) for _ in range(m)]

x = [[i + 1] for i in range(n)]
s = []

for i in range(m):
    a, b = l[i]
    m = -1
    n = -1

    for j in range(len(x)):
        if a in x[j]:
            m = j
        if b in x[j]:
            n = j

    if m != n:
        t = x[m] + x[n]
        del x[max(m, n)]
        del x[min(m, n)]
        x.append(t)
        s.append(len(t))
    else:
        s.append(len(x[m]))

for i in s:
    out.write(str(i) + '\n')

inp.close()
out.close()