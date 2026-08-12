def first_non_repeating(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1

    min_freq = float('inf')
    answer = None

    for key, value in freq.items():
        if value < min_freq:
            min_freq = value
            answer = key

    return answer
s = input()
print(first_non_repeating(s))