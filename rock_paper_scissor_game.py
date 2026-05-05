import random

class RockPaperScissors:

    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

        self.symbols = {
            "rock": "✊",
            "paper": "✋",
            "scissors": "✌️"
        }

    def play_round(self):
        user = input("\nEnter rock, paper, or scissors: ").lower().strip()
        computer = random.choice(self.choices)

        if user not in self.choices:
            print("❌ Invalid choice!")
            return

        print(f"\nYou selected      : {self.symbols[user]} {user}")
        print(f"Computer selected : {self.symbols[computer]} {computer}")

        if user == computer:
            print("🤝 It's a tie!")

        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("🎉 You win!")

        else:
            print("💻 Computer wins!")

    def start_game(self):
        print("🎮 Rock Paper Scissors Game 🎮")

        while True:
            self.play_round()

            play_again = input("\nPlay again? (y/n): ").lower().strip()

            if play_again != "y":
                print("🙏 Thanks for playing!")
                break


# Create object
game = RockPaperScissors()
game.start_game()
