
#imports
from __future__ import print_function
import math

#dimensions for tree and stump
while(True):
    #ask user for info
    print("Enter tree width: ")
    treeWidth = int(input())

    print("Enter tree height (Must be at least half the width):")
    treeHeight = int(input())

    print("Enter stump height: ")
    stumpHeight = int(input())

    print("Enter stump width: ")
    stumpWidth = int(input())

    if(
        treeHeight > stumpHeight and
        treeWidth > stumpWidth and
        treeHeight >= (treeWidth/2)
        ):
        #ask user for info again
        print("Good input! I'll draw a tree now")
        break
        
    else:
        #good info, carry on
        print("Bad input, try again")


def astrics(treeWidth):
    for i in range(treeWidth):
        print("*", end='')
    print()
        
#to make center line
if(treeWidth%2 == 0):
    treeWidth += 1

for i in range(1, (treeHeight-1)):
    print(i)

print(">>>>>>>>>>")

#top of tree
for i in range(treeWidth/2):
    print(" ", end='')
print("*")
#values for middle of tree
treeRatio = float(treeHeight)/treeWidth

#middle of tree
for i in range(1,(treeHeight-1)):
    #this determines the number of astrics that the tree row needs
    numAstrics = ((i+1)*(treeRatio))
    numAstrics = int(math.floor(numAstrics))
    #this maked it so the tree lines up in the middle
    if (numAstrics%2 == 0):
        numAstrics += 1
        
    #this determines the spaces that the row needs to line up
    spaces = (((treeWidth) - numAstrics)/2)
    for i in range(spaces):
        print(" ", end='')
    print("*"*numAstrics)

#bottom of tree
astrics(treeWidth)

###code that currently works to print tree but not correct width.
###prints tree part     
##for i in range(treeHeight):
##    for x in range((treeWidth)*(treeHeight-i-1)):
##        print(" ", end='')
##
##    print(("*"*(int(math.floor(treeWidth/2))) + "*" + "*"*(int(math.floor(treeWidth/2))))*(2*i+1))
##
##
##stumpTab = ((treeWidth)*(treeHeight-1) + (int(math.floor(treeWidth/2))) - (int(math.floor(stumpWidth/2))))
##
###prints stump`
##for i in range(stumpHeight):
##    for x in range(stumpTab):
##        print(" ", end='')
##    print("*"*(int(math.floor(stumpWidth/2))) + "*" + "*"*(int(math.floor(stumpWidth/2))))

