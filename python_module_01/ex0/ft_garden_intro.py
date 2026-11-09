def presentation(plant_type: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {plant_type}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of program ===")


if __name__ == "__main__":
    presentation("Rose", 25, 30)
