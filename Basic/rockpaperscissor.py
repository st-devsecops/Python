# Winning Rules as follows:
# Rock vs paper-> paper wins
# Rock vs scissor-> Rock wins
# paper vs scissor-> scissor wins.
# logic:
# Take the input1 from user
# Take the input2 from user
# verify the input matches to the pre defined values.
# if not matching specify as a comment, u have to give the correct input as mentioned and also exit 
# if it matches 
# if i1 == rock and i2 == paper
#     paper Warning
# if i1=rock and i2 = scissor
# rock win
# if i1 = paper and i2= scissior
# scissor win
# if i1 & i2 same input, its tie

###############################
print("Lets play Rock, paper, scissor Game")

User1 = input("Give the first input: ").lower()
User2 = input("Give the Second input: ").lower()

gameval=["rock", "paper", "scissor"]

if User1 in gameval and User2 in gameval:
    print("Inputs are matching , lets continue the game")    
    if (User1 == "rock" and User2 == "paper") or (User1 == "paper" and User2 == "rock"):
        print("The winner is Paper")
    elif (User1 == "rock" and User2 == "scissor") or (User1 == "scissor" and User2 == "rock"):
        print("The winner is Rock")
    elif (User1 == "paper" and User2 == "scissor") or (User1 == "scissor" and User2 == "paper"):
        print("The winner is Scissor")  
    else:
        (User1 == User2)    
        print("Both the values are same, Game is Tie") 

else:
    print("Unknown inputs, exit the game")
    exit


#####################
