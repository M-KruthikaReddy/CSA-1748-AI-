import numpy as np

def tsp(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if i != j:
                dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])

    tour = [0]
    unvisited_cities = set(range(1, n))
    total_distance = 0

    while unvisited_cities:
        current_city = tour[-1]
        nearest_city = min(
            unvisited_cities,
            key=lambda city: dist_matrix[current_city][city]
        )
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        total_distance += dist_matrix[current_city][nearest_city]

    # Return to starting city
    tour.append(0)
    total_distance += dist_matrix[tour[-2]][0]

    return tour, total_distance
