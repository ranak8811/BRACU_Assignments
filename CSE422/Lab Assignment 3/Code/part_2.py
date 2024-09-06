def ghost_pacman(c):
    results = [3, 6, 2, 3, 7, 1, 2, 0]

    def evaluate(depth, index, pacman_turn, alpha, beta):
        if depth == 3:
            if index < len(results):
                return results[index]
            else:
                return float('-inf')

        if pacman_turn:
            max_value = float('-inf')
            for i in range(2):
                value = evaluate(depth + 1, index * 2 + i, False, alpha, beta)
                max_value = max(max_value, value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return max_value
        else:
            min_value = float('inf')
            for i in range(2):
                value = evaluate(depth + 1, index * 2 + i, True, alpha, beta)
                min_value = min(min_value, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return min_value

    best_value = evaluate(0, 0, True, float('-inf'), float('inf'))

    left_value = max(results[1], results[2]) - c
    right_value = max(results[3], results[4]) - c

    if left_value > best_value and left_value > right_value:
        result = f"The new minimax value is {left_value}. Pacman goes left and uses dark magic\n"
    elif right_value > best_value and right_value >= left_value:
        result = f"The new minimax value is {right_value}. Pacman goes right and uses dark magic\n"
    else:
        result = f"The minimax value is {best_value}. Pacman does not use dark magic\n"

    with open('output1.txt', 'w') as output_file:
        output_file.write(result)


with open('input1.txt', 'r') as input_file:
    value = int(input_file.read().strip())

ghost_pacman(value)
