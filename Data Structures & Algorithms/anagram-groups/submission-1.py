class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        emptyMap = {}

        for words in strs:
            sortedWord = "".join(sorted(words))

            if sortedWord not in emptyMap:
                emptyMap[sortedWord] = []

            emptyMap[sortedWord].append(words)
        return list(emptyMap.values())