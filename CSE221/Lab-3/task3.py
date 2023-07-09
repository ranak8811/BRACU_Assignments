inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

n = int(inp.readline().strip())
lst = list(map(int, inp.readline().strip().split()))

def Partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def Quick_sort(A, p, r):
    if p < r:
        pivot_index = Partition(A, p, r)
        Quick_sort(A, p, pivot_index - 1)
        Quick_sort(A, pivot_index + 1, r)


Quick_sort(lst, 0, len(lst) - 1)

f = ''
for i in lst:
    f += str(i) + ' '
out.write(f)

inp.close()
out.close()