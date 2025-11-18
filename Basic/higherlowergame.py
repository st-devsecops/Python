import random
from data import data1
from logo import art
   


def compare_follower():
    name1, name2 = random.sample(data1, 2)
    print("Lets do choice between two: ", name1['name'], name2['name'])
    i = 0
    choice = input("Select the name: ")
    if name1['follower_count'] > name2['follower_count']:
        winner = name1['name']
    else:
       winner = name2['name']

    if choice == winner:
        i +=1
        print("Correct Answer: ", winner)

    else:
         print("Wrong answer: ", winner)
    print("The score is: ", i)     
    return winner     

playgame = input("Do you want to play Higher-Lower game: ").lower()
print(art)

if playgame in ("yes" or "y"):
      while True:  
        compare_follower()
        playagain = input("Do you want to play again: ").lower()
        if playagain not in ("yes" or "y"):
             print("Thanks for playing!")
             break             
else:
    exit
