# Find the minimum sum of any 3 consecutive elements.

class Solution():
    def minSum(self, nums: list[int], k:int)-> int:
        left = 0
        window_sum = 0
        answer = float('inf')
        for right in range(len(nums)):
            window_sum += nums[right]
            if right - left + 1 == k:
                answer = min(answer, window_sum)
                window_sum -= nums[left]
                left += 1
        return answer

nums = list(map(int, input().split()))
k = int(input())

print(Solution().minSum(nums, k))