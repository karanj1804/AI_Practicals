def dfs(capacity1, capacity2, target):

    stack = [(0, 0, [])]
    visited = set()

    while stack:

        x, y, path = stack.pop()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        path = path + [(x, y)]

        if x == target or y == target:
            return path

        states = [
            (capacity1, y),
            (x, capacity2),
            (0, y),
            (x, 0),
            (x - min(x, capacity2 - y),
             y + min(x, capacity2 - y)),
            (x + min(y, capacity1 - x),
             y - min(y, capacity1 - x))
        ]

        for state in states:
            if state not in visited:
                stack.append((state[0], state[1], path))

    return None


capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

solution = dfs(capacity1, capacity2, target)

if solution:
    print("\nSolution Steps:")

    for step in solution:
        print(step)

else:
    print("No Solution Found")