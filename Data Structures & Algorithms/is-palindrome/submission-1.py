class Solution:
    def isPalindrome(self, s: str) -> bool:

        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:

            if not s[leftPointer].isalnum():
                leftPointer += 1
            elif not s[rightPointer].isalnum():
                rightPointer -= 1

            elif s[leftPointer].lower() != s[rightPointer].lower():
                return False
            else:
                leftPointer += 1
                rightPointer -= 1


        

        return True

        