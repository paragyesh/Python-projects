import random
l = ['rock','paper','scissor']
#rock vs paper -> . Paper wins
#rock vs Scissior - > rock wins
#paper vs scissor- > scissor wins
#Game-Rock,Paper,Scissor.py


while True:
    ccount= 0
    ucount = 0
    uc = int(input('''
Game start.....
1 Yes
2 NO | Exit

        '''))
    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1.rock
2.paper
3.scissor
                        '''))
            if userInput==1:
                uchoice = "rock"
            elif userInput==2:
                uchoice = "paper"
            elif userInput==3:
                uchoice=="scissor"
            Cchoice = random.choice(l)
            if Cchoice==uchoice:
                print("Computer Value",Cchoice)
                print("User Value ", uchoice)
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice == "scissor") or (uchoice == "paper"and Cchoice=="scissor") or (uchoice=="scissor" and Cchoice=="paper"):
                print("Computer Value:",Cchoice)
                print("User Value :", uchoice)
                print ("You Win")
                ucount=ucount+1
            else:
                print("Computer Value:",Cchoice)
                print("User Value :", uchoice)
                print ("Computer Win")
                ccount=ccount+1
                print() 
                print()
                print()           
        if ucount==ccount:
            print("Final Game Draw...")
            print("User Score", ucount)
            print("Computer Score", ccount)
        elif ucount>ccount:
            print("Final you win  the game...")
            print("User Score", ucount)
            print("Computer Score", ccount)
        else:
            print(" Final Computer win the game...")
            print("User Score", ucount)
            print("Computer Score", ccount)
    else:
        break           

