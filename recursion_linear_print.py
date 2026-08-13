def linear(i,n):
    if i > n:
        return
    print(i)
    linear(i+1,n)

linear(1,4)
