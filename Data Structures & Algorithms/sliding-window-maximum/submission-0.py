class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        if not nums:
            return output
            
        max_heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(max_heap)

        output.append(-max_heap[0][0])
        for index in range(k, len(nums)):
            heapq.heappush(max_heap, (-nums[index], index))

            while max_heap[0][1] <= index - k:
                heapq.heappop(max_heap)

            output.append(-max_heap[0][0])
        return output


        