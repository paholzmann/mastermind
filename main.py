import random


class MasterMind():
    def __init__(self, num_guesses):
        self.num_guesses = num_guesses
        self.count = 0
        self.sequence = self.create_number_sequence()

    def main(self):
        self.display_game()
        while self.count < self.num_guesses:
            bulls, cows = self.compare_guess()
            self.count += 1
            if bulls == 4:
                print(f"{bulls} bulls!")
                break
            print(f"{bulls} bulls, {cows} cows")
        print(f"The sequence was: {self.sequence}")

    def display_game(self):
        print("=== Mastermind ===")
        print("Guess the 4-digit secret number!")
        print("No duplicates, numbers 0-9")
        print(f"You have {self.num_guesses} guesses.")

    def create_number_sequence(self):
        sequence = ""
        while len(sequence) < 4:
            random_number = str(random.randint(0, 9))
            if random_number not in sequence:
                sequence += random_number
        return sequence

    def get_user_input(self):
        user_guess = str(input(f"Guess {self.count + 1}: "))
        return user_guess

    def compare_guess(self):
        bulls = 0
        cows = 0
        sequence_list = list(self.sequence)
        user_guess_list = list(self.get_user_input())
        for i in range(len(sequence_list)):
            if sequence_list[i] == user_guess_list[i]:
                bulls += 1
                sequence_list[i] = None
                user_guess_list[i] = None
        for i in range(len(sequence_list)):
            if user_guess_list[i] is not None and user_guess_list[i] in sequence_list:
                cows += 1
                index = sequence_list.index(user_guess_list[i])
                sequence_list[index] = None
        return bulls, cows


if __name__ == '__main__':
    game = MasterMind(10)
    game.main()
