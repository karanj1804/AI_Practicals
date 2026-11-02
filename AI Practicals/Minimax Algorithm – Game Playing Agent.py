def minimax(depth, node, maximizing, values, max_depth):

    if depth == max_depth:
        return values[node]

    if maximizing:

        best = float('-inf')

        for i in range(2):

            value = minimax(
                depth + 1,
                node * 2 + i,
                False,
                values,
                max_depth
            )

            best = max(best, value)

        return best

    else:

        best = float('inf')

        for i in range(2):

            value = minimax(
                depth + 1,
                node * 2 + i,
                True,
                values,
                max_depth
            )

            best = min(best, value)

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

depth = 3

result = minimax(
    0, 0, True, values, depth
)

print("Leaf Node Values:", values)
print("Optimal Value:", result)