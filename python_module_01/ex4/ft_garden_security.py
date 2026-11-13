class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        if height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
        else:
            self._age = age

    def show(self) -> None:
        print(f"Plant created: {self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old\n")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, update_age: int) -> None:
        if update_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = update_age
        print(f"Age updated: {update_age} days")

    def set_height(self, update_height: float) -> None:
        if update_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = update_height
        print(f"Height updated: {update_height:.0f}cm")

    def status(self) -> None:
        print(f"Current state: {self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")


p1 = Plant("Rose", 15.0, 10)

print("=== Garden Security System ===")
p1.show()
p1.set_height(25.0)
p1.set_age(30)
print()
p1.set_height(-10)
p1.set_age(-25)
print()
p1.status()
