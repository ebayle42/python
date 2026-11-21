import sys


def create_inventory() -> None:
    i = 1
    inventory: dict[str, int] = {}
    while i < len(sys.argv):
        add = sys.argv[i].split(":")
        if len(add) != 2:
            print(f"Error - invalid parameter '{sys.argv[i]}'")
        elif add[0] in inventory:
            print(f"Redundant item '{add[0]}' - discarding")
        else:
            try:
                item_name: str = add[0]
                quantity: int = int(add[1])
                inventory.update({item_name: quantity})
            except ValueError as error:
                print(f"Quantity error for '{add[0]}': {error}")
        i += 1
        o = 0
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory.keys())} items:"
          f" {sum(inventory.values())}")
    for items in inventory:
        item = list(inventory.values())
        print(f"Item {items} represents"
              f" {round(item[o]/sum(inventory.values())*100, 1)}%")
        o += 1
    most = None
    least = None
    for items in inventory:
        if most is None or inventory[items] > inventory[most]:
            most = items
        if least is None or inventory[items] < inventory[least]:
            least = items
    if most is not None and least is not None:
        print(f"Item most abundant: {most} with quantity {inventory[most]}")
        print(f"Item least abundant: {least} with quantity {inventory[least]}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    create_inventory()
