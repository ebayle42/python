import random

ACHIEVEMENTS: list[str] = ['Crafting Genius', 'Strategist', 'World Savior',
                           'Speed Runner', 'Survivor', 'Master Explorer',
                           'Treasure Hunter', 'Unstoppable', 'First Steps',
                           'Collector Supreme', 'Untouchable', 'Sharp Mind',
                           'Boss Slayer']


def gen_player_achievements() -> set[str]:
    random_number = random.randint(3, 7)
    return set(random.sample(ACHIEVEMENTS, random_number))

if __name__ == "__main__":
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
