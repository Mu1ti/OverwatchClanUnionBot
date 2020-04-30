from oauth2client.service_account import ServiceAccountCredentials
import gspread

class CtlSheet:
    def __init__(self, Config):
        self.config = Config
        self.BlackListSheet = None
        self.MemberListSheet = None

        self.InitBlacklistSheet()

    def InitSheets(self):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com\/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread.json', scope)
        googleSpread = gspread.authorize(credentials)
        documentName =  self.config['DocumentName']

        self.BlackListSheet = self.GetBlackListSheet()
        self.MemberListSheet = self.GetMemberListSheet()

    def GetBlackListSheet(self):
        return self.GoogleSpread.open(SpreadSheetName).worksheet(self.config['BlackListSheet']['SheetName'] )

    def GetMemberListSheet(self, sheetName):
        return self.GoogleSpread.open(SpreadSheetName).worksheet(self.config['MemberListSheet']['SheetName'] )

    def UpdateBlackListSheet(self, user):
        self.BlackListSheet.append_row(user)

    def UpdateMemberListSheet(self, user):
        # 업데이트 날짜순으로 정렬해야 하기 때문에 생각을 좀 할 필요가 있음
        pass
        