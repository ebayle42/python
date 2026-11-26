import random

PLAYERS: list[str] = ['Enzo', 'Vincent', 'Melvin', 'tristan', 'Pablo', 'simon']

SCORE: dict[str, int] = {}

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS}")

    players_cap: list[str] = [name.capitalize() for name in PLAYERS]
    print(f"New list with all the name capitalized: {players_cap}")

    players_only_cap: list[str] = [
        name for name in PLAYERS if name[0].isupper()
    ]
    print(f"New list of capitalized names only: {players_only_cap}")
    scores: dict[str, int] = {
        name: random.randint(0, 1000) for name in players_cap
    }
    print(f"Score dict: {scores}")

    average: float = sum(scores.values()) / len(scores)
    print(f"Score average is {average:.2f}")

    high_scores: dict[str, int] = {
        name: score for name, score in scores.items() if score > average
    }
    print(f"High scores: {high_scores}")