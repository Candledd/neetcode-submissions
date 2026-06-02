from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #hashtable freq string t, 
        #sliding window, left 0, increment right until we find a match, increment left to find optimal, 
        #stop incrementing left when it doesnt match freq table, increment right again until fits
        #when right - left = len(t), check if fits, return that, else increment right again till match/end. 
        #^ lowk can omit comment above because right increments already and right-left is checked when we check freq
        if len(t) > len(s):
            return ""

        answerFreq = Counter(t)
        windowFreq = Counter()
        optimal = float('inf')
        answer = ""
        left = 0
        
        for right in range(len(s)):
            incoming = s[right]
            windowFreq[incoming] += 1

            while not (answerFreq - windowFreq):
                result = right - left + 1
                if result < optimal:
                    optimal = result
                    answer = s[left : right + 1]
                windowFreq[s[left]] -= 1
                left += 1

        return answer

        


        