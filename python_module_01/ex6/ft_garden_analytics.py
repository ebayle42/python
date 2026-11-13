class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0
            self._shade = 0

        def add_grow(self) -> None:
            self._grow += 1

        def add_age(self) -> None:
            self._age += 1

        def add_show(self) -> None:
            self._show += 1

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

        def add_shade(self) -> None:
            self._shade += 1

        def display_tree(self) -> None:
            self.display()
            print(f" {self._shade} shade")

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
        self._stats = self._create_stats()

    def _create_stats(self) -> "Plant.Stats":
        return Plant.Stats()

    def display_stats(self) -> None:
        self._stats.display()

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
        self._stats.add_age()

    def set_height(self, update_height: float) -> None:
        if update_height < 0:
            print(f"{self.get_name()}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = update_height
        self._stats.add_grow()

    def grow(self, to_grow: float) -> None:
        self.set_height(self.get_height() + to_grow)

    def age(self, to_age: int) -> None:
        self.set_age(self.get_age() + to_age)

    def show(self) -> None:
        print(f"{self.get_name()}: {self.get_height()}cm, "
              f"{self.get_age()} days old")
        self._stats.add_show()

    @staticmethod
    def check_age(age_check: int) -> bool:
        return age_check > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)


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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def seeding(self, how_many_seeds: int) -> None:
        if self._is_bloom:
            self._seeds += how_many_seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def display_stats(self) -> None:
        self._stats.display_tree()

    def produce_shade(self) -> None:
        print(f"Tree {self.get_name()} now produces a shade of "
              f"{self.get_height()}cm long and {self._trunk_diameter}cm wide.")
        self._stats.add_shade()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutritional_value: float) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self, to_age: int) -> None:
        super().age(to_age)
        self._nutritional_value += to_age

    def grow(self, to_grow: float) -> None:
        self.set_height(self.get_height() + to_grow)

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stats()


if __name__ == "__main__":
    f1 = Flower("Rose", 15.0, 10, "red")
    t1 = Tree("Oak", 200.0, 365, 5.0)
    s1 = Seed("Sunflower", 80.0, 45, "yellow", 0)
    a1 = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}\n")
    print("=== Flower")
    f1.show()
    show_stats(f1)
    print("[asking the rose to grow and bloom]")
    f1.bloom()
    f1.grow(8.0)
    f1.show()
    show_stats(f1)
    print()
    print("=== Tree")
    t1.show()
    show_stats(t1)
    print("[asking the oak to produce shade]")
    t1.produce_shade()
    show_stats(t1)
    print()
    print("=== Seed")
    s1.show()
    print("[make sunflower grow, age and bloom]")
    s1.grow(30.0)
    s1.age(20)
    s1.bloom()
    s1.seeding(42)
    s1.show()
    show_stats(s1)
    print()
    print("=== Anonymous")
    a1.show()
    show_stats(a1)
