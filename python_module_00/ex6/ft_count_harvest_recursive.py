def ft_count_harvest_recursive(day):
    print("Day:", day)
    if (day < 5):
        return (ft_count_harvest_recursive(day + 1))
    print("Harvest time!")
