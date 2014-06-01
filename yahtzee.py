#game of yahtzee played from the console

from random import randint
import os
os.system('clear')


# The results object
class Results(object):
    def __init__(self,name):
        self.name = name
        self.value = 0
        self.selected = False
    def set_value(self,value):
        self.value = value
        self.selected = True


# initialise
player=[]
player.append(Results('Ones'))
player.append(Results('Twos'))
player.append(Results('Threes'))
player.append(Results('Fours'))
player.append(Results('Fives'))
player.append(Results('Sixes'))
player.append(Results('3 of a kind'))
player.append(Results('4 of a kind'))
player.append(Results('Full House'))
player.append(Results('Yahtzee'))
player.append(Results('Chance'))
player.append(Results('Small Straight'))
player.append(Results('Long Straight'))

choices = ['1','2','3','4','5','6','t','f','h','y','c','s','l']
total = 0
dice_count=[0,0,0,0,0,0,0]

def dice_roll():
    number = randint(1, 6)
    return number

def count_dice():
    for n in range(7):
        dice_count[n] = dice.count(n)
    print "dice count: ", dice_count

def three_of_a_kind():
    dice_sum = 0
    for i in range(7):
        if dice_count[i] > 2:
            dice_sum = sum(dice)
    return dice_sum

def four_of_a_kind():
    dice_sum = 0
    for i in range(7):
        if dice_count[i] > 3:
            dice_sum = sum(dice)
    return dice_sum

def full_house():
    dice_sum = 0
    two_the_same = False
    three_the_same = False
    for i in range(7):
        if dice_count[i] == 2:
            two_the_same = True
        elif dice_count[i] == 3:
            three_the_same = True
    if two_the_same and three_the_same:
        dice_sum = 25
    return dice_sum

def yahtzee():
    dice_sum = 0
    for i in range(7):
        if dice_count[i] == 5:
            dice_sum = 50
    return dice_sum

''' There are 3 possible variations for a small straight that give us a dice_count of

01111XXX : equivalent to 1234
0X1111XX : equivalent to 2345
0XX1111X : equivalent to 3456
'''
def small_straight():
    if (dice_count[1] > 0 and dice_count[2] > 0 and dice_count[3] > 0 and dice_count[4] > 0) or \
        (dice_count[2] > 0 and dice_count[3] > 0 and dice_count[4] > 0 and dice_count[5] > 0) or \
        (dice_count[3] > 0 and dice_count[4] > 0 and dice_count[5] > 0 and dice_count[6] > 0) :
        return 30
    else:
        return 0

def long_straight():
    if (dice[0] == 1 and dice[1] == 2 and dice[2] == 3 and dice[3] == 4 and dice[4] == 5) or \
       (dice[0] == 2 and dice[1] == 3 and dice[2] == 4 and dice[3] == 5 and dice[4] == 6):
        return 40
    else:
        return 0

# work out what the score is for the chosen play
def get_score(index):
    score = 0
    if index == 0:  #ones have been selected
        for i in range(5):
            if dice[i] == 1:
                score += 1
    elif index == 1:  #twos have been selected
        for i in range(5):
            if dice[i] == 2:
                score += 2
    elif index == 2:  #threes have been selected
        for i in range(5):
            if dice[i] == 3:
                score += 3
    elif index == 3:  #fours have been selected
        for i in range(5):
            if dice[i] == 4:
                score +=4
    elif index == 4:  #fives have been selected
        for i in range(5):
            if dice[i] == 5:
                score += 5
    elif index == 5:  #sixes have been selected
        for i in range(5):
            if dice[i] == 6:
                score += 6
    elif index == 6:  #3 of a kind have been selected
        score = three_of_a_kind()
    elif index == 7:  #4 of a kind have been selected
        score = four_of_a_kind()
    elif index == 8:  #full house have been selected
        score = full_house()
    elif index == 9:  #Yahtzee have been selected
        score = yahtzee()
    elif index == 10:  #chance have been selected
        score = sum(dice)
    elif index == 11:  #small straight have been selected
        score = small_straight()
    elif index == 12:  #long straight have been selected
        score = long_straight()
  
    return score       

# Main loop
for turns in range(13):

    # Assign a random number between 1-6 to each of the 5 dice
    dice=[]
    for i in range(5):
        dice.append(dice_roll()) 
        print "Dice " + str(i+1) +"= " + str(dice[i])

    # The 5 dice have been displayed to the screen
    # The user now gets to choose which dice (if any) they want to roll again
    # they are allowed to change the dice twice
    
    exitloop = False
    tries=0
    
    # you get 2 tries to change the dice
    while (tries < 2 and not exitloop):
        # for each entry, check that we have valid dice numbers
    
        dice_entered = False
        while not dice_entered:

            # Allow the user to enter the dice numbers from the keyboard. Use exception handling to check
            # that we have entered numbers only
            while True:
                try:
                    change_dice = int(raw_input("Enter the dice to change:"))
                    break
                except ValueError:
                    print "Please only enter 0-5"

            # If the user enters 0, they dont want to change any dice. Exit the loop if this is the case
            if change_dice == 0:
                exitloop = True
                dice_entered = True
            else:
                #validate that we only entered digits 1 to 5 by 
                change_dice = str(change_dice)
                for entry in range(0,len(change_dice)):
                    digit = int(change_dice[entry])
                    if digit < 1 or digit > 5:
                        print "Please only enter dice numbers 1-5"
                        dice_entered = False
                        break
                    else:
                        #Roll this dice again and assign value
                        dice[digit-1] = dice_roll()
                        dice_entered = True
                    
            #All of the dice numbers entered are OK
            if dice_entered and not exitloop:
                for i in range(5):
                    print "Dice " + str(i+1) +"= " + str(dice[i])
                tries += 1
                   
    # We now ask for which choice the user wants to make
    dice.sort()
    count_dice()

    chosen = False
    while not chosen:
        choice = raw_input("Choose 1,2,3,4,5,6,(t)hree of a kind,(f)our of a kind,full (h)ouse,(y)ahtzee,(c)hance,(s)mall strainght,(l)ong straight: ")
        if choice not in choices:
            print "Please choose only 1,2,3,4,5,6,t,f,h,y,c,s or l"
        else:
            #check we haven't selected this already
            i = choices.index(choice)
            if not player[i].selected:
                score = get_score(i)
                total += score
                chosen = True
                player[i].set_value(score)
                player[i].selected=True
            else:
                chosen = False
    print "\n"
    for i in player:       
        print i.name, i.value
    print "total: " + str(total) + "\n"

