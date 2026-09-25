class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0 
        result = []
        nums.sort()


        for i, num in enumerate(nums):

            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue

            a = i + 1
            b = len(nums) - 1

            while a < b:

                currentSum = nums[a] + nums[b] + num

                if currentSum > target:
                    b -= 1
                if currentSum < target:
                    a += 1

                if currentSum == target:
                    result.append([num, nums[a], nums[b]]) 
                    a += 1
                    b -= 1

                    while nums[a] == nums[a - 1] and a < b:
                        a += 1

        return result

            


        