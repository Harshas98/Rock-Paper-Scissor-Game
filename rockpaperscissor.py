import random

def generateRandom(lst):
    return random.choice(lst)

def result(uc,cc):
    if(uc == cc):
        return -1
    elif((uc == "rock" and cc == "scissor") or (uc == "scissor" and cc == "paper") or (uc == "paper" and cc == "rock")):
        return 1
    else:
        return 0


sets = 3
user,computer =0,0
lst = ["rock","paper","scissor"]
print("Welcome to ROCK PAPER SCISSOR game\n")
print("Totally Three sets if you win two sets you are the champion\n")
print("Winning Rules :\n"+
      "Rock vs Paper = paper wins\n"+
      "Rock vs Scissor = Rock Wins\n"+
      "Paper vs Scissor = Scissor Wins\n")
while(sets>0):
        userChoice = input("Enter your choice : ").lower()
        computerChoice = generateRandom(lst)
        if(result(userChoice,computerChoice) == 1):
            print("You won this match!!\n")
            user+=1
        elif(result(userChoice,computerChoice) == 0):
            print("You lost this match!!\n")
            computer +=1
        else:
            print("It's draw!!\n")
            user+=1
            computer+=1
        sets -= 1

print("----------Finally the champion is----------\n".upper())
if(user > computer):
    print("            USER           ")
elif(user < computer):
    print("          COMPUTER          ")
else:
    print("USER AND COMPUTER")
