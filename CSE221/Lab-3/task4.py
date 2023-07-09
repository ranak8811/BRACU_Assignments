inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

N = int(inp.readline())
num = list(map(int, inp.readline().split()))
Q = int(inp.readline())

def find_kth_smallest(a, k):
    if len(a) == 1:
        return a[0]

    p = a[0]
    l = []
    r = []
    for x in a[1:]:
        if x <= p:
            l.append(x)
        else:
            r.append(x)

    if k <= len(l):
        return find_kth_smallest(l, k)
    elif k == len(l) + 1:
        return p
    else:
        return find_kth_smallest(r, k - len(l) - 1)

for _ in range(Q):
    K = int(inp.readline())
    kth_smallest = find_kth_smallest(num, K)
    out.write(str(kth_smallest) + '\n')

inp.close()
out.close()