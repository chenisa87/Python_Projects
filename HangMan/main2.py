def random_word():
    import random
    words = ["hello","python","java","chocolate","potato"]
    chosen_word = random.choice(words)
    return chosen_word

def game():
    # init
    chosen_word = random_word()
    word_display = ["_" for _ in chosen_word]
    attemps = 8
    # game start
    print("Welcome to Hangman!")

    while attemps > 0 and '_' in word_display:

        print("\n"+" ".join(word_display))
        guess = input("Guess the letter: ").lower()
        if guess in chosen_word:
            if guess in word_display:
                print("You are already guess the answer.")
            else:
                for index , letter in enumerate(chosen_word):
                    if letter == guess:
                        word_display[index] = guess
        else:
            print("That letter doesn't appear in the word.")    
            attemps-=1

    if '_' not in word_display:
        print("You win the game!!")
        print("".join(word_display))
    else:
        print("You lose the game.")
        print(f"The answer is {chosen_word}.")

game()