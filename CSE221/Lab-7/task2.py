inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n, m = map(int, inp.readline().split())
l = [list(map(int, inp.readline().strip().split())) for _ in range(n)]
l.sort(key = lambda x : x[1])

completed_tasks = [0] * m
assigned_tasks = 0

for task in l:
    assigned = False
    for i in range(m):
        if not assigned and task[0] >= completed_tasks[i]:
            completed_tasks[i] = task[1]
            assigned = True
            assigned_tasks += 1
            break

out.write(str(assigned_tasks))

inp.close()
out.close()