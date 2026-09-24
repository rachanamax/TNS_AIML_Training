import random

secret = random.randint(1,20)
count=0
max_count=5


while count<max_count:
    count+=1
    number = int(input("Guess the number : "))
    if number == secret:
        print("You have guessed correctly")
        break

    elif (number>secret):
        print("Too High")
        continue
        

    else:
        print("Too Low ")
        continue
       

if count==5:
        print("No more attempts  ")