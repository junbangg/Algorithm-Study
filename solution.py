class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        costMap = []
        counter = 1
        for (g, c) in zip(gas, cost):
            if counter == len(gas):
                counter = 0
            costMap.append((g - c, counter))
            counter += 1
        for i in range(len(costMap)):
            origin = costMap[i]
            total, nxt = origin
            while total >= 0:
                if nxt == i:
                    return i
                cur = costMap[nxt]
                total += cur[0]
                nxt = cur[1]
        return -1
