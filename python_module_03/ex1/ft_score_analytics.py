import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    i = 1
    score: list[int] = []
    while i < len(sys.argv):
        try:
            score += [int(sys.argv[i])]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        i += 1
    if not score:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        maximum = max(score)
        minimum = min(score)
        print(f"Scores processed: {score}")
        print(f"Total players: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score) / len(score)}")
        print(f"High score: {maximum}")
        print(f"Low score: {minimum}")
        print(f"Score range: {maximum - minimum}")
