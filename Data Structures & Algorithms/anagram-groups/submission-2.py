class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        emptyMap = defaultdict(list)
        for word in strs:
            freqList = [0] * 26
            for char in word:
                #a is the base for alphabetical, subtracting a letter by a show us the distance from a to align with freqList
                freqList[ord(char) - ord('a')] += 1
            emptyMap[tuple(freqList)].append(word)
        return list(emptyMap.values())
            