class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap 
        map = {}
        for i,n in enumerate(nums):
            compliment = target - n
            if compliment in map:
                return [map[compliment], i]
            map[n] = i 
        return []