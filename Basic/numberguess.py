# Number Guessing game:
# generate a random no in the range of 1-100 and guess the no in 3 attemps.
# Logic:
# 1. Generate a random no in the range of 1-100
# 2. Take the User input
# 3. compare the both values
# 4. if the given value is less than/more than 3 nos of the generated value, then given no is very close
# 5. if the given valus is is less than /more than 10 nos of the generated value, given no is near by
# 6. if the both matches user wins
# 7. maxium input is allowed is 3 times

#############################################################
import random
print("######Lets play the Number guessing game######")
print("The number should be in between 1-100")

no = random.randint(1,100)


for i in range(0,5):
    userno = int(input("Guess the Number: "))
    if userno > 100:
        print("The given no is not in the range of 1-100, exiting.............")
        exit()
    elif userno == no:
        print("Guessed the correct number")
        print("generated random is: ", no)
        exit()
    elif abs(no - userno) <=3:
        print("The given number is very close")
    elif abs(no - userno) <=10:
        print("The given number is near by")
    else:
        print("no is neither close/far.")    

print("generated random is: ", no)
##############################################
