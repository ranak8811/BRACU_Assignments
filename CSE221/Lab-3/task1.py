inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

n = int(inp.readline().strip())
lst = list(map(int, inp.readline().strip().split()))

c = 0

def alienCount(arr):
    global c
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        alienCount(left_half)
        alienCount(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
                c += len(right_half) - j
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

alienCount(lst)
out.write(str(c))

inp.close()
out.close()