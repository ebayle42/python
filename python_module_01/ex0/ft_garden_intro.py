def presentation(name_par: str, height_par: int, age_par: int) -> None:
    name = name_par
    height = height_par
    age = age_par
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    presentation("Rose", 25, 30)
