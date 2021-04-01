# first attempt
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

# O(n) solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        answer = fuel = 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                answer = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return answer 
