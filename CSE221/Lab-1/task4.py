f1 = open('input4.txt', 'r')
f2 = open('output4.txt', 'w')

N = int(f1.readline().strip())
trains = [f1.readline().strip() for i in range(N)]
print(trains)

for i in range(N):
    for j in range(N-i-1):
        fline = trains[j].split()
        sline = trains[j+1].split()

        if fline[0] > sline[0]:
            trains[j], trains[j+1] = trains[j+1], trains[j]
        elif fline[0] == sline[0] and fline[-1] < sline[-1]:
            trains[j], trains[j+1] = trains[j+1], trains[j]

for train in trains:
    f2.write(train + '\n')

f1.close()
f2.close()