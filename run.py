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
Logger = logging.getLogger()
LoggHandler = None


@DiscordDriver.event
async def on_ready():
    ClanUnionDriver.ChannelInit()

    Logger.setLevel(logging.INFO)
    LoggHandler = logging.FileHandler('actions.log', 'w', 'utf-8-sig')
    Logger.addHandler(LoggHandler)

    print("[*] Start ClanUnionBot")

#####################################
#     MemberList & ErrorReport      #
#####################################

@DiscordDriver.event
async def on_command_error(message, exception):
    if message.channel.type.name == "text":
        return None

    if not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is not Staff")
        return None

    # 클랜원 리스트 받기
    if ClanUnionDriver.IsMemberList(message):
        ClanUnionDriver.Status = "MemberListVerify"
        ClanUnionDriver.MemberListUpdate(message)
        Logger.info("[*] "+ message.author.name + "#" + message.author.discriminator+" is send me memberlist "+message.message.content)
        await message.channel.send(ClanUnionDriver.Message.MemberListVerify(ClanUnionDriver.MemberList))
        return None

    Logger.info("[!] "+ message.author.name + "#" + message.author.discriminator+" is make exception! "+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    Logger.info("[!] Exception Type : "+exception.args[0])
    Logger.info("[!] "+ message.author.name + "#" + message.author.discriminator+" : "+message.message.content)

#####################################
#             BlackList             #
#####################################

@DiscordDriver.command()
async def 본계정(message):
    if message.channel.type.name == "text":
        return None

    if not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is not Staff")
        return None
    
    verify = ClanUnionDriver.IsBlackUser(message)

    if verify == True:
        ClanUnionDriver.Status = "BlackUserVerify"
        ClanUnionDriver.BlackUserUpdate(message)
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is send me blacklist "+message.message.content)
        await message.channel.send(ClanUnionDriver.Message.BlackListVerify(ClanUnionDriver.BlackUser))

    else :
        await message.channel.send(ClanUnionDriver.Message.BlackListError(verify))

#####################################
#             TypedVerify           #
#####################################

@DiscordDriver.command()
async def 네(message):
    if message.channel.type.name == "text":
        return None

    if not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is not Staff")
        return None

    if ClanUnionDriver.Status == "BlackUserVerify":
        ClanUnionDriver.Sheet.UpdateBlackListSheet(ClanUnionDriver.ListedBlackUser())

        src = ClanUnionDriver.BlackUser.Source
        admins = Config['AdminUserDiscord']
        url = Config['GoogleSheet']['URL']
        msg = ClanUnionDriver.Message.BlackListUpdate(src, admins, url)

        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" was "+ClanUnionDriver.Status+" accepted")
        await ClanUnionDriver.BlackListChannel.send(ClanUnionDriver.Message.BlackListSpread(ClanUnionDriver.BlackUser, url))
        await message.channel.send(msg)

        ClanUnionDriver.Status = ""
        ClanUnionDriver.BlackUserReset()

        return None
    
    elif ClanUnionDriver.Status == "MemberListVerify":
        ClanUnionDriver.MemberList.Save()
        ClanUnionDriver.Sheet.UpdateClanListSheet()

        src = ClanUnionDriver.MemberList.Name
        admins = Config['AdminUserDiscord']
        url = Config['GoogleSheet']['URL']
        msg = ClanUnionDriver.Message.MemberListUpdate(src, admins,url)

        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" was "+ClanUnionDriver.Status+" accepted")
        await ClanUnionDriver.MemberListChannel.send(ClanUnionDriver.Message.MemberListSpread(ClanUnionDriver.MemberList, url))
        await message.channel.send(msg)

        ClanUnionDriver.Status = ""
        ClanUnionDriver.MemberListReset()

        return None

    # EasterEgg
    await message.channel.send("네? ^^;;")

@DiscordDriver.command()
async def 아니요(message):
    if message.channel.type.name == "text":
        return None

    if not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is not Staff")
        return None

    if ClanUnionDriver.Status :
        ClanUnionDriver.BlackUserReset()
        ClanUnionDriver.Status = ""
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" was "+ClanUnionDriver.Status+" denied")
        await message.channel.send(ClanUnionDriver.Message.VerifyDeny)

        return None

    # EasterEgg
    await message.channel.send("네? ㅁ..무엇이 아닌가요? ^^;;")

#####################################
#                Help               #
#####################################

@DiscordDriver.command()
async def 블랙리스트(message):
    if message.channel.type.name == "text":
        return None

    if not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is not Staff")
        return None

    Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is helping BlackList")
    await message.send(ClanUnionDriver.Message.BlackListHelp)

@DiscordDriver.command()
async def 클랜원명단(message):
    if message.channel.type.name == "text":
        return None

    if not ClanUnionDriver.IsStaff(message):
        await message.channel.send(ClanUnionDriver.Message.IDKYou(Config['Discord']['Channel']['StaffNotify']))
        Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is not Staff")
        return None

    Logger.info("[*] "+message.author.name + "#" + message.author.discriminator+" is helping MemberList")
    await message.send(ClanUnionDriver.Message.MemberListHelp)    

#####################################
#                Run.               #
#####################################

if __name__ == "__main__":
    DiscordDriver.run(Config['Discord']['Token'])