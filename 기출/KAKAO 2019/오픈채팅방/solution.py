from collections import OrderedDict

def convertToOutputStrings(info, uid_currentID):
    outputStrings = []
    command_koreanString = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다."
    }
    for uid, command in info:
        outputString = uid_currentID[uid] + command_koreanString[command]
        outputStrings.append(outputString)
    return outputStrings

def solution(record):
    uid_currentID = OrderedDict()
    outputInfo = []

    for data in record:
        splitData = data.split()
        command, uid, nickname = "", "", ""
        if len(splitData) == 2:
            command, uid = splitData[0], splitData[1]
        else:
            command, uid, nickname = splitData[0], splitData[1], splitData[2]
        if command == "Leave":
            outputInfo.append([uid, command])
        else:
            if command == "Enter":
                outputInfo.append([uid, command])
            uid_currentID[uid] = nickname
    print(uid_currentID)
    print(outputInfo)
    return convertToOutputStrings(outputInfo, uid_currentID)

    


