def first_non_repeating(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1
    
    for key in freq:
        if freq[key] == 1:
            return key
        
s = input()
print(first_non_repeating(s))