# Sub task - 1

f1 = open('input1.txt', 'r')
f2 = open('output1.txt', 'w')

fline = f1.readline().strip().split()
N = int(fline[0])
S = int(fline[1])

nums = list(map(int, f1.readline().strip().split()))
flag = False
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == S:
            f2.write(f"{i+1} {j+1}")
            flag = True

    if flag:
        break

if not flag:
    f2.write("IMPOSSIBLE")


f1.close()
f2.close()


# Sub task - 2

f1 = open('input1.txt', 'r')
f2 = open('output1.txt', 'w')

fline = f1.readline().strip().split()
N = int(fline[0])
S = int(fline[1])

nums = list(map(int, f1.readline().strip().split()))

num_lists = [[nums[i], i + 1] for i in range(N)]
num_lists.sort(key=lambda x: x[0])

left = 0
right = N - 1
flag = False
while left < right:
    curr_sum = num_lists[left][0] + num_lists[right][0]
    if curr_sum == S:
        idx1 = num_lists[left][1]
        idx2 = num_lists[right][1]
        f2.write(f"{idx1} {idx2}") if idx1 < idx2 else f2.write(
            f"{idx2} {idx1}")
        flag = True
        break
    elif curr_sum < S:
        left += 1
    else:
        right -= 1
if not flag:
    f2.write("IMPOSSIBLE")

f1.close()
f2.close()
