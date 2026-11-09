class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = round(height, 2)
        self._age = age

    def show(self) -> None:
        print(f"Created: {self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")

    def set_height(self, height_up: float) -> None:
        if height_up < 0:
            print("Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = round(float(height_up), 2)
        print(f"Height updated: {height_up}cm")

    def set_age(self, age_up: int) -> None:
        if age_up < 0:
            print("Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age_up
        print(f"Age updated: {age_up} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def state(self) -> None:
        print(f"Current state: {self._name}:, {self.get_height()}cm, "
              f"{self.get_age()} days old")


p1 = Plant("Rose", 15.0, 10)

print("=== Garden Security System ===")
p1.show()
print()
p1.set_height(25)
p1.set_age(30)
print()
p1.set_height(-100)
p1.set_age(-15)
print()
p1.state()
