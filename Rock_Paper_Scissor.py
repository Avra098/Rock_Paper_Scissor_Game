import random
L = ["rock","paper","scissior"]

while True:
    ucount=0
    Ccount=0
    uc=int(input('''
1.Press 1 to play
2. Exit
                 '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1.rock
2.paper
3.scissor
                '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="paper"
            elif userInput==3:
                uchoice="scissor"
                
            Cchoice=random.choice(L)
            print(uchoice)
            print(Cchoice)
            
            if Cchoice==uchoice:
                print("Computer Value :",Cchoice)
                print("User Value :",uchoice)
                print("Game Draw")
                ucount=ucount+1
                Ccount=Ccount+1
            elif(uchoice=="rock"and Cchoice=="scissor")or(uchoice=="paper"and Cchoice=="rock")or(uchoice=="scissor"and Cchoice=="paper"):
                print("Computer value :",Cchoice)
                print("User value",uchoice)
                print("You Win")
                ucount=ucount+1
            else:
                print("Computer value :",Cchoice)
                print("User value",uchoice)
                print("Computer Win")
                Ccount=Ccount+1
            if ucount==Ccount:
                print("Final Game Draw")
                print("User Score :",ucount)
                print("Computer Score :",Ccount)
            elif ucount>Ccount:
                print("Finally You win")
                print("User Score",ucount)
                print("Computer Score",Ccount)
            else:
                print("Finally Computer wins")
                print("User Score",ucount)
                print("Computer Score",Ccount)
            
            
        else:
            break
