n1 = 60
n2 = 30

while(n1> 0 and n2 >0):
    if (n1 > n2):
        n1 = n1 % n2
    else:
        n2 = n2 % n1
    if n1 == 0:
        print(n2)
    else:
        print(n1)