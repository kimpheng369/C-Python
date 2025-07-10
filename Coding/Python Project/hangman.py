import random
import time

def hangman():
    print("welcome to hangman!")

    ready = input("Are you ready to play the game ? [yes/no]: ").strip().lower().lower()
    if ready != "yes":
        print("Okay, might be you can't beat this game LOL xD")
        return

    word_list = ["community", "computer", "elephant", "chocolate", "sunshine", "butterfly",
                 "watermelon", "christmas", "kangaroo", "mountain", "celebrate", "telescope",
                 "ronaldo", "football", "umbrella", "halloween", "adventure"]

    win_champ = r"""
                         ___________
                        '._==_==_=_.' 
                        .-\:      /-. 
                       | (|:.     |) | 
                        '-|:.     |-' 
                          \::.    /  
                           '::. .'   
                             ) (     
                           _.' '._  
    """

    end_game = r"""
    
╔╗──╔═══╦╗───╔╗──╔═══╦═══╦═══╗
║║──║╔═╗║║───║║──║╔═╗║╔═╗║╔══╝
║║──║║─║║║───║║──║║─║║╚══╣╚══╗
║║─╔╣║─║║║─╔╗║║─╔╣║─║╠══╗║╔══╝
║╚═╝║╚═╝║╚═╝║║╚═╝║╚═╝║╚═╝║╚══╗
╚═══╩═══╩═══╝╚═══╩═══╩═══╩═══╝
    """

    stages = [r"""
         +---+
         |   |
             |
             |
             |
             |
        =========""", r"""
         +---+
         |   |
         O   |
             |
             |
             |
        =========""", r"""
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========""", r"""
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========""", r"""
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========""", r"""
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========""", r"""
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        ========="""]

    play_again = True

    while play_again:
        seleceted_word = random.choice(word_list)
        guessed_word = ['_'] * len(seleceted_word)
        chances_left = 6
        while chances_left > 0:
            print(f"Word: {' '.join(guessed_word)}")
            print(stages[6 - chances_left])

            if ''.join(guessed_word) == seleceted_word:
                print(f"Congratulations! You guessed the word: {seleceted_word}")
                print(win_champ)
                break

            guess = input("Guess a character: ").strip().lower()

            if guess in seleceted_word:
                for i, letter in enumerate(seleceted_word):
                    if letter == guess:
                        guessed_word[i] = guess
                print("👍")
            else:
                chances_left -= 1
                print(f"Incorrect guess! Chances left: {chances_left}")
                print("👎")
        if chances_left == 0:
            print(f"Sorry, you lost! The word was: {seleceted_word}")
            print("Thank you, good luck next time!")
            print(end_game)
            print(stages[6])

        play_again_str = input("Do you want to play again? [yes/no]: ").strip().lower()
        if play_again_str != "yes":
            play_again = False
            print("Thank you, Good luck next time!")

if __name__ == "__main__":
    hangman()