def sum_of_n(i,s):
    if i < 1:
        print(s)
        return
    sum_of_n(i-1,s+i)

sum_of_n(3,0)