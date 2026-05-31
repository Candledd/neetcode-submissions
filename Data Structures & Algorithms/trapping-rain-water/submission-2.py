class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        for indx in range(len(height)):
            if indx == 0:
                leftMax[0] = height[0]
                continue

            leftMax[indx] = max(leftMax[indx-1], height[indx])
        
        for indx in range(len(height) - 1, -1, -1):
            if indx == len(height) - 1:
                rightMax[len(height)-1] = height[len(height)-1]
                continue

            rightMax[indx] = max(rightMax[indx+1], height[indx])

        res = 0
        for indx in range(len(height)):
            res += min(leftMax[indx], rightMax[indx]) - height[indx]
        return res

            
