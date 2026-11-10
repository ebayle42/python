class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 0.8

    def to_age(self) -> None:
        self.age += 1

    def show(self) -> None:
        for i in range(8):
            if i > 1:
                print("=== Day", i, "===")
            print(f"{self.name}: {round(self.height, 2)}cm,"
                  f"{self.age} days old")
            if i < 1:
                print("=== Day 1 ===")
            self.grow()
            self.to_age()
            if i >= 7:
                print(f"Growth this week: {round(0.8*7, 1)}cm")


p1 = Plant("Rose", 25, 30)

print("=== Gardern Plant Growth ===")
p1.show()
