import discord, asyncio

from modules import Config
import json

from modules.BlackUser import BlackUser
from modules.CtlSheet import CtlSheet

class ClanUnion:
	def __init__(self, Config, DiscordDriver):
		self.Discord = DiscordDriver
		self.Sheet = CtlSheet(Config['GoogleSheet'])
		self.BlackUser = BlackUser()
		self.StaffList = Config.ClanStaffList

		guild__name = Config['Discord']['ServerName']
		BlackListChannelName = Config['Discord']['Channel']['BlackList']
		MemberListChannelName = Config['Discord']['Channel']['MemberList']

		self.BlackListChannel = discord.utils.get(DiscordDriver.get_all_channels(), guild__name=guild__name, name=BlackListChannelName)
		self.MemberListChannel = discord.utils.get(DiscordDriver.get_all_channels(), guild__name=guild__name, name=MemberListChannelName)

	class BlackList:
        def __init__(self):
            pass

        def HelpMessage(self):
            pass


    class MemberList:
        def __init__(self):
            self.List = {}
            pass

        def Load(self, message):
            content = message.message.contnet

            self.

            


    class StaffList:
        def __init__(self):
            self.List = ""

        def Load(self):
            content = None
            with open('StaffList.json','r',encoding='utf8') as staffListFile:
                content = stafflistFile.read()
                content = json.loads(content)
                self.staffList = content

            return None

    class Verify:
        def __init__(self):
            pass
        
        def IsStaff(self, message, staffList):
		    author = message.author.name + "#" + message.author.discriminator
		
		    if author in staffList:
			    return True

		    return False

        def IsMemberList(self, message):
            content = message.message.content

            if ('#' in content) and ('\n' in content):
                return True

            else False
