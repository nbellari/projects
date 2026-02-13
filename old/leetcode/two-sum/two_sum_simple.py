from typing import *

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    # just in case there is no match
    return [-1, -1]

list1 = [1, 5, 10, 11]
target = 21

print (twoSum(list1, target))
