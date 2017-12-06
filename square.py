
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


def printAstrics(treeWidth):
    for i in range(treeWidth):
        print("*", end='')
    print()


print(">>>>>>>>>>")
print()


treeRatio = float(treeHeight)/treeWidth
#middle of tree

for i in range(0,treeHeight):
    #this determines the number of astrics that the tree row needs
    numAstrics = i*treeRatio
    numAstrics = int(math.floor(numAstrics))
    #this maked it so the tree lines up in the middle
    if (numAstrics%2 == 0):
        numAstrics += 1
        
    #this determines the spaces that the row needs to line up
    spaces = int(math.floor((treeWidth - numAstrics)/2))
    print(" "*spaces,end="")
    print("*"*numAstrics)

