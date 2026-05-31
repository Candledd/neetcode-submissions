
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for indx, num in enumerate(nums):
            if num > 0:
                break
            
            if indx > 0 and nums[indx] == nums[indx - 1]:
                continue

            left = indx + 1
            right = len(nums)-1

            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    result.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                if total > 0:
                    right -= 1
                if total < 0:
                    left += 1
        return result
                
                
