def ft_count_harvest_recursive(days=5, current=1):
    if current > days:
        print("Harvest time!")
        return
    print(f"Day {current}")
    ft_count_harvest_recursive(days, current + 1)
