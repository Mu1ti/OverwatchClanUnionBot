import json

def SetPath(argv):
    result = "conf.json"
    
    if len(argv) > 2:
        result = argv[1]
    
    return result
 
def Import(argv):
    result = None
    path = SetPath(argv)

    with open(path, 'r', encoding='utf8') as Config:
        result = json.loads(Config.read())

    return result