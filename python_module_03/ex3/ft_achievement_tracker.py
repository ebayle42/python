import random

ACHIEVEMENTS: set[str] = {'Crafting Genius', 'Strategist', 'World Savior', 
                           'Speed Runner', 'Survivor', 'Master Explorer', 
                           'Treasure Hunter', 'Unstoppable', 'First Steps', 
                           'Collector Supreme', 'Untouchable', 'Sharp Mind', 
                           'Boss Slayer'}

def gen_player_achievements() -> set[str]:
    random_number = random.randint(1, (len.ACHIVEMENTS))
    return set(random.sample(ACHIEVEMENTS, random_number))

