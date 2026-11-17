import math


def ask_coords() -> tuple:
    while True:
        try:
            parts = input("Enter new coordinates as floats "
                          "in format 'x,y,z': ").split(',')
            if len(parts) != 3:
                raise ValueError
            return (float(parts[0]), float(parts[1]), float(parts[2]))
        except ValueError:
            print("Invalid syntax")


def get_player_pos() -> None:
    print("Get a first set of coordinates")
    x1, y1, z1 = ask_coords()
    print(f"Got a first tuple: {x1, y1, z1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist, 4)}\n")

    print("Get a second set of coordinates")
    x2, y2, z2 = ask_coords()
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    get_player_pos()