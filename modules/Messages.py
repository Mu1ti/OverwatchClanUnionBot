from modules import Util

def BlackListUpdate(source, adminUserDiscord, documentURL):
    result = Util.MessageContent('BlackListUpdate').format(source, ', '.join(adminUserDiscord), documentURL)
    return result 

def BlackListVerify(blackUser):
    result = Util.MessageContent('BlackListVerify').format(Util.BlackUserToText(blackUser))
    return result 

def BlackListSpread(blackUser):
    result = Util.MessageContent('BlackListSpread').format(blackUser.Source, Util.BlackUserToText(blackUser))
    return result 

def BlackListError(error):
    result = Util.MessageContent('BlackListError').format(error)
    return result

def ClanMemberVerify(memberList):
    result = Util.MessageContent('BlackListVerify').format(memberList)
    return result 

def IDKYou(channelName):
    result = Util.MessageContent('IDKYou').format(channelName)
    return result


BlackListHelp = Util.MessageContent('BlackListHelp')
MemberListHelp = Util.MessageContent('MemberListHelp')

VerifyDeny = Util.MessageContent('VerifyDeny')