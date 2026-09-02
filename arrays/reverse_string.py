class Solution():
    def rev_str(self, s:list[str]):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

s = input().split()
print(Solution().rev_str(s))