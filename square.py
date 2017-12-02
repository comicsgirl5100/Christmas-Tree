#imports
import math


while(True):
    #ask user for info
    print("enter tree height: ")
    treeHeight = int(input())

    print("enter tree width: ")
    treeWidth = int(input())

    print("Enter stump height: ")
    stumpHeight = int(input())

    print("Enter stump width: ")
    stumpWidth = int(input())

    if(treeHeight < stumpHeight or treeWidth < stumpWidth):
        #ask user for info again
        print("bad input, try again")
    else:
        #good info, carry on
        break
print("1", end="")
print("2", end="")
print("3")

for i in range(treeHeight):
    print (" "*(treeWidth))*(treeHeight-i-1) + (("*"*(int(math.floor(treeWidth/2)))+"*" + "*"*(int(math.floor(treeWidth/2))))*(2*i+1))


stumpTab = ((treeWidth)*(treeHeight-1) + (int(math.floor(treeWidth/2))) - (int(math.floor(stumpWidth/2))))

for i in range(stumpHeight):
    if i in[0]:
        print((" "*stumpTab) + ("*"*(int(math.floor(stumpWidth/2))) + "*" + "*"*(int(math.floor(stumpWidth/2)))))

    else:
        print((" "*stumpTab) + ("*"*(int(math.floor(stumpWidth/2))) + "*" + "*"*(int(math.floor(stumpWidth/2)))))
