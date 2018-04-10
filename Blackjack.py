import random
import locale

#takes input of number of players and error checks for 5 or less players
playerinput = raw_input("Blackjack: How many players: ")

try:
    numPlayers=int(playerinput)
except ValueError:
    print "Not a Number"
#still need to figure out what to do if player enters letters
if numPlayers > 5:
    print "Must be 5 or less players"
else:
    print ('There are ' + str(numPlayers) + ' players and one dealer')


#takes players name
nameinput = raw_input("What is your name? ")

#creates the deck of cards in an array "Deck" which contains "Suit" and "Value"
suits=["clubs", "diamonds", "hearts", "spades"]

values=["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

deck=[]

for suit in suits:
    
    for value in values:
        card={}
        card["suit"]=suit
        card["value"]=value
        deck.append(card)
        
#print deck

#creates an list to contain players and their informaion
players =[]

#selects a random card, prints it, then removes it from the deck, then prints number of cards left twice then displays both cards then loops that for each player adding them to a list

for eachPlayer in range(numPlayers+1):
        selection = random.choice(deck)
#        print selection
        
        deck.remove(selection)
        card1 = selection
#        print(len(deck))
        
        selection = random.choice(deck)
#        print selection
        
        deck.remove(selection)
        card2=selection
#        print(len(deck))
        
        handList = [card1, card2]
        
        player = {
            "name" : 'Player '+ str(eachPlayer),
            "money" : 100.25,
            "hand" : handList,
            "handValue" : 0
        }
        
        players.append(player)       

#sets the 0 player to Dealer and 1 to player input
players[0]["name"] = 'Dealer'

players[1]["name"] = nameinput

#set score to zero, score check, and add to HandValue

for a in players:
    a["handValue"] = 0

for a in players:
    
   for b in a["hand"]:
        
        if isinstance(b["value"], int) == True:
            a["handValue"] = a["handValue"] + b["value"]
          
        elif b["value"] == "A":
            a["handValue"] = a["handValue"] + 11
                 
        else:
            a["handValue"] = a["handValue"] + 10

# loop to print results of dealing for each player
for z in range(len(players)):
    print players[z]["name"] +' has ' + str(players[z]["hand"][0]["value"]) + ' of ' + str(players[z]["hand"][0]["suit"])  + ' and ' + str(players[z]["hand"][1]["value"]) + ' of ' + str(players[z]["hand"][1]["suit"]) + ', totaling ' + str(players[z]["handValue"])
    
    
#does calculations based on Dealer Total and declares winners 

