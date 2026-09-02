nums = [2, 1, 3, 2, 1]
k = 7

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

print(answer)