#1
for i in range(4):
    for j in range(5):
        print("*",end=" ")
    print()

print()
#2
for i in range(5):
    for j in range(i+1):
        print("*", end =" ")
    print()

print()
#3
for i in range(5):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
print()
#4
for i in range(5):
    for j in range(i+1):
        print(i+1, end=" ")
    print()
print()
#5
for i in range(5):
    for j in range(5,i,-1):
        print("*",end = " ")
    print()
print()
#6
for i in range(5):
    for j in range(1,6-i):
        print(j,end = " ")
    print()
print()
#7
for i in range(5):
    for j in range(4-i):
        print(" ",end =" ")
    for j in range(2*i+1):
        print("*", end=" ")
    for j in range(4-i):
        print(" ",end =" ")
    print()
print()
#8
for i in range(5):
    for j in range(i):
        print(" ",end =" ")
    for j in range(2*5-(2*i+1)):
        print("*", end=" ")
    for i in range(i):
        print(" ",end =" ")
    print()
print()
#9
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
print()
