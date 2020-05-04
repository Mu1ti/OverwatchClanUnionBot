from oauth2client.service_account import ServiceAccountCredentials
import gspread

class CtlSheet:
    def __init__(self, Config):
        self.Config = Config
        self.BlackListSheet = None
        self.MemberListSheet = None

        self.InitSheets()

    def InitSheets(self):
        documentName =  self.Config['DocumentName']
        jsonKeyFileName = self.Config['JsonKeyFileName']

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(jsonKeyFileName, scope)
        googleSheetDriver = gspread.authorize(credentials)
        
        self.ClanUnionDocument = googleSheetDriver.open(documentName)
        self.BlackListSheet = self.GetBlackListSheet()
        self.MemberListSheet = self.GetMemberListSheet()

    def GetBlackListSheet(self):
        return self.ClanUnionDocument.worksheet(self.Config['BlackListSheet']['SheetName'] )

    def GetMemberListSheet(self):
        return self.ClanUnionDocument.worksheet(self.Config['MemberListSheet']['SheetName'] )

    def UpdateBlackListSheet(self, user):
        self.BlackListSheet.append_row(user)

    def UpdateMemberListSheet(self, user):
        # 업데이트 날짜순으로 정렬해야 하기 때문에 생각을 좀 할 필요가 있음
        pass