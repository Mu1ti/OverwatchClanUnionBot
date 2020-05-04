import json, sys, discord, asyncio, logging

from discord.ext import commands

from modules import Config
from modules import Messages
from modules.BlackUser import BlackUser
from modules.CtlSheet import CtlSheet

global Status 
global TargetBlackUser

Config = Config.Import(sys.argv)
DiscordDriver = commands.Bot(command_prefix='')
SheetDriver = CtlSheet(Config['GoogleSheet'])
TargetBlackUser = BlackUser()

@DiscordDriver.event
async def on_ready():
    print("[*] Start ClanUnionBot")
    logging.info('Start ClanUnionBot')

@DiscordDriver.command()
async def test(message):
    await message.send("What Do You Want To Test?")

@DiscordDriver.command()
async def 네(message):
    global Status 
    global TargetBlackUser

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

    TargetBlackUser = BlackUser()
    await message.send(Messages.VerifyDeny)

@DiscordDriver.command()
async def 본계정(message):
    global Status 
    global TargetBlackUser

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
    if "추가" in message.message.content:
        sendMessage = Messages.BlackListHelp
        await message.send(sendMessage)
        
if __name__ == "__main__":
    DiscordDriver.run(Config['Discord']['Token'])