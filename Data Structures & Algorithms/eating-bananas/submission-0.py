class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l, r = 1, max(piles)
        result = r



        while l <= r:
            middle = l + ((r - l) // 2)

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / middle)

            if totalTime <= h:
                result = middle
                r = middle - 1

            elif totalTime > h:
                l = middle + 1

                
        return result






