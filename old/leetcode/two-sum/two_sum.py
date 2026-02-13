from typing import *

# This variant uses a hash to store the elements as it walks the list
def twoSum(nums: List[int], target: int) -> List[int]:
    visited: Dict[int, int] = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if (visited.get(diff) != None):
            return [visited[diff], i]
        else:
            visited[nums[i]] = i
    return [-1, -1]

list1 = [2, 4]
target = 6

print (twoSum(list1, target))
