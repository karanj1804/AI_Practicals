def goal_stack_planning():

    initial = ["A", "B", "C"]

    goal = ["C", "B", "A"]

    print("Initial State:", initial)
    print("Goal State:", goal)

    stack = []

    for block in goal:
        stack.append(("PLACE", block))

    print("\nGoal Stack:")

    while stack:

        action = stack.pop()

        print("Executing:", action)

    print("\nPlanning Completed!")
    print("Goal Configuration:", goal)


goal_stack_planning()