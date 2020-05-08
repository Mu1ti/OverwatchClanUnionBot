import sys, discord, logging

from discord.ext import commands

from modules import Init
from modules.ClanUnion import ClanUnion

#####################################
#            Initialize             #
#####################################

Config = Init.Config(sys.argv)
DiscordDriver = commands.Bot(command_prefix='')
ClanUnionDriver = ClanUnion(Config, DiscordDriver)

@DiscordDriver.event
async def on_ready():
    ClanUnionDriver.ChannelInit()
    print("[*] Start ClanUnionBot")

#####################################
#     MemberList & ErrorReport      #
#####################################

@DiscordDriver.event
async def on_command_error(message, exception):
    if message.channel.type.name == "private" and not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        return None

    # 클랜원 리스트 받기
    if ClanUnionDriver.IsMemberList(message):
        ClanUnionDriver.Status = "MemberListVerify"
        ClanUnionDriver.MemberListUpdate(message)
        await message.channel.send(ClanUnionDriver.Message.MemberListVerify(ClanUnionDriver.MemberList))

    print("[*] "+message.author.name + "#" + message.author.discriminator+" : "+message.message.content)

#####################################
#             BlackList             #
#####################################

@DiscordDriver.command()
async def 본계정(message):
    if message.channel.type.name == "private" and not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        return None
    
    verify = ClanUnionDriver.IsBlackUser(message)

    if verify == True:
        ClanUnionDriver.Status = "BlackUserVerify"
        ClanUnionDriver.BlackUserUpdate(message)
        await message.channel.send(ClanUnionDriver.Message.BlackListVerify(ClanUnionDriver.BlackUser))

    else :
        await message.channel.send(ClanUnionDriver.Message.BlackListError(verify))

#####################################
#             TypedVerify           #
#####################################

@DiscordDriver.command()
async def 네(message):
    if message.channel.type.name == "private" and not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        return None

    if ClanUnionDriver.Status == "BlackUserVerify":
        ClanUnionDriver.Sheet.UpdateBlackListSheet(ClanUnionDriver.ListedBlackUser())

        src = ClanUnionDriver.BlackUser.Source
        admins = Config['AdminUserDiscord']
        url = Config['GoogleSheet']['URL']
        msg = ClanUnionDriver.Message.BlackListUpdate(src, admins, url)

        await ClanUnionDriver.BlackListChannel.send(ClanUnionDriver.Message.BlackListSpread(ClanUnionDriver.BlackUser, url))
        await message.channel.send(msg)

        ClanUnionDriver.BlackUserReset()

        return None
    
    elif ClanUnionDriver.Status == "MemberListVerify":
        ClanUnionDriver.MemberList.Save()
        ClanUnionDriver.Sheet.UpdateClanListSheet()

        src = ClanUnionDriver.MemberList.Name
        admins = Config['AdminUserDiscord']
        url = Config['GoogleSheet']['URL']
        msg = ClanUnionDriver.Message.MemberListUpdate(src, admins,url)

        await ClanUnionDriver.MemberListChannel.send(ClanUnionDriver.Message.MemberListSpread(ClanUnionDriver.MemberList, url))
        await message.channel.send(msg)

        ClanUnionDriver.MemberListReset()

        return None

    ClanUnionDriver.Status = ""

    # EasterEgg
    await message.channel.send("네? ^^;;")

@DiscordDriver.command()
async def 아니요(message):
    if message.channel.type.name == "private" and not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        return None

    if ClanUnionDriver.Status :
        ClanUnionDriver.BlackUserReset()
        ClanUnionDriver.Status = ""
        await message.channel.send(ClanUnionDriver.Message.VerifyDeny)

        return None

    # EasterEgg
    await message.channel.send("네? ㅁ..무엇이 아닌가요? ^^;;")

#####################################
#                Help               #
#####################################

@DiscordDriver.command()
async def 블랙리스트(message):
    if message.channel.type.name == "private" and not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        return None

    await message.send(ClanUnionDriver.Message.BlackListHelp)

@DiscordDriver.command()
async def 클랜원명단(message):
    if message.channel.type.name == "private" and not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        return None

    await message.send(ClanUnionDriver.Message.MemberListHelp)    

#####################################
#                Run.               #
#####################################

if __name__ == "__main__":
    DiscordDriver.run(Config['Discord']['Token'])