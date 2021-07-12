import subprocess
import re
from model import WebRadiosList

class Mpc:
    def __init__(self):
       self.actualPlayedStation = None

    def mpcCommand(self, cmd):
        p = subprocess.Popen(['mpc'] + cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        r = p.stdout.read()
        return r

    def play(self, webRadio):
        self.clear()
        self.addStation(webRadio.url)
        self.mpcCommand(["play"])
        ret = WebRadiosList
        for item in ret:
            item.isPlaying = False
        for item in ret:
            if webRadio.name == item.name and webRadio.url == item.url:
                item.isPlaying = True 
        return ret

    def stop(self):
        self.mpcCommand(["stop"])
        ret = WebRadiosList
        for item in ret:
            item.isPlaying = False
        return ret

    def clear(self):
        self.mpcCommand(["clear"])

    def addStation(self, url):
        self.mpcCommand(["add", url])

    def getVolume(self):
        ret = self.mpcCommand(["volume"])
        string = str(ret)
        table = re.split(':|%', str(ret))
        return table[1]   

    def volumeChange(self, arg):
        self.mpcCommand(["volume", arg])
