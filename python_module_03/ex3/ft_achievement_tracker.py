import random

ACHIEVEMENTS: list[str] = ['Collector Supreme', 'Crafting Genius',
                           'First Steps', 'Master Explorer', 'Sharp Mind',
                           'Speed Runner', 'Survivor', 'Treasure Hunter',
                           'Unstoppable', 'Untouchable']


def gen_player_achievements() -> set[str]:
    random_number = random.randint(3, 7)
    return set(random.sample(ACHIEVEMENTS, random_number))


if __name__ == "__main__":
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    all_achievement = alice.union(bob, charlie, dylan)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achievements: {all_achievement}\n")
    print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}\n")
    print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
    print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}\n")
    print(f"Alice is missing: {all_achievement.difference(alice)}")
    print(f"Bob is missing: {all_achievement.difference(bob)}")
    print(f"Charlie is missing: {all_achievement.difference(charlie)}")
    print(f"Dylan is missing: {all_achievement.difference(dylan)}")
