def subsets(nums):
    result = [[]]
    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        result.extend(new_subsets)
    return result

nums = {int(x) for x in input("Enter unique numbers separated by space: ").split()}
print(subsets(nums))
