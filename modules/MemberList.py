import json, time
from datetime import datetime
class MemberList:
    def __init__(self):
        self.Name = ""
        self.Update = ""
        self.Members = ""

    def MessageFormVerify(self, content):
        content = content
        if '#' in content and '\n' in content:
            return True

        return False

    def MessageFormPharse(self, message):
        self.Members = message.split('\n')

    def GetClanName(self, staffList, message):
        author = message.author.name + "#" + message.author.discriminator
        self.Name = staffList[author]

    def GetUpdate(self):
        self.Update = time.time()

    def Save(self):
        with open('datas/ClanList.json', 'r+', encoding='utf-8-sig') as clanListFile :
            clanLists = json.load(clanListFile)
            clanLists[self.Name]['Update'] = self.Update
            clanLists[self.Name]['Members'] = self.Members

            clanListFile.truncate(0)
            clanListFile.seek(0)

            clanListFile.write(json.dumps(clanLists,ensure_ascii=False, indent=4))

    def GetStrUpdateTime(self):
        return datetime.fromtimestamp(self.Update).strftime('%Y-%m-%d %H:%M:%S')

    def ToText(self):
        return '\n'.join(self.Members)
