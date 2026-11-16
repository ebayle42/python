import math

def get_player_pos() -> None:
    print("Get a first set of coordinates")
    yes = True
    while yes:
        try:
            x1, y1, z1 = map(float, input("Enter new coordinates as floats "
                        "in format 'x,y,z': ").split(','))
            yes = False
        except ValueError:
            print("Invalid syntax")
    x2 = 0.0
    y2 = 0.0
    z2 = 0.0
    print(f"Got a first tuple: {x1, y1, z1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_between = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance to center: {round(distance_between, 4)}\n")

    print("Get a second set of coordinates")
    yes = True
    while yes:
        try:
            x2, y2, z2 = map(float, input("Enter new coordinates as floats "
                        "in format 'x,y,z': ").split(','))
            yes = False
        except ValueError:
            print("Invalid syntax")
    distance_between = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance_between, 4)}")

if __name__ == "__main__":
    get_player_pos()
