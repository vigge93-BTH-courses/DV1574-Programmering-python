import random


def max_n(*nums):
    if nums is None or len(nums) < 2:
        raise TypeError('Must provide at least two arguments')
    if not all(map(lambda n: type(n) == int or type(n) == float, nums)):
        raise TypeError('All provided arguments must be numerical')

    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return largest


nums = [random.randrange(0, 100) for x in range(1000)]
print(max_n(*nums))
