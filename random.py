import random
rand = random.randint(1, 10)
guess = int(input("Enter a number :"))

if(rand>guess):
        print("guess a lesser number")
else:
        print("guess a biger number")

#x = int(x)
        #print("guess a number between 1 to 10")
#type(rand)
#if  (guess>rand):
#        print("number is too high")
#if  (guess<rand):
#       print("number is too low")
#if  (guess==rand):
#        print("Congrautes you won!!!!")