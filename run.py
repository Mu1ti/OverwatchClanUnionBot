import json, sys, discord, asyncio, logging

from discord.ext import commands

from modules import Config
from modules.BlackUser import BlackUser
from modules import Messages
from modules import CtlSheet

DiscordDriver = commands.Bot(command_prefix='')
SheetDriver = CtlSheet
Config = Config.Import(sys.argv)

@DiscordDriver.event
async def on_ready():
    print("[*] Start ClanUnionBot")
    logging.info('Start ClanUnionBot')

@DiscordDriver.command()
async def 본계정(message):
    # TODO
    # 블랙유저의 출처(Source를 추가해야 함)

    blackuser = BlackUser()
    content = message.message.content
    verify = blackuser.MessageFormVerify(content)

    if verify == True:
        blackuser.MessageFormPharse(content)
        pass

    else :
        warningMessage = "앗...! "+verify+"에 대한 내용이 잘못된 것 같습니다... ㅠㅠ\n없으면 \"없음\"으로라도 작성 부탁드립니다! :laughing:"
        await message.send(warningMessage)

@DiscordDriver.command()
async def 블랙리스트(message):
    if "추가" in message.message.content:
        sendMessage = Messages.AddBlackList
        await message.send(sendMessage)
        

if __name__ == "__main__":

    DiscordDriver.run(Config['Discord']['Token'])