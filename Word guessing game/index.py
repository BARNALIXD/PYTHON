import random
name = input("What is your name?")
print("Good luck !", name)

words = ['rainbow', 'computer', 'science', 'programming', 'pythons', 'mathematics', 'player', 'players', 
         'conditions', 'reverses', 'waters', 'board',]

word = random.choice(words)

print("Guess the characters")
guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print('_')
            failed += 1

            if failed == 0:
                print("You win")

                print("the word is :",word )
                break

            print()
            guess = input("guess a character:")

            guesses += guess

            if guess not in word:
                turns -= 1

                print("Wrong")
                print("You have", turns, "more attempts")

                if turns == 0:
                    print("You lose")

