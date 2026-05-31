import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        noOfZeros = 0

        for num in nums:
            if num:
                prod *= num
            else:
                noOfZeros += 1

        if noOfZeros > 1:
            return [0] * len(nums)
        
        result = [0] * len(nums)
        for index, num in enumerate(nums):
            if noOfZeros == 1:
                if num == 0 :
                    result[index] = prod
                else:
                    result[index] = 0
            else:
                result[index] = prod // num

        return result

