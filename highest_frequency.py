def highest_frequency(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    max_freq = 0
    answer = 0

    for key, value in freq.items():
        if value > max_freq:
            max_freq = value
            answer = key
    return answer

n = list(map(int, input().split()))
print(highest_frequency(n))