from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        count = list(sorted(count, key=count.get, reverse=True))
        return count[:k]

        