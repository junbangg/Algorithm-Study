from collections import defaultdict

def isAvailableForHome(employeeData, remote_tasks):
    isAvailable = True
    for data in employeeData:
        if data not in remote_tasks:
            isAvailable = False
    return isAvailable

def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    employee_data = defaultdict(list) # team#, tasks
    team_data = defaultdict(list) # employee#, isHome

    for i, data in enumerate(employees):
        data = data.split()
        employee_data[i+1] = [data]
        
        team_data[int(data[0])].append([i+1, False])
    
    for employee, data in employee_data.items():
        data = data[0]
        teamNumber, tasks = data[0], data[1:]
        if isAvailableForHome(tasks, remote_tasks):
            team_data[int(teamNumber)][1] = True
    
    for team, data in team_data.items():
        if 
        


    return answer