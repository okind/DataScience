#day 1
print("welcome to the band name generator")
city = input("Which city did you grow up in?\n")
pet=input("what is the name of a pet? \n")
print("You band name could be "+ city+" " +pet)
#day2
print("welcome to the tip calculator")
bill = input("What was the total bill?\n")
tip=input("What percentage tip would you like to give? 10,12 or 15? \n")
people_num=input("How many people to spllit the bill? \n")
single_payment=(int(tip)/100+1)*float(bill)/int(people_num)
final_payment = str(round(single_payment, 2))
print(f"Each person should pay:  {final_payment}")

#day3
#if height>30:
#   print())
#elif condition:
#else:
#   print()
print("Welcome to the game")
choice1 = input("You are at a crossroad, where do you want to go? Left or right?").lower()
if choice1 == "left":
    choice2 = input("You are at a crossroad, what do you want to do? Swim or wait").lower()
    if choice2 == "wait":
        choice3 = input("You are at a crossroad, which door do you want to open? Red, blue or yellow").lower()
        if choice3 == "yellow":
            print('You win!')
        else:
            print('Game over')
    else:
        print('Game over')
else:
    print('Game over')

import random
random_int = random.randint(0, 2) # random number between 0 and 2 including these numbers
print(random_int)
random_float=random.random() #number between 0 and 1, not including 1
print(random_float)
#day4
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
