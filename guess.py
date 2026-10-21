import random

secret_number=34

attempts_left = 3

print("Guess the secret number between 1 and 50!")

while(attempts_left != 0 ):

  guess= int(input("enter a number between 1 to 50\n"))

  attempts_left=attempts_left-1

  if secret_number == guess:

    print("YOU WON")

    break

  else:

    diff=secret_number-guess

    if abs(diff)<10:

      print("Hot")

    else:

      print("Cold")

  if attempts_left<=0:

    print("YOU LOST")import random

secret_number=34

attempts_left = 3

print("Guess the secret number between 1 and 50!")

while(attempts_left != 0 ):

  guess= int(input("enter a number between 1 to 50\n"))

  attempts_left=attempts_left-1

  if secret_number == guess:

    print("YOU WON")

    break

  else:

    diff=secret_number-guess

    if abs(diff)<10:

      print("Hot")

    else:

      print("Cold")

  if attempts_left<=0:

    print("YOU LOST")import random

secret_number=34

attempts_left = 3

print("Guess the secret number between 1 and 50!")

while(attempts_left != 0 ):

  guess= int(input("enter a number between 1 to 50\n"))

  attempts_left=attempts_left-1

  if secret_number == guess:

    print("YOU WON")

    break

  else:

    diff=secret_number-guess

    if abs(diff)<10:

      print("Hot")

    else:

      print("Cold")

  if attempts_left<=0:

    print("YOU LOST")