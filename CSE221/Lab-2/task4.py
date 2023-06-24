f1 = open('input4.txt', 'r')
f2 = open('output4.txt', 'w')

n = f1.readline().strip()
data = list(map(int, f1.readline().strip().split()))


def find_max_value(arr):
    if len(arr) == 1:
        return arr[0]

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_max = find_max_value(left_half)
    right_max = find_max_value(right_half)

    if left_max > right_max:
        return left_max
    else:
        return right_max


max_value = find_max_value(data)
f2.write(str(max_value))

f1.close()
f2.close()


# Time complexity of this code is O(n).
