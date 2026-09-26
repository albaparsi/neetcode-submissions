class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in dic:
                return [dic[difference], index]
            dic[number] = index


        