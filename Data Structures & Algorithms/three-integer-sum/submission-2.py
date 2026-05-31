class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            
            seen = set()

            for pointer in range(index + 1, len(nums)):
                opposite = -(nums[index] + nums[pointer])

                if opposite in seen:
                    result.add((nums[index], opposite, nums[pointer]))
                else:
                    seen.add(nums[pointer])
        return [list(t) for t in result]

            