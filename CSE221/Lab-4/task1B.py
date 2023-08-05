# Sub task - B

inp = open('input1b_2.txt', 'r')
out = open('output1b_2.txt', 'w')

v, e = map(int, inp.readline().strip().split())

a = []
for i in range(e):
    row = list(map(int, inp.readline().strip().split()))
    a.append(row)

f = ''
for k in range(v+1):
    m = f"{k} : "
    for j in range(e):
        if (k == a[j][0]):
            t = f" ({a[j][1]},{a[j][2]})"
            m += str(t)
    f += m+ '\n'

out.write(f)

inp.close()
out.close()



#----------------------------------------------------------------
'''
                Brainstorming Part:
    a.
    For undirected graphs in Adjacency matrix I have to write '1' for both vertices 
    which are connected with each other.

    b.
    For parallel edges we can't represent the graph using Adjacency Matrix.
'''