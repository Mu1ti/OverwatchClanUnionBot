import json

def Config(argv):
    result = None
    path = setPath(argv)

    with open(path, 'r', encoding='utf8') as Config:
        result = json.loads(Config.read())

    return result

def setPath(argv):
    result = "conf.json"
    
    if len(argv) > 2:
        result = argv[1]
    
    return result