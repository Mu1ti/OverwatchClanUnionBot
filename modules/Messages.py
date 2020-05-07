from modules import Util

def BlackListUpdate(source, adminUserDiscord, documentURL):
    result = Util.MessageContent('BlackListUpdate').format(source, ', '.join(adminUserDiscord), documentURL)
    return result 

def BlackListVerify(blackUser):
    result = Util.MessageContent('BlackListVerify').format(Util.BlackUserToText(blackUser))
    return result 

def BlackListSpread(blackUser, documentURL):
    result = Util.MessageContent('BlackListSpread').format(blackUser.Source, Util.BlackUserToText(blackUser), documentURL)
    return result 

def BlackListError(error):
    result = Util.MessageContent('BlackListError').format(error)
    return result

def MemberListVerify(memberList):
    result = Util.MessageContent('MemberListVerify').format(memberList)
    return result 

def MemberListUpdate(source, adminUserDiscord, documentURL):
    result = Util.MessageContent('MemberListUpdate').format(source, ', '.join(adminUserDiscord), documentURL)
    return result

def MemberListSpread(memberList, documentURL):
    result = Util.MessageContent('MemberListSpread').format(memberList.Name, memberList.Update, len(MemberList.Members), documentURL)
    return result

def IDKYou(channelName):
    result = Util.MessageContent('IDKYou').format(channelName)
    return result


BlackListHelp = Util.MessageContent('BlackListHelp')
MemberListHelp = Util.MessageContent('MemberListHelp')

VerifyDeny = Util.MessageContent('VerifyDeny')