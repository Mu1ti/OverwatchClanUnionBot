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

def MessageContent(messageName):
    result = ''
    with open('messages/'+messageName,'r', encoding='utf8') as messageFile :
        result = messageFile.read()

    return result