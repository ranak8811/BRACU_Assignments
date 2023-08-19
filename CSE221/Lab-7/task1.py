inp = open('input1.txt', 'r')
out = open('output1.txt', 'w')

n = int(inp.readline().strip())
l = [list(map(int, inp.readline().strip().split())) for _ in range(n)]
l.sort(key = lambda x : x[1])

res = []
end = 0
for i in l:
    if end <= i[0]:
        res.append(i)
        end = i[1]

final_output = f"{len(res)}\n"
for x in res:
    s, e = x
    final_output += f"{s} {e}\n"
out.write(final_output)

inp.close()
out.close()