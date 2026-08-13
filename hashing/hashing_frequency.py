arr = [1, 2, 1, 3, 2, 1, 4, 3]
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)

for key,value in freq.items():
    print(key, value)