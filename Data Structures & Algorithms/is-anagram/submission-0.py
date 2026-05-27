class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for letter in s:
            s_hash[letter] = s_hash.get(letter, 0) + 1
        for letter in t:
            t_hash[letter] = t_hash.get(letter, 0) + 1

        if s_hash == t_hash:
            return True

        return False
        