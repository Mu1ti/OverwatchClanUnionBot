import discord, json

from modules import Messages
from modules import Init
from modules import Util

from modules.UnionData import UnionData
from modules.BlackUser import BlackUser
from modules.MemberList import MemberList
from modules.CtlSheet import CtlSheet

class ClanUnion:
    def __init__(self, Config, DiscordDriver):
        self.Config = Config
        self.Discord = DiscordDriver

        self.Status = ""
        self.BlackUser = BlackUser()
        self.MemberList = MemberList()

        self.Message = Messages

        self.Sheet = CtlSheet(Config['GoogleSheet'])
        self.Data = UnionData(Config['Datas'])
        self.Util = Util

        self.BlackListChannel = None
        self.MemberListChannel = None

    def ChannelInit(self):
        guildName = self.Config['Discord']['ServerName']
        blackListChannelName = self.Config['Discord']['Channel']['BlackList']
        memberListChannelName = self.Config['Discord']['Channel']['MemberList']

        self.BlackListChannel = discord.utils.get(self.Discord.get_all_channels(), guild__name=guildName, name=blackListChannelName)
        self.MemberListChannel = discord.utils.get(self.Discord.get_all_channels(), guild__name=guildName, name=memberListChannelName)

    def IsStaff(self, message):
        author = message.author.name + "#" + message.author.discriminator
    
        if author in list(self.Data.Staff.keys()):
            return True

        return False

    def IsBlackUser(self, message):
        result = self.BlackUser.MessageFormVerify(message.message.content)
        return result

    def IsMemberList(self, message):
        result = self.MemberList.MessageFormVerify(message.message.content)
        return result

    def BlackUserUpdate(self, message):
        self.BlackUser.GetBlackUserSource(self.Data.Staff, message)
        self.BlackUser.MessageFormPharse(message.message.content)

    def BlackUserReset(self):
        self.BlackUser = BlackUser()

    def MemberListReset(self):
        self.MemberList = MemberList()

    def MemberListUpdate(self, message):
        self.MemberList.GetClanName(self.Data.Staff, message)
        self.MemberList.GetUpdate()
        self.MemberList.MessageFormPharse(message.message.content)

    def ListedMemberList(self):
        return self.MemberList.ToList()

    def ListedBlackUser(self):
        return self.BlackUser.ToList()