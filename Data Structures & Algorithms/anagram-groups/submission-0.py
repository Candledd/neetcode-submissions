class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        emptyMap = defaultdict(list)

        for words in strs:
            sortedWord = "".join(sorted(words))
            emptyMap[sortedWord].append(words)
        return list(emptyMap.values())