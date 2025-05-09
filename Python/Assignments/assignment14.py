#Modernise the hackerrank code

class CoordinateGenerator:
    def __init__(self, x, y, z, n):
        self.x = x
        self.y = y
        self.z = z
        self.n = n

    def generate_coordinates(self):
        return [
            [i, j, k]
            for i in range(self.x + 1)
            for j in range(self.y + 1)
            for k in range(self.z + 1)
            if i + j + k != self.n
        ]

    @staticmethod
    def get_user_input():
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        z = int(input("Enter z: "))
        n = int(input("Enter n: "))
        return x, y, z, n

def main():
    x, y, z, n = CoordinateGenerator.get_user_input()
    generator = CoordinateGenerator(x, y, z, n)
    result = generator.generate_coordinates()
    print(result)

if __name__ == "__main__":
    main()
