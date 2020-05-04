import json


class BlackUser:
    def __init__(self):
        self.BattleTag = ""
        self.Tier = ""
        self.Discord = ""
        self.Old = ""
        self.Gender = ""
        self.OtherPersonalInformation = ""
        self.Reason = ""
        self.Source = ""
        self.Explanation = ""
        self.SubBattleTag = ""
    
    def MessageFormVerify(self, message):
        properties = \
        {
            'BattleTag' : False,
            'Tier' : False,
            'Discord' : False,
            'Old' : False,
            'Gender' : False,
            'OtherPersonalInformation' : False,
            'Reason' : False,
            'Explanation' : False,
            'SubBattleTag' : False
        }

        for line in message.split('\n'):
            if self.GetPropertyContent(line, '본계정'):
                properties['BattleTag']=True
            elif self.GetPropertyContent(line, '점수대'):
                properties['Tier']=True
            elif self.GetPropertyContent(line, '디스코드'):
                properties['Discord']=True
            elif self.GetPropertyContent(line, '나이'):
                properties['Old']=True
            elif self.GetPropertyContent(line, '성별'):
                properties['Gender']=True
            elif self.GetPropertyContent(line, '기타 개인신상'):
                properties['OtherPersonalInformation']=True
            elif self.GetPropertyContent(line, '사유'):
                properties['Reason']=True
            elif self.GetPropertyContent(line, '세부내용'):
                properties['Explanation']=True
            elif self.GetPropertyContent(line, '부계정'):
                properties['SubBattleTag']=True

        if not properties['BattleTag']:
            return "본계정"
        if not properties['Tier']:
            return "점수대"
        if not properties['Discord']:
            return "디스코드"
        if not properties['Old']:
            return "나이"
        if not properties['Gender']:
            return "성별"
        if not properties['OtherPersonalInformation']:
            return "기타 개인신상"
        if not properties['Reason']:
            return "사유"
        if not properties['Explanation']:
            return "세부내용"
        if not properties['SubBattleTag']:
            return "부계정"

        return True

    def MessageFormPharse(self, message):
        for line in message.split('\n'):
            if '본계정' in line:
                self.BattleTag = self.GetPropertyContent(line, '본계정')
            if '점수대' in line:
                self.Tier = self.GetPropertyContent(line, '점수대')
            if '디스코드' in line:
                self.Discord = self.GetPropertyContent(line, '디스코드')
            if '나이' in line:
                self.Old = self.GetPropertyContent(line, '나이')
            if '성별' in line:
                self.Gender = self.GetPropertyContent(line, '성별')
            if '기타 개인신상' in line:
                self.OtherPersonalInformation = self.GetPropertyContent(line, '기타 개인신상')
            if '사유' in line:
                self.Reason = self.GetPropertyContent(line, '사유')
            if '세부내용' in line:
                self.Explanation = self.GetPropertyContent(line, '세부내용')
            if '부계정' in line:
                self.SubBattleTag = self.GetPropertyContent(line, '부계정')

    def GetPropertyContent(self, line, propertyName):
        content = None

        if propertyName in line :
            if ':' in line :
                content = ''.join(line.split(':')[1:])

            else:
                content = line.replace(propertyName, '')

            content = content.strip()

            if content : 
                return content

        return False

    def GetBlackUserSource(self, message):
        author = message.author.display_name
        clan = ""

        with open('ClanMasterList.json', 'r', encoding='utf8') as ClanMasterListFile:
            clanMasterList = ClanMasterListFile.read()
            clanMasterList = json.loads(clanMasterList)
            clan = clanMasterList[author]

        self.Source = clan

    def GetListLenFromInfoType(self, infoType):
        if infoType == "Discord":
            return 2

        elif infoType == "Reason":
            return 3

        elif infoType == "SubBattleTag":
            return 8

        return None

    def GetSplitList(self, string):
        if ',' in string :
            return string.split(',')

        elif '/' in string :
            return string.split('/')

        elif ' ' in string :
            return string.split(' ')

        return [string]

    def GetUserInfoToList(self, string, infoType):
        listLen = self.GetListLenFromInfoType(infoType)
        result = self.GetSplitList(string)
        listedStringLen = len(result)

        if listLen > listedStringLen :
            result += ['']*(listLen-listedStringLen)

        elif listLen < listedStringLen :
            result = result[0:(listLen-1)]

        return result
        
    def ToList(self):
        result = []
        subBattleTagList = self.GetUserInfoToList(self.SubBattleTag, "SubBattleTag")
        discordList = self.GetUserInfoToList(self.Discord, "Discord")
        reasonList = self.GetUserInfoToList(self.Reason, "Reason")

        result += [self.BattleTag, self.Tier]
        result += discordList
        result += [self.Old, self.Gender, self.OtherPersonalInformation]
        result += reasonList
        result += [self.Source, self.Explanation]
        result += subBattleTagList
        
        
        return result