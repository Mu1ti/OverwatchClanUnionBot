import json

from datetime import datetime

def BlackUserToText(blackUser):
    result = ""

    result += "본계정 : " + blackUser.BattleTag + "\n"
    result += "점수대 : " + blackUser.Tier + "\n"
    result += "디스코드 : " + blackUser.Discord + "\n"
    result += "나이 : " + blackUser.Old + "\n"
    result += "성별 : " + blackUser.Gender + "\n"
    result += "기타 개인신상 : " + blackUser.OtherPersonalInformation + "\n"
    result += "사유 : " + blackUser.Reason + "\n"
    result += "세부내용 : " + blackUser.Explanation + "\n"
    result += "부계정 : " + blackUser.SubBattleTag + "\n"

    return result

def GetClanList():
    with open('datas/ClanList.json', 'r+', encoding='utf-8-sig') as ClanListFile:
        return json.load(ClanListFile)

def SortingClanList():
    clanList = GetClanList()
    sortList = []
    result = {}

    for clan in clanList:
        sortList.append([clanList[clan]['Update'], clan])

    sortList.sort()
    sortList.reverse()

    for clan in sortList:
        result[clan[1]] = clanList[clan[1]]

    return result

def GetRowCount(clanList):
    result = 0
    for clan in clanList:
        memberCount = len(clanList[clan]['Members'])
        if result < memberCount:
            result = memberCount

    return result

def ConvertClanListForSheet():
    clanList = SortingClanList()
    rowCount = GetRowCount(clanList)
    result = []
    helpMessage = "검색은 Ctrl + F를 누르시고, 배틀태그를 입력 해 주세요! (ex 납작해졌군#1234)\n" + \
                    "클랜 관리자 이외에 절대 공유하지 말아주세요.\n" + \
                    "제작자 및 관리자는 유출로 인한 피해에 대해 책임지지 않습니다."

    result.append([helpMessage])

    clanNameRow = ['클랜명']
    for clanName in clanList:
        clanNameRow.append(clanName)

    result.append(clanNameRow)

    updateRow = ['업데이트 날짜']
    
    for clanName in clanList:
        updateString = datetime.fromtimestamp(clanList[clanName]['Update']).strftime('%Y-%m-%d %H:%M:%S')
        updateRow.append(updateString)

    result.append(updateRow)

    clanMemberRows = []

    for i in range(0,rowCount):
        memberRow = ['']

        for clanName in clanList:
            if i < len(clanList[clanName]['Members']):
                memberRow.append(clanList[clanName]['Members'][i])
            else:
                memberRow.append('')
                
        clanMemberRows.append(memberRow)

    for row in clanMemberRows:
        result.append(row)

    return result

def MessageContent(messageName):
    result = ''
    with open('messages/'+messageName,'r', encoding='utf8') as messageFile :
        result = messageFile.read()

    return result