from random import choice

rock="R"
peper ="P"
scissor="S"
player1=0
player2=0

print(f"ROCK == > {rock}")
print(f"PEPER == > {peper}")
print(f"scissor == > {scissor}\n")

while True:

    player=input("Enter :").upper()
    random_player=choice([rock,peper,scissor])

    # rack peper scissor conditions 

    if len(player) == 1 or player in [rock,peper,scissor]:
        if player == random_player:
            print("\ndrow the match !")
        elif player == rock and random_player == peper:
            player2+=1
            print("\noppocite player win !")
        elif player == peper and random_player == rock:
            player1+=1
            print("\nyou win !")
        elif player == scissor and random_player == rock:
            player2+=1
            print("\noppocite player win !")
        elif player == rock and player == scissor:
            player1+=1
            print("\nyou win !")
        elif player == peper and random_player == scissor:
            player2+=1
            print("\noppocite player win !")
        elif player == scissor and random_player == peper:
            player1+=1
            print("\nyou win !")
        print("-----------------------")
        print(player ,"player1 win count :",player1)
        print(random_player ,"player2 win count :",player2)
        print("-----------------------")

    else:
        print(" You give the input is worng !")
    
    if player1 == 10 or player2 == 10:
        if player1 > player2:
            print(" win the match !")
            break
        else:
            print(" random player win ! ")
            break
