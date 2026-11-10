class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = round(height, 2)
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._blooming = False

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self._blooming = True

    def is_blooming(self) -> bool:
        return self._blooming

    def get_color(self) -> str:
        return self._color

    def state(self) -> None:
        print(f" Color: {self.get_color()}")
        if self.is_blooming():
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def get_diameter(self) -> float:
        return self._trunk_diameter

    def state(self) -> None:
        print(f" Trunk diameter: {self.get_diameter()}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print(f"Tree Oak now produces a shade of {self.get_height()}cm"
              f" long and {self.get_diameter()}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutrition = 0

    def get_season(self) -> str:
        return self._harvest_season

    def get_nutrition(self) -> int:
        return self._nutrition

    def grow(self) -> None:
        print("[make tomato grow and age for 20 days]")
        self._height += 42
        self._age += 20
        self._nutrition += 20

    def state(self) -> None:
        print(f"{self._name}: {self.get_height()}cm, "
              f"{self.get_age()} days old")
        print(f" Harvest season: {self.get_season()}")
        print(f"Nutritional value: {self.get_nutrition()}")


f1 = Flower("Rose", 15.0, 10, "red")
t1 = Tree("Oak", 200.0, 365, 5.0)
v1 = Vegetable("Tomato", 5.0, 10, "April")
print("=== Garden Plant Types ===")
print("=== Flower")
f1.show()
f1.state()
f1.bloom()
f1.show()
f1.state()
print()
print("=== Tree")
t1.show()
t1.state()
t1.produce_shade()
print()
print("=== Vegetable")
v1.state()
v1.grow()
v1.state()
