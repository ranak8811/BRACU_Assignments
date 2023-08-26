inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n = int(inp.readline().strip())

memo = {}

def find(n):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    x = find(n - 1) + find(n - 2)
    memo[n] = x
    return x

result = find(n)
out.write(str(result))

inp.close()
out.close()