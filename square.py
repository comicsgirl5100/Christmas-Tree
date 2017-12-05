
#imports
from __future__ import print_function
import math

def printf(str, *args):
    print(str % args, end='')


for x in xrange(10):
    printf('.')
print("done")
#..........done

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
print(" ", end="")
      
for i in range(treeHeight):
    for x in xrange((treeWidth)*(treeHeight-i-1)):
        printf(" ") #, (end=""))*((treeWidth))*(treeHeight-i-1))

    print(("*"*(int(math.floor(treeWidth/2)))+"*" + "*"*(int(math.floor(treeWidth/2))))*(2*i+1))


stumpTab = ((treeWidth)*(treeHeight-1) + (int(math.floor(treeWidth/2))) - (int(math.floor(stumpWidth/2))))

for i in range(stumpHeight):
    if i in[0]:
        for x in xrange(stumpTab+1):
            printf(" ")
        print("*"*(int(math.floor(stumpWidth/2))) + "*" + "*"*(int(math.floor(stumpWidth/2))))

    else:
        for x in xrange(stumpTab+1):
            printf(" ")
        print("*"*(int(math.floor(stumpWidth/2))) + "*" + "*"*(int(math.floor(stumpWidth/2))))
        #print((" "*stumpTab) + ("*"*(int(math.floor(stumpWidth/2))) + "*" + "*"*(int(math.floor(stumpWidth/2)))))
