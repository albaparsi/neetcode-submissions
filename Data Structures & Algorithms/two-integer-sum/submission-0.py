class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashT = {}

        for num in range(len(nums)):
            diff = target - nums[num]

            if diff in hashT:
                return [hashT[diff], num]
            hashT[nums[num]] = num
            



        