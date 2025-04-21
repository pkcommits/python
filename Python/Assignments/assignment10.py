import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Step 1: Take number of points
n = int(input("Enter the number of points: "))

# Step 2: Input each point one by one
points = []
for i in range(n):
    x, y = map(float, input(f"Enter point {i+1} (x y): ").split())
    points.append((x, y))

# Step 3: Calculate distances
distances = []
total_distance = 0.0

for i in range(n - 1):
    dist = euclidean_distance(points[i], points[i + 1])
    distances.append(dist)
    print(f"Distance between {points[i]} and {points[i+1]}: {dist:.2f}")
    total_distance += dist

# Step 4: Show total
print(f"Total Path Length: {total_distance:.2f}")
