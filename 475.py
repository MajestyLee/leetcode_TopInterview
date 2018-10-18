'''
475.
Heaters
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
'''


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        r = 0
        n = len(heaters)
        f = True
        i = 1
        houses = sorted(houses)
        heaters = sorted(heaters)
        for house in houses:
            if house < heaters[0]:
                if f:
                    r = heaters[0] - house if heaters[0] - house > r else r
                    f = False
                continue
            if house > heaters[-1]:
                r = houses[-1] - heaters[-1] if houses[-1] - heaters[-1] > r else r
                break
            while (i < n):
                if house >= heaters[i - 1] and house <= heaters[i]:
                    rr = min(house - heaters[i - 1], heaters[i] - house)
                    r = rr if rr > r else r
                    break
                i += 1
        return r
