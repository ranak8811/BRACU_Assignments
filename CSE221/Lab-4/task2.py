from collections import deque

inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n, m = map(int, inp.readline().strip().split())

d = {}
for i in range(1, n+1):
    d[i] = []

for _ in range(m):
    u, v = map(int, inp.readline().strip().split())
    d[u].append(v)
    
# print(d)

def BFS(G, s):
    a = [0 for _ in range(n+1)]
    q = deque()
    q.append(s)
    a[s] = 1
    t = str(s) + " "
    while q:
        u = q.popleft()
        for i in G[u]:
            if a[i] == 0:
                q.append(i)
                a[i] = 1
                t += str(i) + " "
    # print(t)
    out.write(t)

BFS(d, 1)

inp.close()
out.close()