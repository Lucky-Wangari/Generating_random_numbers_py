import random

number = input("Type a number:  ")

if number.isdigit():
    number = int(number)
    # this is to pass a condition it can only be an int
    
    if number <= 0:
        print("Type  number larger than 0")
        quit()
else:
    print("Type a number")
    quit()
    
random_number = random.randint(0, number)
guess = 0
# print(random_number)

while True:
    guess += 1
    player = input("Make a guess: ")
    #  the pragram allows the player to input a random guess.
    if player.isdigit():
        # checking if the player has input an int.
        player = int(player)
        # conditioning the player to input a digit.
    else:
        print("Please type a number")
        # if the while loop is not closed it continues as long as the condition is met.
        # therefore to control it we use the continue condition, to limit the while loop.
        continue
    
    if player == random_number:
        print("You're guess is Correct!")
        break
    # break is used to ensure once the condition is met the iteration stops.
    # below is the use of nested loops
    elif player > random_number:
         print("You were above the number!")
    else:
         print("You were below the number!")

print("You got", guess, "guesses")