class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        if height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{name}: Error, age can't be negative")
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def set_age(self, update_age: int) -> None:
        if update_age < 0:
            print(f"{self.get_name()}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = update_age

    def set_height(self, update_height: float) -> None:
        if update_height < 0:
            print(f"{self.get_name()}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = update_height

    def show(self) -> None:
        print(f"{self.get_name()}: {self.get_height()}cm, "
              f"{self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_bloom = False

    def bloom(self) -> None:
        self._is_bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self._is_bloom:
            print(f" {self.get_name()} is blooming beautifully!")
        else:
            print(f" {self.get_name()} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self.get_name()} now produces a shade of "
              f"{self.get_height()}cm long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, age)
        self._nutritional_value = nutritional_value
        self._harvest_season = harvest_season

    def age(self, to_age: int) -> None:
        self.set_age(self.get_age() + to_age)
        self._nutritional_value += to_age

    def grow(self, to_grow: float) -> None:
        self.set_height(self.get_height() + to_grow)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


if __name__ == "__main__":
    f1 = Flower("Rose", 15.0, 10, "red")
    t1 = Tree("Oak", 200.0, 365, 5.0)
    v1 = Vegetable("Tomato", 5.0, 10, "April", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    f1.show()
    print("[asking the rose to bloom]")
    f1.bloom()
    f1.show()
    print()
    print("=== Tree")
    t1.show()
    print("[asking the oak to produce shade]")
    t1.produce_shade()
    print()
    print("=== Vegetable")
    v1.show()
    print("[make tomato grow and age for 20 days]")
    v1.grow(42.0)
    v1.age(20)
    v1.show()
