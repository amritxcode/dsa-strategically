for i in range(5):
    for j in range(4-i):
        print(" ",end =" ")
    for j in range(2*i+1):
        print("*", end=" ")
    for j in range(4-i):
        print(" ",end =" ")
    print()
for i in range(5):
    for j in range(i):
        print(" ",end =" ")
    for j in range(2*5-(2*i+1)):
        print("*", end=" ")
    for i in range(i):
        print(" ",end =" ")
    print()