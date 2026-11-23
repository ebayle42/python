import random
from typing import Generator

PLAYERS: list[str] = ['melvin', 'yacine', 'tristan', 'enzo', 'vincent']

ACTION: list[str] = ['manger', 'boire', 'coder', 'smash', 'corriger']

def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield(random.choice(PLAYERS), random.choice(ACTION))

if __name__ == "__main__":
    gen_event()