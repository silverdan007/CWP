import random
arr = ["rock", "paper", "scissors"]
playerScore = 0
comScore = 0
def compChoice():
    choice = random.randint(0,2)
    return choice

def playerChoice():
    choice = input("type 1 = rock, 2 = paper, 3 = scissors")
    try:
        if 1 < int(choice) > 3:
            print("out of range please select 1 - 3")
            return playerChoice()
        else:
            print(choice)
            return int(choice) - 1
    except ValueError:
        print("enter a number")
        return playerChoice()
    return int(choice) - 1

def vet(player, comp, playerScore, comScore):
    if comp == player:
        print("OMG its a lion Lol Draw")
    elif comp == 0 and player == 2:
        print("computer wins Rock beats scissors")
        comScore += 1
    elif player == 0 and comp == 2:
        print("Yay you win Rock beats scisors")
        playerScore += 1
    elif player > comp:
        print(f"you win {arr[player]} beats {arr[comp]}")
        playerScore += 1
    else:
        print(f"Comp win {arr[comp]} beats {arr[player]}")
        comScore += 1
    return playerScore, comScore
rounds = 5

for i in range(rounds):
    play1 = playerChoice()
    print(f"you chose {arr[play1]}")
    play2 = compChoice()
    print(f"computer chose {arr[play2]}")
    playerScore, comScore = vet(play1,play2, playerScore, comScore)
    print(comScore)
    print(playerScore)
    print(f"Round {i + 1}")

if comScore > playerScore:
    print("computer wins")
else:
    print("You win")



    
    

