inp = open('input3.txt', 'r')
out = open('output3.txt', 'w')

n, x = map(int, inp.readline().strip().split())

coin_denominations = list(map(int, inp.readline().strip().split()))

min_coins = [float('inf')] * (x + 1)
min_coins[0] = 0

for coin in coin_denominations:
    for amount in range(coin, x + 1):
        if min_coins[amount - coin] + 1 < min_coins[amount]:
            min_coins[amount] = min_coins[amount - coin] + 1
            # print(min_coins)

if min_coins[x] == float('inf'):
    out.write("-1")
else:
    out.write(str(min_coins[x]))

inp.close()
out.close()
