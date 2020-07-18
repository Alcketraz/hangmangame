import random


def hangman():
    word = random.choice(["avengers", "light", "food", "television",
            "battery", "metal", "ironman", "naruto", "gintoki", "Bleach" ])

    validLetters = 'qwertyuioplkjhgfdsazxcvbnm'

    turns = 10
    guessmade = ''
    while len(word) > 0:
        mainWord = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                mainWord = mainWord + letter
            else:
                mainWord = mainWord + "_"+" "

        if mainWord == word:
             print(mainWord)
             print("You won!")
             break
        print("Guess the word:", mainWord)
        guess = input()

        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character")
            guess= input()

        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print("9 turns left")
                print(" -------------- ")
            elif turns == 8:
                print("8 turns left")
                print(" -------------- ")
                print("       O        ")
            elif turns == 7:
                print("7 turns left")
                print(" -------------- ")
                print("       O        ")
                print("       |        ")
            elif turns == 6:
                print("6 turns left")
                print(" -------------- ")
                print("       O        ")
                print("       |        ")
                print("      /         ")
            elif turns == 5:
                print("5 turns left")
                print(" -------------- ")
                print("       O        ")
                print("       |        ")
                print("      / \       ")
            elif turns == 4:
                print("4 turns left")
                print(" -------------- ")
                print("      \O        ")
                print("       |        ")
                print("      / \       ")
            elif turns == 3:
                print("3 turns left")
                print(" -------------- ")
                print("      \O/       ")
                print("       |        ")
                print("      / \       ")
            elif turns == 2:
                print("2 turns left")
                print(" -------------- ")
                print("      \O/|      ")
                print("       |        ")
                print("      / \       ")
            elif turns == 1:
                print("1 turn left")
                print("last breaths counting, take care....")
                print(" -------------- ")
                print("      \O_|/     ")
                print("       |        ")
                print("      / \       ")
            elif turns == 0:
                print("You lose!")
                print("You let a kind man die!!")
                print(" -------------- ")
                print("       O_|      ")
                print("      /|\       ")
                print("      / \       ")
                break


print("Welcome!!!!")
name = input("Enter your name:")
print("Welcome to hangman-"+name)
print("-----------------------------------")
print("Try to guess the words in 10 tries")


hangman()