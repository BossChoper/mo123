import pandas as panda
import random
def roll_dice():
    """Simulates rolling three dice."""
    return random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
 def calculate_points(rolls):
    """Calculates the points for a given roll."""
    if len(set(rolls)) == 1:  # If all dice show the same face
        return 0, "tuples out"  # No points for tuples out
    elif len(set(rolls)) == 2:  # If two dice show the same face
        return sum(rolls), "fixed"  # Points equal to the sum of all faces
    else:
        return sum(rolls), "regular"  # Points equal to the sum of all faces
 def main():
    players = ["Player 1", "Player 2"]  # List of player names
    results = {player: 0 for player in players}  # Dictionary to store each player's points

    num_turns = 5  # Number of turns per player

    for player in players:
        print(f"\n{player}'s Turn:")
        for _ in range(num_turns):
            input("Press Enter to roll the dice...")
            rolls = roll_dice()
            points, roll_type = calculate_points(rolls)
            results[player] += points
            print(f"You rolled: {rolls} ({roll_type})")
            print(f"Points for this turn: {points}")
            print(f"Total points for {player}: {results[player]}")

    print("\nGame Over!")
    print("Final Scores:")
  #added a print out for panda's implementation, prints results in a dataframe
data_frame1 = panda.DataFrame(results, index=[0])
print(data_frame1)
    for player, points in results.items():
        print(f"{player}: {points}")
