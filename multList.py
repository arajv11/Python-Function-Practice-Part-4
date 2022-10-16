def mult_list(nums):
    if (len(nums) < 2):
        return "Not enough numbers in argument"
    else:
        answer = nums[0]
        for i in range(1, len(nums)):
            answer *= nums[i]
        return answer

print(mult_list([1]))
print(mult_list([1, 2, 3]))