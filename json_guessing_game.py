#Sherry Zhang
#9/27/21

#Hangman game 

import os, json, random
from urllib.request import urlopen
os.system('cls')

request = urlopen("https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json")
dictionary = request.read()
dictionary = json.loads(dictionary)

words = dictionary.keys()
print(type(words))
three_letter = []
four_letter = []
five_letter = []

for i in words:
    if '-' not in i:
        if len(i) == 3:
            three_letter.append(i)
        if len(i) == 4:
            four_letter.append(i)
        if len(i) == 5:
            five_letter.append(i)

char_list = []

#creates categories for player to choose from
def Menu():
    while 1:
        #Create a menu to play game within categories of words
        print("""
            Menu
        1. 3 letter words
        2. 4 letter words
        3. 5 letter words
        4. Exit
        """)

        selection = input("Which category would you like? ")

        if selection.isdigit() and int(selection) <= 4:
            return int(selection)
        else:
            print("Please enter a number between 1 and 4")

#Uses selection from menu to select word from proper list
def selectWord(selection):
    if selection == 1:
        word = random.choice(three_letter)
    elif selection == 2:
        word = random.choice(four_letter)
    elif selection == 3:
        word = random.choice(five_letter)

    return word

name = input("What is your name: ")

playing_count = 0
high_score = []

choice = Menu() #choose which category from menu

while choice < 4 and playing_count < 3:
    if choice != 4:
        random_word = selectWord(choice)
        score = 0
        playing_count += 1

        #create character lists with _ to display guesses
        char_list = ["_ "] * len(random_word)
        
        chances = len(random_word) + 3
        print(f"You have {chances} chances\n")

        str_char = "".join(char_list)

        print(str_char)

        #while the player hasn't won or still has chances, continue, use break
        while 1:
            guess = input("Guess a letter of the word, type stop to end: ")
            guess = guess.lower()
            print()

            if guess == "stop":
                break

            #make sure input is exactly one letter
            elif guess.isalpha() and len(guess) == 1:
                #check if guess is in random word
                if guess in random_word and guess not in char_list:
                    for i in range(len(random_word)):
                        if random_word[i] == guess:
                            char_list[i] = guess
                            str_char = "".join(char_list)
                            score += 3
                
                    #check if the player has won
                    if str_char == random_word:
                        print("You won!")
                        score += 5*chances
                        break
                
                #Subtract chance for repeat guesses
                else:
                    print("You already guessed that letter!")
                    chances -= 1

            #if input is not one letter 
            else:
                print("Please guess a letter")
                chances -= 1

            #break if there are no chances left
            if chances == 0:
                print("You ran out of guesses")
                break

            print("Chances left", chances)
            print(f"{str_char}\n")
        
        high_score.append(score)
        
        print("\nthe word was", random_word)
        print("your score was", score)
        char_list = []
    