from model import WebRadiosList

def webRadioFromName(radioName):
    for item in WebRadiosList:
        if item.name == radioName:
            radio = item
            return radio