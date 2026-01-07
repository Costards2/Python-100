import random as rd
from hangman_words import word_list

list_size = len(word_list) 
choosen_word = word_list[rd.randint(0, list_size - 1)]

print("Welcome to hangman!!\n")

blank_word = ''
# for letter in choosen_word:
#     blank_word += '_' 
blank_word = ["_"] * len(choosen_word)

print("The word is:\n")
for letra in blank_word:
    print(letra, end=" ")
print()

can_guess = True
lives = 6
guessed_letters = []

while can_guess:
    choosen_letter = input("\nGuess a letter\n").lower()

    while choosen_letter in guessed_letters:
        print("Youve already guessed this lettes dummy!\n")
        choosen_letter = input("Choose another letter\na")


    count = 0
    #letter_in_word = False;
    for letter in choosen_word:
        if (letter == choosen_letter):
            #letter_in_word = True
            blank_word[count] = choosen_letter
            if choosen_letter not in guessed_letters:
                guessed_letters.append(choosen_letter)

        count += 1

    print()
    for letter in blank_word:
        print(letter, end=" ")
    print()

    if choosen_letter not in choosen_word:
        lives -= 1
        print(f"\nGuessed wrong \"{choosen_letter}\" is not in the word, so you lose a life! Total lives = {lives}")
        if lives == 0:
            can_guess = False
            print("\nLOST THE GAME")

    if "_" not in blank_word:
        can_guess = False
        print("\nGAME WON")

    #THE FIRST ATTEMP I DID, IT WORKS BUT I IMPROVED IT 
    # if letter_in_word == False:
    #     lives -= 1
    #     print(f"\nGuessed Wrong and los a life! Total lives = {lives}")
    #     if lives == 0:
    #         can_guess = False
    #         print("\nLOST THE GAME")

    # yet_to_guess = 0;
    # for letter in blank_word:
    #     if letter == '_':
    #         yet_to_guess += 1
    
    # if yet_to_guess == 0:
    #     print("\nGAME WON")
    #     can_guess = False


    