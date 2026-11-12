def ft_count_harvest_iterative() -> None:
    max = int(input("Days until harvest: "))
    day = range(1, max + 1)
    for i in day:
        print("Day", i)
    print("Harvest time!")
