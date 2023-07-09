inp = open('input2.txt', 'r')
out = open('output2.txt', 'w')

n = int(inp.readline().strip())
lst = list(map(int, inp.readline().strip().split()))

def get_max(a):
  n = len(a)

  if n == 1:
    return float('-inf')
  if n == 2:
    return a[0] + (a[1])**2

  mid = len(a)//2

  l = a[ : mid]
  r = a[mid : ]

  left_max = get_max(l)
  right_max = get_max(r)

  lm = max(l)
  m = abs(a[mid])
  for i in range(mid+1, len(a)):
    if m < abs(a[i]):
      m = abs(a[i])
  cross_max = lm + m**2

  return max(left_max, right_max, cross_max)

max_value = get_max(lst)

out.write(str(max_value))

inp.close()
out.close()