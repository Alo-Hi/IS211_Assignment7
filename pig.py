
import random

random.seed(0)


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points


class Die:
    def roll(self):
        return random.randint(1, 6)


class PigGame:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.die = Die()
        self.current_player = 0


    def play_turn(self):
        player = self.players[self.current_player]
        turn_total = 0

        while True:
            print(f"\n{player.name}'s turn")
            print(f"Turn total: {turn_total}")
            print(f"Total score: {player.score}")

            choice = input("Roll (r) or Hold (h)? ").lower()

            if choice == "r":
                roll = self.die.roll()
                print(f"You rolled a {roll}")

                if roll == 1:
                    turn_total = 0
                    print("You lost your turn points!")
                    print(f"Turn total: {turn_total}")
                    print(f"Total score: {player.score}")
                    break
                else:
                    turn_total += roll

            elif choice == "h":
                player.add_score(turn_total)
                print(f"{player.name} now has {player.score} points.")
                break

            else:
                print("Please enter r or h.")


    def play(self):
        while True:
            self.play_turn()

            player = self.players[self.current_player]

            if player.score >= 100:
                print(f"\n{player.name} wins with {player.score} points!")
                break

            self.current_player = (self.current_player + 1) % 2



if __name__ == "__main__":
    game = PigGame()
    game.play()



