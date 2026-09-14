class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = set() #supposed to use a hashset 
        for n in nums:
            if n in map:
                return True
            map.add(n)
        return False