for i in range (1, 13):
    for j in range(1, 13):
        if i * j < 10:
            print("  ", end="")
        elif i * j < 100:
            print(" ", end="")
        print(i * j, end=" ")
    print()