#Create functions that initialize the lists along with any 
# opportunities for making common functions

#The goal of this file is to eliminate redundant game data setup code

#The refactored code will come from playDominion.py in order to generate 
# different versions of test data and play the game

#Move the refactored code to this file and update testDominion1.py and 
# testDomonion2.py by removing original code and replace it with calls to 
# the refactored code

import Dominion
import random
from collections import defaultdict

#getBoxes takes refactored code from testDominion and creates helper functions
#to initialize the boxes
def getBoxes(nV):
    #Define box
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

#getSupplyOrder takes refactored code from testDominion and creates helper functions
#to initialize the supply order
def getSupplyOrder():
    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}
    return supply_order

#getSupply takes refactored code from testDominion and creates helper functions
#to fill the supply for the game round
def getSupply(nV, nC, player_names):
    box = getBoxes(nV)
    #Pick 10 cards from box to be in the supply.
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list,[(k,box[k]) for k in random10])
    insertIntoSupply(supply, player_names, nV, nC)
    return supply

#insertIntoSupply takes refactored code from testDominion and creates helper functions
#to insert the specified amount of supply into overall supply 
def insertIntoSupply(supply, player_names, nV, nC):
    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC

#getPlayerObjects takes refactored code from testDominion and creates helper functions
#to create and get player objects for the game round
def getPlayerObjects(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players