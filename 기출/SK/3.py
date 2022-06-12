# from collections import defaultdict
# def solution(n, plans, clients):
#     answer = [0] * (n-1)
#     dataList = []
#     refinedPlans = defaultdict(list)

#     allServices = []
#     for number, info in enumerate(plans):
#         info = info.split()
#         data = int(info[0])
#         allServices.extend(info[1:])
#         dataList.append(data)
#         refinedPlans[number+1].extend(allServices)
#     for clientNumber, requirements in enumerate(clients):
#         requirements = requirements.split()
#         data = int(requirements[0])
#         services = requirements[1:]

#         minimumPlan = 0
#         for i, providedData in enumerate(dataList):
#             print(data, providedData)
#             if data <= providedData:
#                 minimumPlan = i + 1
#                 break
#         if providedData < data:
#             continue
#         services = set(services)
#         print(minimumPlan)
#         # print(services)
#         # print(refinedPlans)
#         for index in range(minimumPlan, len(refinedPlans)+1):
#             # print(refinedPlans[index])
#             # print(set(refinedPlans[index]).intersection(services))
#             if len(set(refinedPlans[index]).intersection(services)) == len(services):
#                 # print(index)
#                 answer[clientNumber] = index
#                 break

#     return answer

from collections import defaultdict
def solution(n, plans, clients):
    answer = [0] * (n-1)
    dataList = []
    refinedPlans = defaultdict(set)

    allServices = []
    for number, info in enumerate(plans):
        info = info.split()
        data = int(info[0])
        allServices.extend(info[1:])
        dataList.append(data)
        refinedPlans[number+1] = set(allServices)
        
    for clientNumber, requirements in enumerate(clients):
        requirements = requirements.split()
        data = int(requirements[0])
        services = set(requirements[1:])

        minimumPlan = 0
        for i, providedData in enumerate(dataList):
            if data <= providedData:
                minimumPlan = i + 1
                break
        if providedData < data:
            continue
        for index in range(minimumPlan, len(refinedPlans)+1):
            if len(refinedPlans[index].intersection(services)) == len(services):
                answer[clientNumber] = index
                break

    return answer