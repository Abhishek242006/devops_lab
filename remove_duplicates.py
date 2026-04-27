def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # pointer for unique elements

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1  # new length


# Example usage
nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)

print("New length:", new_length)
print("Updated list:", nums[:new_length])