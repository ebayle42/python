class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        0.8
        
    def age(self) -> None:
        1
        
    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")