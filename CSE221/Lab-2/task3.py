f1 = open('input3.txt', 'r')
f2 = open('output3.txt', 'w')

n = f1.readline().strip()
data = list(map(int, f1.readline().strip().split()))


def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        a1 = mergeSort(arr[:mid])
        a2 = mergeSort(arr[mid:])
        return merge(a1, a2)


sorted_data = mergeSort(data)
f = ''
for i in sorted_data:
    f += str(i) + ' '
f2.write(f)

f1.close()
f2.close()
