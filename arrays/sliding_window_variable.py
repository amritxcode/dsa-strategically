class Solution():
    def subLen(self, nums, k):
        left = 0
        window_sum = 0
        answer = 0
        for right in range(len(nums)):
            window_sum += nums[right]
            while window_sum > k:
                window_sum -= nums[left]
                left += 1
            current_length = right - left + 1
            answer = max(answer, current_length)

        return answer

nums = list(map(int, input().split()))
k = int(input())

print(Solution().subLen(nums, k))