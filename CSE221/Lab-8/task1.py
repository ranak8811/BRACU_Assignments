inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

n, m = map(int, inp.readline().strip().split())
l = [list(map(int, inp.readline().strip().split())) for _ in range(m)]

l.sort(key=lambda x: x[2])

x = [[i + 1] for i in range(n)]

s = 0
for i in range(len(l)):
    a, b, c = l[i]
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
        s += c

out.write(str(s))

inp.close()
out.close()
