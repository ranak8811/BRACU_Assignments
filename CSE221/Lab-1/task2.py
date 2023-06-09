f1 = open('input2.txt', 'r')
f2 = open('output2.txt', 'w')

num_of_elem = int(f1.readline().strip())
arr = list(map(int, f1.readline().strip().split(' ')))

def bubbleSort(arr):
    for i in range(len(arr)-1):
        is_swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_swapped = True
        if not is_swapped:
            break

# To achieve θ(n) for the best case scenario, we can check if any swap occurred in the inner loop.
# If no swap occurred, it means the array is already sorted and we can terminate the sorting process early.
# By breaking out of the outer loop when no swap occurs in the inner loop, we can achieve a best-case time complexity of θ(n).


bubbleSort(arr)
sorted_arr = ' '.join(map(str,arr))

f2.write(sorted_arr)

f1.close()
f2.close()