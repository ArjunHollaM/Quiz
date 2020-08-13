import questions as q
import time
import matplotlib.pyplot as plt
import numpy as np

def single():
    print("All the best!\nLet's start!")
    time.sleep(2)
    total=q.ask()
    return total



if __name__ == '__main__':
    print("Welcome to the Science and Technology quiz!")
    print("Hello!!\nI'm Arjun...and your host for today!")
    time.sleep(3)
    print("::::INSTRUCTIONS::::\n-> You have to select the number of players\n-> There will be 10 questions..each carrying 10 points.\n-> Type your response after you see 4 options.")
    print("-> Every wrong answer will lead to deduction of 5 points\n-> If you wish to use a lifeline just type 'life' instead of your response")
    time.sleep(10)
    print("LIFELIES: \n1-50-50-->Removes two options which are wrong.-Awards 5 points\n2-Pass-->Skips the question-Awards 3 points\n3-Eliminate One-->Eliminates one wrong option-Awards 7 points")
    time.sleep(6)
    players=input(" Type 1 - Single player \n Type 2 - 2 players\n")
    if(players=='1'):
        name=input("Your name::")
        if(input("Whenever you are ready type 'ok'\n")=='ok'):
            result=single()
            if result>=40 and result<70: print("Well done {}! .\n you have got {} points.".format(name,result))
            if result>=70 and result<70: print("Wow {} , You know your facts really well.\n You have got {} points.".format(name,result))
            if result>=90 and result<=100: print("You are a genius {}!!.\n You have got {} points. You belong amongst the best.".format(name,result))
            if result>=20 and result<40: print("You could do better {} .\n You got {} points.".format(name,result))
            if result>=0 and result<20: print("Well what was that {}.Could have gone a lot worse. You got only {} ".format(name,result))
            if result<0: print("You did this on purpose right? \n You got {} {}.".format(result,name))
            plt.bar(name, result,align='center',alpha=0.9)
            plt.ylabel("Points")
            plt.show()
        else:
            print("It's ok. Try later")
    elif players=="2":
        player1=input("Name of player1::")
        player2=input("Name of player2::")
        play=[player1,player2]
        all_scores=list()
        for i in play:
            print("Type 'ok' whenever you are ready "+i)
            res=input()
            if (res=='ok'):
                result=single()
                all_scores+=[result]
                if result>=40 and result<70: print("Well done {}! .\n you have got {} points.".format(i,result))
                if result>=70 and result<70: print("Wow {} , You know your facts really well.\n You have got {} points.".format(i,result))
                if result>=90 and result<=100: print("You are a genius {}!!.\n You have got {} points. You belong amongst the best.".format(i,result))
                if result>=20 and result<40: print("You could do better {} .\n You got {} points.".format(i,result))
                if result>=0 and result<20: print("Well what was that {}.Could have gone a lot worse. You got only {} ".format(i,result))
                if result<0: print("You did this on purpose right? \n You got {} {}.".format(result,i))
            if  res != 'ok':
                print("It's ok. Try later")
                break
        if len(all_scores)>1:
            if all_scores[0]>all_scores[1]:
                print("STANDINGS:")
                print("1st----> " + player1 + "    " + str(all_scores[0]) + "\n2nd----> " + player2 + "    " + str(all_scores[1]))
                print("Congratulations {}!! You have won the contest!".format(player1))
                pl = (player1, player2)
                y_pos = np.arange(len(pl))
                plt.bar(y_pos,all_scores, align='center', alpha=0.9)
                plt.xticks(y_pos, pl)
                plt.ylabel("Points")
                plt.title("Score Review")
                plt.show()
            elif all_scores[1]>all_scores[0]:
                print("STANDINGS:")
                print("1st----> " + player2 + "    " + str(all_scores[1]) + "\n2nd----> " + player1 + "    " + str(all_scores[0]))
                print("Congratulations {}!! You have won the contest!".format(player1))
                pl=(player1,player2)
                y_pos = np.arange(len(pl))
                plt.bar(y_pos,all_scores, align='center', alpha=0.9)
                plt.xticks(y_pos, pl)
                plt.ylabel("Points")
                plt.title("Score Review")
                plt.show()
        else:
            print("No Result")
    else:
        print("Invalid Input")


