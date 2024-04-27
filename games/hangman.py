import random
word_string  = '''mango apple grapes peach watermelon kiwi strawberry 
pine guava banana'''
words=word_string.split()
word = random.choice(words)
numberOfGuesses = len(word) +2

letters = ['_'] * len(word)



def checkLetter(guess,word):
    for i in range(len(word)):
        if(guess == word[i]):
            return True
    return False


def returnIndex(guess):
    for i in range(len(word)):
        if(guess == word[i]):
            return i


def GameLayout(word,numberOfGuesses):
    letters = []
    for i in range(len(word)):
        letters.append('_')
    print(letters)


def Guess(word):
    guess = input("Enter Guess: ")
    if(checkLetter(guess,word)):
        print("correct guess")
        index = returnIndex(guess)
        letters[index]=guess
        return True
    else:
        print("incorrect guess")
        print(f"{numberOfGuesses} remaining")
        return False

while numberOfGuesses != 0:
    if(not Guess(word)):
        numberOfGuesses-=1
    print(letters)
