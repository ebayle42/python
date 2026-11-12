def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def count_days(current: int) -> None:
        if days + 1 > current:
            print(f"Day {current}")
            count_days(current + 1)
        if days == current:
            print("Harvest time!")
            return
    count_days(1)
