for i in range (1,10):
    #Print our spaces
    for j in range(10 - i):
        print("  ",end="")
    for j in range (i):
    #Count to whatever number we need *Plus one is to prevent 0
        print (j + 1, end=" ")
    #Subtracts one from i, first one being 0 so it does not print
    for j in range (i - 1, 0, - 1):
        print (j, end=" ")
    print()