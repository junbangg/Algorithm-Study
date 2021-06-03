import sys
def solution(ads):
    time, cost = 0, 0
    ad = False
    ads.sort()
    while ads:
        newAd = []
        addTime = 0
        removeAt = -1
        minCost = sys.maxsize
        maxPriorityCost = -sys.maxsize
        prioritySwitch = False
        for i, ad in enumerate(ads):
            if ad[0] == time and maxPriorityCost < ad[1]:
                maxPriorityCost = ad[1]
                newAd = ad
                addTime = ad[0] - time + 5
                removeAt = i
                prioritySwitch = True
            if not prioritySwitch:
                potentialCost = (time-ad[0]) * ad[1]
                if minCost > potentialCost:
                    minCost = potentialCost
                    removeAt, newAd = i, ad
                    addTime = 5
        ads.pop(removeAt)
        if prioritySwitch:
            cost += maxPriorityCost
        else:
            cost += minCost
        time += addTime
        print(newAd)
        print(time)
        print(cost)
    return cost


tc1 = [[1,3],[3,2],[5,4]] # 20
tc2 = [[0,3],[5,4]] # 0
tc3 = [[0,1], [0,2], [6,3], [8,4]]  # 40
tc4 = [[5,2], [2,2], [6,3], [9,2]] # 33

#print(solution(tc1))
#print(solution(tc2))
print(solution(tc3))
#print(solution(tc4))
