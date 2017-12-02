#square
#size = int(input("enter a size."))
#for i in range(size):
#    print ('* ' * size)

#print("-----------------------------------")
#hollow square
#n = int(input("enter another size"))
#print('*' * n)
#for i in range(n-2):
#    print ('*' + ' ' * (n-2) + '*')
#print('*' * n)

#print("-----------------------------------")
#stump 
print("enter tree height: ")
treeHeight = int(input())
print("enter tree width: ")
treeWidth = int(input())

print("Enter stump width")
stumpWidth = int(input())
print("Enter stump height")
stumpHeight = int(input())

for i in range(treeHeight):
    print (" "+" "*(treeWidth))*(treeHeight-i-1) + ("*" +" "*(treeWidth))*(2*i+1)
    
for i in range(stumpHeight):
    if i in[0]:
        #print((" "+" "*(treeWidth))*(treeHeight-1)(((stumpWidth)/2)-0.5) + "* "*(stumpWidth))
        print((" "+" "*(treeWidth))*(treeHeight-1) + "*"*(stumpWidth))
        #print("* "*(stumpWidth))
    else:
        #print((" "+" "*(treeWidth))*(treeHeight-1)(((stumpWidth)/2)-0.5) + "* "*(stumpWidth))
        print((" "+" "*(treeWidth))*(treeHeight-1) + "*"*(stumpWidth))
        #print("* "*(stumpWidth))
