### Function to make decison 
import random
pick=["ROCK","PAPER","SCISSOR"]
def decision(playerPick,computerPick):
    if playerPick == computerPick:
        return 0
    if playerPick == "ROCK":
        if computerPick == "SCISSOR":
            return 1
        else:
            return -1
    if playerPick == "PAPER":
        if computerPick == "SCISSOR":
            return -1
        else:
            return 1
    if playerPick == "SCISSOR":
        if computerPick == "ROCK":
            return -1
        else:
            return 1

def playerInput():
    while True:
        playerPick=input("Make your pick (Rock, Paper or Scissor):")
        if playerPick.upper() not in pick:
            print("Not valid pick, Try again!")
        else:
            break
    return playerPick

print("Game Rules: \nROCK breaks SCISSOR\nSCISSOR cut PAPER\nPAPER covers ROCK")
print("="*25)
s = {1:"WIN", -1:"LOSE", 0:"TIE"}
while True:
    score = dict()
    cP = pick[random.randint(0,2)]
    pP = playerInput()
    result = decision(pP.upper(),cP)
    print(f'\nYou picked {pP.upper()} and Computer picked {cP}! \n\nRESULT:{s[result]}! \n')
    score[s[result]] = score.get(s[result],0)+1
    n=int(input("What's next? \n\n1) Play again \n2) quit \n Your Choice:"))
    if n == 2:
        break

print('FINAL SCORECARD')
print("="*25)
print(score)
#print(f'WON : {score.get('WIN',0)} \nLOST : {score.get('LOSE',0)} \nTIED :{score.get('TIE',0)}')




#### 1) Rock
#### 2) Paper
#### 3) Scissor