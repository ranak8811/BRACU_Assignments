# Sub task --> 1
# It runs in O(nlogn)

f1 = open('input2.txt', 'r')
f2 = open('output2.txt', 'w')

N = int(f1.readline().strip())
nl = list(map(int, f1.readline().strip().split()))
M = int(f1.readline().strip())
ml = list(map(int, f1.readline().strip().split()))

a = 0
b = 0
f = ''

while a < N and b < M:
    if nl[a] <= ml[b]:
        f += str(nl[a]) + ' '
        a += 1
    else:
        f += str(ml[b]) + ' '
        b += 1
while a < N:
    f += str(nl[a]) + ' '
    a += 1
while b < M:
    f += str(ml[b]) + ' '
    b += 1
f2.write(f)

f1.close()
f2.close()


# Sub task --> 2
# It runs in O(n)

f1 = open('input2.txt', 'r')
f2 = open('output2.txt', 'w')

N = int(f1.readline().strip())
nl = list(map(int, f1.readline().strip().split()))
M = int(f1.readline().strip())
ml = list(map(int, f1.readline().strip().split()))

a = 0
b = 0
f = ''
for i in range(N+M):
    if a == N:
        f = f"{f} {ml[b]}"
        b += 1
    elif b == M:
        f = f"{f} {nl[a]}"
        a += 1
    elif nl[a] < ml[b]:
        f = f"{f} {nl[a]}"
        a += 1
    else:
        f = f"{f} {ml[b]}"
        b += 1

f2.write(f)

f1.close()
f2.close()
