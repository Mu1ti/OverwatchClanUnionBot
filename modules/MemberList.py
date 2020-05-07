import json

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
        return message.split('\n')

    def GetClanName(self, staffList, message):
        author = message.author.name + "#" + message.author.discriminator
        self.Name = staffList[author]

    def GetUpdate(self):
        self.Update = datetime.now().strftime("%Y-%m-%d")

    def Save(self):
        with open('datas/ClanList.json', 'r+', encoding='utf8') as clanListFile :
            clanLists = json.load(clanListFile)
            clanLists[self.Name]['Update'] = self.Update
            clanLists[self.Name]['Members'] = self.Members

            clanListFile.write(json.dumps(clanLists))

    def ToList(self):
        result = ['']
        result += [self.Name, self.Update]
        result += self.Members

        return result