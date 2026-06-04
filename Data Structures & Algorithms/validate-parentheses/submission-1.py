class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpenTuple = { ")" : "(", 
                        "]" : "[",
                        "}" : "{" }
        for char in s:
            if char in closeOpenTuple:
                if stack and stack[-1] == closeOpenTuple[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        
