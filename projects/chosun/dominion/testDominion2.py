# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 13:33:23 2020

@author: Sunghoon Cho
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
if len(player_names)>2:
    nV=12
else:
    nV=8
nC = -10 + 10 * len(player_names)

#Define box, supply_prder, and supply which has been replaced with call to the
# refactored funtion in the testUtility.py file
box = testUtility.getBoxes(nV) 
supply_order = testUtility.getSupplyOrder() 
supply = testUtility.getSupply(nV, nV, player_names)

#test scenario 2
#duchy supply has been emptied 
supply["Duchy"] = []

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.getPlayerObjects(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)