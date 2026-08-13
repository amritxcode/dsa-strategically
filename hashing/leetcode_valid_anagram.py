def is_anagram(s, t):
    freq = {}
    if len(s) != len(t):
        return False
    
    for i in s:
        freq[i] = freq.get(i, 0) + 1

    for i in t:
        if i not in freq:
            return False

        freq[i] -= 1

        if freq[i] < 0:
            return False

    return True

s = input()
t = input()
print(is_anagram(s,t))