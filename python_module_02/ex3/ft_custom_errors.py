class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.message = message


def check_plant(plant: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"The {plant} plant is wilting!")


def check_water(tank_level: int, needed: int) -> None:
    if tank_level < needed:
        raise WaterError("Not enough water in the tank!")


def test_plant_error() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_water_error() -> None:
    print("Testing WaterError...")
    try:
        check_water(2, 10)
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_garden_errors() -> None:
    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        check_water(2, 10)
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_plant_error()
    print()
    test_water_error()
    print()
    test_garden_errors()
    print()
    print("All custom error types work correctly!")
