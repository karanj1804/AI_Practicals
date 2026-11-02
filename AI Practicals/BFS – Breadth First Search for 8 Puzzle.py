from collections import deque

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc

            new_state = list(state)
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def bfs(start):

    queue = deque([(start, [start])])
    visited = {start}

    while queue:

        state, path = queue.popleft()

        if state == goal:
            return path

        for neighbor in get_neighbors(state):

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))

solution = bfs(start)

if solution:
    print("\nSolution Found:")

    for state in solution:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()

    print("Total Moves:", len(solution) - 1)

else:
    print("No Solution Found")