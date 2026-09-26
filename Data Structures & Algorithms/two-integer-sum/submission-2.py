class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for index in range(len(nums)):
            number = nums[index]

            difference = target - number

            if difference in dic:
                return [dic[difference], index]

            dic[number] = dic.get(number, index)