class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #key: numbers, value: index
        hashMap = {}
        
        for curr, number in enumerate(nums):
            needed = target - number

            if needed in hashMap:
                return [hashMap[needed], curr]
                
            hashMap[number] = curr
        