def highest_frequency(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i, 0) + 1

    max_freq = 0
    answer = None

    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            answer = key
    return answer

n = input()
print(highest_frequency(n))