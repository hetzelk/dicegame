import time
import os
import random
os.system("cls")



def title():
    print(" ______  __              __       ____              __   ") 
    print("|   __ \|  |.---.-.----.|  |--.__|    |.---.-.----.|  |--.")
    print("|   __ <|  ||     Double-Ace's Style      _  |  __||    < ")
    print("|______/|__||___._|____||__|__|_______||___._|____||__|__|")
    print("")

title()

def rules():
    print("This game is kind of like Blackjack, except simplified.")
    print("You only get 2 cards, whatever those 2 cards are is what you get.")
    print("You're betting your money on pure luck.")
    print("There are no Jacks, Queens, or Kings, just Aces and 1-10.")
    print("The highest possible you can get is 22 points (2 Aces).")
    print("")
    print("")

rules()

player1 = input("What is player 1's name? ")
player2 = input("What is player 2's name? ")

#startbank = int(input("How much would you like to deposit? "))

#printbank = print("You deposited",startbank)

continuegame = ""

while continuegame == "":
    os.system("cls")

    title()
    print(player1)
    betp1 = int(input("How much do you want to bet? "))

    def card1():
        card = random.randrange(10) + 2 # Integer from 0 to 9
        return card
    def card2():
        card = random.randrange(10) + 2 # Integer from 0 to 9
        return card

    def comcard1():
        card = random.randrange(10) + 2 # Integer from 0 to 9
        return card
    def comcard2():
        card = random.randrange(10) + 2 # Integer from 0 to 9
        return card

    cardname1 = card1()
    cardname2 = card2()

    computercardname1 = comcard1()
    computercardname2 = comcard2()

    suitlist = ["Spades", "Hearts", "Clubs", "Diamonds"]



    def suit1():
        suit = random.randrange(4)
        return suit
    def suit2():
        card = random.randrange(4)
        return card

    def comsuit1():
        card = random.randrange(4)
        return card
    def comsuit2():
        card = random.randrange(4)
        return card

    suitname1 = suit1()
    suitname2 = suit2()

    computersuitname1 = comsuit1()
    computersuitname2 = comsuit2()



    def cardnamechanger1(cardname1):

        if cardname1 == 11:
            result = ("A")
            return(result)
     
        elif cardname1 == 10:
            result = ("10")
            return(result)

        elif cardname1 == 9:
            result = ("9")
            return(result)

        elif cardname1 == 8:
            result = ("8")
            return(result)

        elif cardname1 == 7:
            result = ("7")
            return(result)

        elif cardname1 == 6:
            result = ("6")
            return(result)

        elif cardname1 == 5:
            result = ("5")
            return(result)

        elif cardname1 == 4:
            result = ("4")
            return(result)

        elif cardname1 == 3:
            result = ("3")
            return(result)

        elif cardname1 == 2:
            result = ("2")
            return(result)

    def suitnamechanger1(suitname1):

        if suitname1 == 0:
            result = ("Spades")
            return(result)

        elif suitname1 == 3:
            result = ("Hearts")
            return(result)

        elif suitname1 == 2:
            result = ("Clubs")
            return(result)

        elif suitname1 == 1:
            result = ("Diamonds")
            return(result)

    showsuitname1 = suitnamechanger1(suitname1)

    def cardnamechanger2(cardname2):

        if cardname2 == 11:
            result = ("A")
            return(result)
     
        elif cardname2 == 10:
            result = ("10")
            return(result)

        elif cardname2 == 9:
            result = ("9")
            return(result)

        elif cardname2 == 8:
            result = ("8")
            return(result)

        elif cardname2 == 7:
            result = ("7")
            return(result)

        elif cardname2 == 6:
            result = ("6")
            return(result)

        elif cardname2 == 5:
            result = ("5")
            return(result)

        elif cardname2 == 4:
            result = ("4")
            return(result)

        elif cardname2 == 3:
            result = ("3")
            return(result)

        elif cardname2 == 2:
            result = ("2")
            return(result)

    def suitnamechanger2(suitname2):

        if suitname2 == 0:
            result = ("Spades")
            return(result)

        elif suitname2 == 3:
            result = ("Hearts")
            return(result)

        elif suitname2 == 2:
            result = ("Clubs")
            return(result)

        elif suitname2 == 1:
            result = ("Diamonds")
            return(result)

    showsuitname2 = suitnamechanger2(suitname2)




    def computercardnamechanger1(computercardname1):

        if computercardname1 == 11:
            result = ("A")
            return(result)
     
        elif computercardname1 == 10:
            result = ("10")
            return(result)

        elif computercardname1 == 9:
            result = ("9")
            return(result)

        elif computercardname1 == 8:
            result = ("8")
            return(result)

        elif computercardname1 == 7:
            result = ("7")
            return(result)

        elif computercardname1 == 6:
            result = ("6")
            return(result)

        elif computercardname1 == 5:
            result = ("5")
            return(result)

        elif computercardname1 == 4:
            result = ("4")
            return(result)

        elif computercardname1 == 3:
            result = ("3")
            return(result)

        elif computercardname1 == 2:
            result = ("2")
            return(result)

    def computersuitnamechanger1(computersuitname1):

        if computersuitname1 == 0:
            result = ("Spades")
            return(result)

        elif computersuitname1 == 3:
            result = ("Hearts")
            return(result)

        elif computersuitname1 == 2:
            result = ("Clubs")
            return(result)

        elif computersuitname1 == 1:
            result = ("Diamonds")
            return(result)

    showcomputersuitname1 = computersuitnamechanger1(computersuitname1)



    def computercardnamechanger2(computercardname2):

        if computercardname2 == 11:
            result = ("A")
            return(result)
     
        elif computercardname2 == 10:
            result = ("10")
            return(result)

        elif computercardname2 == 9:
            result = ("9")
            return(result)

        elif computercardname2 == 8:
            result = ("8")
            return(result)

        elif computercardname2 == 7:
            result = ("7")
            return(result)

        elif computercardname2 == 6:
            result = ("6")
            return(result)

        elif computercardname2 == 5:
            result = ("5")
            return(result)

        elif computercardname2 == 4:
            result = ("4")
            return(result)

        elif computercardname2 == 3:
            result = ("3")
            return(result)

        elif computercardname2 == 2:
            result = ("2")
            return(result)

    def computersuitnamechanger2(computersuitname2):

        if computersuitname2 == 0:
            result = ("Spades")
            return(result)

        elif computersuitname2 == 3:
            result = ("Hearts")
            return(result)

        elif computersuitname2 == 2:
            result = ("Clubs")
            return(result)

        elif computersuitname2 == 1:
            result = ("Diamonds")
            return(result)

    showcomputersuitname2 = computersuitnamechanger2(computersuitname2)




    def winner(cardname1, cardname2, computercardname1, computercardname2):
        if cardname1 + cardname2 > computercardname1 + computercardname2:
            return(1)
            #print("You win.")

        else:
            return(0)
            #print("Dealer wins.")



    showwinner = winner(cardname1, cardname2, computercardname1, computercardname2)
        
    def definewinner(showwinner):
        if showwinner > 0:
            winnings = betp1 * 2
            return winnings
        else:
            return 0

    def printwinner(showwinner):
        if showwinner > 0:
            print(player1, "You Win!")
        else:
            print(player2, "You Win!")



    winnings = definewinner(showwinner)


    def getstartdeposit():
        currentbank = 1000
        return currentbank 

    currentbank = getstartdeposit()

    def addtobank(winnings, currentbank):
        result = currentbank + winnings
        return result

    addwinningstobank = addtobank(winnings, currentbank)

    def betfrombank(addwinningstobank):
        currentbank = addwinningstobank - betp1
        result = currentbank
        return(result)

    betbank = betfrombank(addwinningstobank)

#    print("******")
#    print("get start deposit $", currentbank)
#    print("add to bank $", addwinningstobank)
#    print("bet from bank $", betbank)
#    print("******")









    start = input("Press Enter to start Double-Ace.")


    print("")
    print(player1, "Your 1st Card:", cardnamechanger1(cardname1), "of", showsuitname1)
    print(player1, "Your 2nd Card:", cardnamechanger2(cardname2), "of", showsuitname2)

    print("")
    print(player2, ", Would you like to bet against their hand? ")

    betp2 = int(input("How much would you like to bet? (Enter 0 if nothing) "))

    print("")
    print(player2, "  Your 1st Card:", computercardnamechanger1(computercardname1), "of", showcomputersuitname1)
    print(player2, "  Your 2nd Card:", computercardnamechanger2(computercardname2), "of", showcomputersuitname2)





    def showp1winnings():
        result = (betp1 *2) + betp2
        return(result)


    def showp2winnings():
        result = (betp2 *2) + betp1
        return(result)





    print("")
    print(printwinner(showwinner))


    restart = input("Press enter to restart.")
    #time.sleep(3.0)
























































