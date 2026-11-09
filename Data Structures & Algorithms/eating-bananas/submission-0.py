class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # approach: basically we need to discover the greatest pile in the array, with that we can eat from 1 to max(pile) bananas and then we gotta try which of them is the minimum banana-per-hour - for that instead of iterating through all possibilites we can use a binary search
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas/k)

            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        
        return res

