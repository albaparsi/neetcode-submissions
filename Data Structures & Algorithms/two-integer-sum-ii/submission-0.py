class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        result = []
        a = 0
        b = len(numbers) - 1

        while a < b:
            
            if numbers[a] + numbers[b] > target:
                b -= 1
            if numbers[a] + numbers[b] < target:
                a += 1
            if numbers[a] + numbers[b] == target:
                result = [a + 1 , b + 1]

                return result
        