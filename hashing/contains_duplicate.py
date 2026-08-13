def dups(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

n = list(map(int, input().split()))
print(dups(n))