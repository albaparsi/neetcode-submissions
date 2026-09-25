class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")" : "(", "]" : "[", "}" : "{"}


        for c in s:
            if c not in hashMap:
                stack.append(c)
            
            else:
                if not stack:
                    return False

                else:

                    popped = stack.pop()

                    if popped != hashMap[c]:
                        return False

        if not stack:
            return True


        else:
            return False