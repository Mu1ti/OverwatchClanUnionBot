def AddBlackList(self):
    return MessageContent('BlackListHelp')

def AddMemberList(self):
    return MessageContent('MemberListHelp')

def MessageContent(messageName):
    result = ''
    with open('messages/'+messageName,'r', encoding='utf8') as messageFile :
        result = messageFile.read()

    return result