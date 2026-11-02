import random


cities = {
    'A': (0, 0),
    'B': (2, 4),
    'C': (5, 2),
    'D': (6, 6),
    'E': (8, 3)
}


def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def calculate_cost(route):
    cost = 0

    for i in range(len(route)):
        cost += distance(
            route[i],
            route[(i + 1) % len(route)]
        )

    return cost


def beam_search(k=3, iterations=100):

    all_cities = list(cities.keys())

    beam = []

    for _ in range(k):
        route = all_cities[:]
        random.shuffle(route)
        beam.append(route)

    for _ in range(iterations):

        candidates = []

        for route in beam:
            for i in range(1, len(route)):
                for j in range(i + 1, len(route)):

                    new_route = route[:]
                    new_route[i], new_route[j] = (
                        new_route[j], new_route[i]
                    )

                    candidates.append(new_route)

        candidates.sort(key=calculate_cost)

        unique = []
        seen = set()

        for route in candidates:
            key = tuple(route)

            if key not in seen:
                seen.add(key)
                unique.append(route)

            if len(unique) == k:
                break

        if unique:
            beam = unique

    best_route = min(beam, key=calculate_cost)

    return best_route, calculate_cost(best_route)


route, cost = beam_search()

print("Best Route:", " -> ".join(route + [route[0]]))
print("Minimum Distance:", round(cost, 2))