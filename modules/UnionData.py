import json, os

class UnionData:
    def __init__(self, DatasConfig):
        self.Config = DatasConfig
        self.Staff = self.Load('StaffList')
        self.Clan = self.Load('ClanList')
        self.Black = self.Load('BlackList')

    def Load(self, listType):
        listFileName = self.Config[listType]
        result = None

        if listType == "StaffList":
            result = self._jsonLoad(listFileName)

        elif listType == "ClanList":
            result = self._jsonLoad(listFileName)

        elif listType == "BlackList":
            result = self._jsonLoad(listFileName)

        return result

    def Update(self, listType):
        listFileName = self.Config[listType]

        if listType == "StaffList":
            self._jsonSave(listFileName, self.Staff)

        elif listType == "ClanList":
            self._jsonSave(listFileName, self.Clan)

        elif listType == "BlackList":
            self._jsonSave(listFileName, self.Black)

    def _jsonLoad(self, fileName):
        content = None

        with open(fileName, 'r', encoding='utf8') as jsonFile:
            content = json.loads(jsonFile.read())

        return content

    def _jsonSave(self, fileName, content):
        with open(fileName, 'w', encoding='utf8') as jsonFile:
            jsonFile.write(json.dumps(content))

        return content