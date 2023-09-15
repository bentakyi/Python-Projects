import random

class WordGame:
    def __init__(self):
        self.wordlist = []
        self.hashed_word = ""
        self.guessed_words = []
        self.number_of_guesses = 0
        self.random_word = ""

    def load_wordlist(self, filename):
        try:
            with open(filename, 'r') as file:
                self.wordlist = [word.strip() for word in file]
        except FileNotFoundError as e:
            print('Error Fetching Words:', str(e))

    def make_random_word(self):
        return random.choice(self.wordlist)

    def initialize_game(self):
        self.random_word = self.make_random_word()

        for letter in self.random_word:
            if letter in "aeiou":
                self.hashed_word += "#"
            else:
                self.hashed_word += letter

    def check_guess(self):
        if self.number_of_guesses >= 3:
            print("Game Over")
            return
        else:
            self.number_of_guesses += 1
            user_guess = input("Type your guess:")
            if user_guess == self.random_word:
                print("Your are correct")
            else:
                print("Wrong Answer, Try Again.", self.hashed_word)
                self.check_guess()

    def play_game(self):
        self.load_wordlist('wordlist.txt')
        self.initialize_game()
        print('Guess the word:', self.hashed_word)
        self.check_guess()

def main():
    word_game = WordGame()
    word_game.play_game()

if __name__ == "__main__":
    main()
