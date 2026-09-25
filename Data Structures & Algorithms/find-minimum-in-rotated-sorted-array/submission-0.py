class Solution:
    def findMin(self, nums: List[int]) -> int:

        result = nums[0]

        l, r =0, len(nums) - 1

        while l<=r:

            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break

            middle = l + ((r - l)//2)
            result = min(result, nums[middle])

            if nums[middle] >= nums[l]:
                l = middle + 1
            elif nums[middle] <= nums[r]:
                r = middle - 1

        return result



        