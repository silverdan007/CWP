import random as rand
print (rand.randint(1,5))
def niminit():
    return rand.randint(4,50)

def computerChoice(a):
    if a >= 3:
        return rand.randint(1, 3)
    else:
        return rand.randint(1, a)
def playerChoice(a):
    choice = input("pick a number between 1 - 3")
    if a < 4:
        if int(choice) > 3:
            return playerChoice(a)
    if int(choice) in range (1, 4):
        return int(choice)
    else:
        print("invalid entry")
        return playerChoice(a)
    
def checkWin(player, sticksleft):
    if sticksleft == 0:
        print (f"{player} wins")
        return player
    else:
        return 1
    
def gameOn():
    a = niminit()
    while a != 0:
        comp = computerChoice(a)
        a -= comp
        print (f"{a} sticks left")
        checkWin("comp", a)
        if a == 0:
            return "computer"
        
        player = playerChoice(a)
        a -= player
        print (f"{a} sticks left")
        checkWin("player", a)
        if a == 0:
            return "player"
        

gameOn()