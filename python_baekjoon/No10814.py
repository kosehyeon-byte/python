n = int(input("Enter a number: "))

points = [list(input("Enter information (age name): ").split()) for _ in range(n)]
points.sort(key=lambda point: int(point[0]))

for point in points:
    print(point[0], point[1])