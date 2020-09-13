import random
total=0
result=0
player1point=0
player2point=0
lst=["stone","paper","scissor"]

print("<------WELCOME TO STONE PAPER AND SCISSOR-------->")
print("<--------WANT TO WIN!!!! GET 5 POINTS BUDDY-------> ")
while result!=5:
    player1=input("whats your choise:")
    player2=random.choice(lst)
    print("Computer choice is:",player2)
    if player1=="stone":
        if player2=="paper":
            player2point=player2point+1
            print("---player2 you get one point buddy---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="stone":
        if player2=="scissor":
            player1point=player1point+1
            print("---player1 you get one point buddy---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="paper":
        if player2=="stone":
            player1point=player1point+1
            print("---player1 you get one point buddy---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="paper":
        if player2=="scissor":
            player1point=player2point+1
            print("---player1 you get one point buddy---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="scissor":
        if player2=="stone":
            player1point=player2point+1
            print("---player1 you get one point buddy---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="scissor":
        if player2=="paper":
            player1point=player1point+1
            print("---player2 you get one point buddy---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="stone":
        if player2=="stone":
            print("---tie!---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="scissor":
        if player2=="scissor":
            print("---tie!---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1=="paper":
        if player2=="paper":
            print("---tie!---")
            print("player1 point is:",player1point)
            print("player2 point is:",player2point)
    if player1point==5:
        result=player1point
        print("Player1 you win")
        break
    if player2point==5:
        result=player2point
        print("Computer wins")
        break
