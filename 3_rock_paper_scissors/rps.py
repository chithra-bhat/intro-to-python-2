#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']


class Player:
    """The Player class is the parent class for all Players in this game."""

    def __init__(self):
        self.name = "Parent"

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Rock Player"

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            user_input = input("Choose rock, paper or scissors: ")
            user_input = user_input.strip().lower()
            if user_input in moves:
                return user_input
            else:
                print(
                    f"Move '{user_input}' not in rock, paper, or scissors."
                    " Please try again."
                )


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Reflect Player"
        self.opponent_last_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.opponent_last_move = their_move

    def move(self):
        return self.opponent_last_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Cycle Player"
        self.your_last_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.your_last_move = my_move

    def move(self):
        idx = moves.index(self.your_last_move)
        return moves[(idx + 1) % len(moves)]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_count = 0
        self.p2_count = 0

    def get_rounds_count(self):
        while True:
            try:
                n = int(input("How many rounds do you want to play? "
                        "(Enter a number 1-5): "))
                if 1 <= n <= 5:
                    return n
                else:
                    print("Please enter a valid number between 1 and 5.")
            except ValueError:
                print("Enter a number (1-5).")

    def beats(self, one, two):
        if one == two:
            return 'draw'
        elif (one == 'rock' and two == 'scissors') or \
             (one == 'scissors' and two == 'paper') or \
             (one == 'paper' and two == 'rock'):
            return 'win'
        else:
            return 'lose'

    def display_round_score(self, round):
        print(
            f"Score after Round {round}:"
            f"\nHuman: {self.p1_count}"
            f"  {self.p2.name}: {self.p2_count}\n"
        )

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You chose: {move1}  {self.p2.name} chose: {move2}")
        result = self.beats(move1, move2)
        if result == 'draw':
            print("Same selection, scores unchanged.")
        elif result == 'win':
            self.p1_count += 1
        else:
            self.p2_count += 1
        self.display_round_score(round)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def print_result(self):
        cyan = "\033[1;36m"
        purple = "\033[1;35m"
        reset = "\033[0m"

        print(
            f"{cyan}Final Score: \nHuman: {self.p1_count} "
            f"{self.p2.name}: {self.p2_count}{reset}"
        )

        if self.p1_count > self.p2_count:
            print(f"{purple}\nYou win!\n {reset}")
        elif self.p2_count > self.p1_count:
            print(f"{purple}\n{self.p2.name} wins!\n {reset}")
        else:
            print(f"{purple}\nTie\n{reset}")

    def play_game(self):
        red = "\033[1;31m"
        green = "\033[1;32m"
        reset = "\033[0m"

        n = self.get_rounds_count()
        print(f"{green}\nGame start!\n{reset}")
        for round in range(1, n + 1):
            print(f"Round {round}:")
            self.play_round(round)
        self.print_result()
        print(f"{red}Game over!\n{reset}")


if __name__ == '__main__':
    while True:
        print("\nWho do you want to play with?\n")
        print(
            "1. Rock Player\n"
            "2. Computer\n"
            "3. Reflect Player\n"
            "4. Cycle Player\n"
        )

        while True:
            try:
                user_choice = int(input("Pick a number (1-4):"))
                if 1 <= user_choice <= 4:
                    if user_choice == 1:
                        opponent = RockPlayer()
                        break
                    elif user_choice == 2:
                        opponent = RandomPlayer()
                        break
                    elif user_choice == 3:
                        opponent = ReflectPlayer()
                        break
                    else:
                        opponent = CyclePlayer()
                        break
                else:
                    print("\nInvalid input. Enter a number (1-4).\n")
            except ValueError:
                print("\nInvalid input. Enter a number (1-4).\n")

        game = Game(HumanPlayer(), opponent)
        game.play_game()

        play_again = input("Do you want to play again?(type 'quit' to stop): ")
        play_again = play_again.strip().lower()
        if play_again == 'quit':
            print("\nThank you for playing!\n")
            break
