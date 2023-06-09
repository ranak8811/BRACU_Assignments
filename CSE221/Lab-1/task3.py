f1 = open('input3.txt', 'r')
f2 = open('output3.txt', 'w')

num_of_std = int(f1.readline().strip())
ids = list(map(int, f1.readline().strip().split(' ')))
marks = list(map(int, f1.readline().strip().split(' ')))

def selectionSort(marks, ids):
    for i in range(num_of_std):
        max_id = i
        for j in range(i+1, num_of_std):
            if marks[j] == marks[max_id]:
                if ids[max_id] < ids[j]:
                    max_id = max_id 
                else:
                    max_id = j
            elif marks[max_id] < marks[j]:
                max_id = j
        marks[i], marks[max_id] = marks[max_id], marks[i]
        ids[i], ids[max_id] = ids[max_id], ids[i]
        f2.write(f"ids: {ids[i]} Mark: {marks[i]}\n")

selectionSort(marks, ids)

f1.close()
f2.close()