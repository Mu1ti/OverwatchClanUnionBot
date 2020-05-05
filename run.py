import json, sys, discord, asyncio

from discord.ext import commands

from modules import Config
from modules import Messages
from modules.BlackUser import BlackUser
from modules.ClanMember import ClanMember
from modules.CtlSheet import CtlSheet

global Status 
global TargetBlackUser


Config = 

Config = Config.Import(sys.argv)
DiscordDriver = commands.Bot(command_prefix='')
ClanUnionDriver = ClanUnion(Config, DiscordDriver)

SheetDriver = CtlSheet(Config['GoogleSheet'])
TargetBlackUser = BlackUser()
ClanMemberList = ClanMember()
#ClanMaster = 

@DiscordDriver.event
async def on_ready():
    print("[*] Start ClanUnionBot")

@DiscordDriver.on_message
async def on_message(message):
    global Status 
    verifier = ClanUnionDriver.Verify
    
    if verifier.IsStaff(message):
        if verifier.IsMemberList(message):
            # 멤버리스트가 맞다면 멤버 명단에 추가하면 됨..
            # 멤버리스트는 어디다가..?


            memberList = 
            sendMessage = Messages.ClanMemberVerify()

        sendMessage = Messages.MemberList
        await message.send(sendMessage)

    else:
        staffNotifyChannel = Config['Discord']['StaffNotify']
        sendMessage = Messages.IDKYou(staffNotifyChannel)
        await message.send(sendMessage)

    if ClanUnionDriver.VerifyUser(message):
        sendMessage = Messages.MemberListHelp(Config['Discord']['StaffNotify'])
        await message.send(sendMessage)
        return None

    if ('#' in content) and ('\n' in content):
        Status = "MemberListVerify"
        memberList = content.split('\n')

        author = message.author.name + "#" + message.author.discriminator

        ClanName = ClanMaster[author]
                
        
@DiscordDriver.command()
async def test(message):
    await message.send("What Do You Want To Test?")

@DiscordDriver.command()
async def 네(message):
    global Status 
    global TargetBlackUser

    if ClanUnionDriver.VerifyUser(message):
        sendMessage = Messages.MemberListHelp(Config['Discord']['StaffNotify'])
        await message.send(sendMessage)
        return None

    blackListChannel = discord.utils.get(DiscordDriver.get_all_channels(), guild__name=Config['Discord']['ServerName'], name=Config['Discord']['Channel']['BlackList'])

    if Status == "BlackListVerify":
        SheetDriver.UpdateBlackListSheet(TargetBlackUser.ToList())
        source = TargetBlackUser.Source
        adminUserDiscord = Config['AdminUserDiscord']
        url = Config['GoogleSheet']['URL']

        await blackListChannel.send(Messages.BlackListSpread(TargetBlackUser))
        await message.send(Messages.BlackListUpdate(source, adminUserDiscord, url))

@DiscordDriver.command()
async def 아니요(message):
    global TargetBlackUser

    if ClanUnionDriver.VerifyUser(message):
        sendMessage = Messages.MemberListHelp(Config['Discord']['StaffNotify'])
        await message.send(sendMessage)
        return None

    TargetBlackUser = BlackUser()
    await message.send(Messages.VerifyDeny)

@DiscordDriver.command()
async def 본계정(message):
    global Status 
    global TargetBlackUser

    if ClanUnionDriver.VerifyUser(message):
        sendMessage = Messages.MemberListHelp(Config['Discord']['StaffNotify'])
        await message.send(sendMessage)
        return None

    content = message.message.content
    verify = TargetBlackUser.MessageFormVerify(content)

    if verify == True:
        TargetBlackUser.MessageFormPharse(content)
        TargetBlackUser.GetBlackUserSource(message)
        Status = "BlackListVerify"
        await message.send(Messages.BlackListVerify(TargetBlackUser))

    else :
        warningMessage = "앗...! "+verify+"에 대한 내용이 잘못된 것 같습니다... ㅠㅠ\n해당 내용이 없다면 \"없음\"으로 작성 부탁드립니다! :laughing:"
        await message.send(warningMessage)

@DiscordDriver.command()
async def 블랙리스트(message):
    verifier = ClanUnionDriver.Verify()
    
    if verifier.IsStaff(message):
        sendMessage = Messages.BlackListHelp
        await message.send(sendMessage)

    else:
        staffNotifyChannel = Config['Discord']['StaffNotify']
        sendMessage = Messages.IDKYou(staffNotifyChannel)
        await message.send(sendMessage)


@DiscordDriver.command()        
async def 클랜원명단(message):
    verifier = ClanUnionDriver.Verify()
    
    if verifier.IsStaff(message):
        sendMessage = Messages.MemberList
        await message.send(sendMessage)

    else:
        staffNotifyChannel = Config['Discord']['StaffNotify']
        sendMessage = Messages.IDKYou(staffNotifyChannel)
        await message.send(sendMessage)

if __name__ == "__main__":
    DiscordDriver.run(Config['Discord']['Token'])