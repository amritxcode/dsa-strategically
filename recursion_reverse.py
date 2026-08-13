def rev(i,n):
    if i < 1:
        return
    print(i)
    rev(i-1,n)

rev(4,1)