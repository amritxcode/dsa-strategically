nums = [1, 2, 3, 5, 7, 9, 12, 15]
target = 14

left = 0
right = len(nums) - 1

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        print([left, right])
        break 
    
    elif total < target:
        left += 1

    else:
        right -= 1

else:
    print([])