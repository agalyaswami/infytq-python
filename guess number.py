import random
def guess_number(number_in_mind):
    my_number=random.randint(1,11)
    guess=input("tr to guess the number")
    if guess>number_in_mind:
        print("Number is high")
    elif guess<number_in_mind:
        print("Number is low")
    else:
        print("You have got it right")
  guess_number(4)
    

