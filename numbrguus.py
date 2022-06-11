n = 55
number_of_guesses = 1
print("number of guesses is limited to only 9 time: ")
while (number_of_guesses<=9):
    guess_number = int(input("guess the number: \n"))
    if guess_number<55:
        print("you enter less number plese input greater number.\n")
    elif guess_number>55:
        print("you enter greater number plese enter smaller number.\n")
    else:
        print("you win\n")
        print((number_of_guesses,"no of guesses he took to finish"))
        break
    print((5-number_of_guesses,"no of guesses left"))
    number_of_guesses = number_of_guesses + 1
if(number_of_guesses>5):
    print("game over")