for i in range(10,0,-1):
    for j in range (10 - i):
        print("  ", end="")
    for j in range (i):
        print(j, end=" ")
    print()