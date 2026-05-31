class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #freq dict
        count = {}
        for num in nums:
            count[num] = count.get(num, 0)+1

        #sort freq hashmap
        tupleList = [(freq,num) for num, freq in count.items()]
        tupleList.sort(reverse=True)

        return [num for freq, num in tupleList[:k]]
