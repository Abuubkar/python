def moveZeroes(nums: [int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    # 40ms
    index = 0
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
        i += 1
    i = index
    while i < len(nums):
        nums[i] = 0
        i+=1


# [1]
# [0,0,1]
data = [0, 1, 0, 3, 12]
moveZeroes(data)
print(data)


# index = 0
#      char = ""
#       i = 0
#        while i < len(nums):
#             if nums[i] != 0:
#                 nums[index] = nums[i]
#                 index += 1
#             else:
#                 char += "0"
#             i += 1

#         nums[:] = nums[0:index] + list(int(count) for count in char)

# 184 ms
# count = ""
# while (0 in nums):
#     count += "0"
#     nums.remove(0)
# if count != "":
#     nums[:] = nums + list(int(char) for char in count)

# 188 ms
# count = ""
# while (0 in nums):
#     count += "0"
#     nums.pop(nums.index(0))
# if count != "":
#     nums[:] = nums + list(int(char) for char in count)

# 200+ms
# i = 0
# j = int()
# size = len(nums)
# number_of_zero = 0
# while i < size-number_of_zero:

#     if nums[i] == 0:
#         j = i
#         number_of_zero += 1
#         nums.append(0)
#         nums[:] = nums[0:j] + nums[j+1:size+1]
#     if nums[i] != 0:
#         i += 1
