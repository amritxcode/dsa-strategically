def count_frequency(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1
    return freq

n = list(map(int, input().split()))
print(count_frequency(n))