def alphabeta(depth, node, maximizing, values,
              alpha, beta, max_depth):

    if depth == max_depth:
        return values[node]

    if maximizing:
        best = float('-inf')

        for i in range(2):
            value = alphabeta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            value = alphabeta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

depth = 3

result = alphabeta(
    0, 0, True, values,
    float('-inf'),
    float('inf'),
    depth
)

print("Leaf Node Values:", values)
print("Optimal Value:", result)