class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hasht = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in hasht:
                stack.append(char)
            else:
                if not stack or hasht[stack.pop()] != char:
                    return False

        return not stack
