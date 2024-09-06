import random

def alpha_beta(depth, index, is_max, results, alpha, beta):
    if depth == 3:
        return results[index]

    if is_max:
        max_value = float('-inf')
        for i in range(0, 2):
            val = alpha_beta(depth + 1, index * 2 + i, False, results, alpha, beta)
            max_value = max(max_value, val)
            alpha = max(alpha, max_value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = float('inf')
        for i in range(0, 2):
            val = alpha_beta(depth + 1, index * 2 + i, True, results, alpha, beta)
            min_value = min(min_value, val)
            beta = min(beta, min_value)
            if beta <= alpha:
                break
        return min_value

def battle(player):
    results = [random.choice([-1, 1]) for _ in range(8)]
    rounds = 0
    scorpion_win = 0
    sub_zero_win = 0
    round_results = ""

    current = player

    for round_number in range(3):
        rounds += 1
        if current == 0:
            winner = alpha_beta(0, 0, True, results, float('-inf'), float('inf'))
        else:
            winner = alpha_beta(0, 0, False, results, float('-inf'), float('inf'))

        if winner == -1:
            scorpion_win += 1
            round_winner = f"Winner of Round {rounds}: Scorpion"
        else:
            sub_zero_win += 1
            round_winner = f"Winner of Round {rounds}: Sub-Zero"

        round_results += round_winner + '\n'
        current = 1 - current

    if scorpion_win > sub_zero_win:
        final_winner = "Game Winner: Scorpion"
    else:
        final_winner = "Game Winner: Sub-Zero"

    output = f"{final_winner}\nTotal Rounds Played: {rounds}\n" + round_results

    with open('output.txt', 'w') as file:
        file.write(output)

with open('input.txt', 'r') as file:
    starting_player = int(file.read().strip())

battle(starting_player)
