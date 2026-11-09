class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")

    def set_height(self, height_up: int) -> None:
        if height_up > 0:
            print("Error, height can't be negative")
            print("Height update rejected")
            return
        self.height = height_up

    def set_height(self, age_up: int) -> None:
        if age_up > 0:
            print("Error, age can't be negative")
            print("Age update rejected")
            return
        self.age = age_up

    def get_height(self) -> None:
        