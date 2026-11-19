import math


def get_player_pos() -> tuple[float, ...]:
    while True:
        parts = input("Enter new coordinates as floats "
                      "in format 'x,y,z': ").split(',')
        count = 0
        for p in parts:
            count += 1
        if count != 3:
            print("Invalid syntax")
            continue
        try:
            coords: tuple[float, ...] = ()
            for p in parts:
                coords = coords + (float(p),)
            return coords
        except ValueError as error:
            print(f"Error on parameter '{p.strip()}': {error}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: {x1, y1, z1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist, 4)}\n")

    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")
