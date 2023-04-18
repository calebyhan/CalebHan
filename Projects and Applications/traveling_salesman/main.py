import math
import matplotlib.pyplot as plt

input_points = [[1, 2], [3, 4], [-1, 5], [7, -1], [-5, 2], [-1, -5]]


def edge(points):
    edge_point = [0, 0]
    for point in points:
        edge_point = point if math.dist([0, 0], edge_point) < math.dist([0, 0], point) else edge_point
    return edge_point


def solve(edge_point, points):
    order = [edge_point]
    points.remove(edge_point)
    while len(points) > 0:
        closest = points[0]
        for point in points:
            closest = point if math.dist(point, order[-1]) < math.dist(point, closest) else closest
        order.append(closest)
        print(closest)
        points.remove(closest)
    return order


def distance(points):
    dist = 0
    for i, point in enumerate(points):
        if i == 0:
            continue
        dist += math.dist(points[i - 1], points[i])
    return dist


ordered_points = solve(edge(input_points), input_points)

x = [n[0] for n in ordered_points]
y = [n[1] for n in ordered_points]

plt.plot(x, y)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.title("Simple Traveling Salesman Solution")

plt.show()

print(ordered_points)
print(distance(ordered_points))
