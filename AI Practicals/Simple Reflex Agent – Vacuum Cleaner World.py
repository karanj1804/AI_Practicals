def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


location = input("Enter location (A/B): ")
status_A = input("Enter status of A (Clean/Dirty): ")
status_B = input("Enter status of B (Clean/Dirty): ")

print("\nInitial Environment:")
print("A:", status_A)
print("B:", status_B)

for i in range(5):
    if location == "A":
        action = vacuum_agent(location, status_A)
    else:
        action = vacuum_agent(location, status_B)

    print("\nAgent Location:", location)
    print("Action:", action)

    if action == "Suck":
        if location == "A":
            status_A = "Clean"
        else:
            status_B = "Clean"

    elif action == "Right":
        location = "B"

    elif action == "Left":
        location = "A"

    if status_A == "Clean" and status_B == "Clean":
        print("\nBoth rooms are clean!")
        break

print("\nFinal Environment:")
print("A:", status_A)
print("B:", status_B)