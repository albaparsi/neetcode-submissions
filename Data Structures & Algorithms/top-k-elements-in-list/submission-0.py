class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for i in nums:
            
            freq[i] = 1 + freq.get(i, 0)

        sorted_by_value = dict(
        sorted(freq.items(), key=lambda x: x[1])
        )

        items = list(sorted_by_value.items())


        return [key for key, value in items[-k:]]




