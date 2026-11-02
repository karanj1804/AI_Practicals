class ModelBasedAgent:
    def __init__(self):
        self.visited = set()

    def move(self, grid, position, goal):
        x, y = position
        self.visited.add(position)

        if position == goal:
            return "Goal Reached"

        directions = [
            (-1, 0, "Up"),
            (1, 0, "Down"),
            (0, -1, "Left"),
            (0, 1, "Right")
        ]

        for dx, dy, action in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < len(grid) and
                0 <= ny < len(grid[0]) and
                grid[nx][ny] != 1 and
                (nx, ny) not in self.visited):

                return action

        return "No Path Found"


grid = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

agent = ModelBasedAgent()
position = start

while position != goal:
    action = agent.move(grid, position, goal)

    print("Current Position:", position)
    print("Action:", action)

    if action == "Goal Reached":
        break

    if action == "No Path Found":
        print("Unable to reach goal")
        break

    if action == "Up":
        position = (position[0] - 1, position[1])
    elif action == "Down":
        position = (position[0] + 1, position[1])
    elif action == "Left":
        position = (position[0], position[1] - 1)
    elif action == "Right":
        position = (position[0], position[1] + 1)

if position == goal:
    print("Goal Reached Successfully!")