import subprocess
import re

class Mpc:
    def __init__(self):
       self.actualPlayedStation = None

    def mpcCommand(self, cmd):
        p = subprocess.Popen(['mpc'] + cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        r = p.stdout.read()
        return r

    def play(self, webRadio):
        self.actualPlayedStation = webRadio
        self.clear()
        self.addStation(webRadio.url)
        self.mpcCommand(["play"])

    def stop(self):
        self.actualPlayedStation = None
        self.mpcCommand(["stop"])

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

    def getActualPlayedStation(self):
        if self.actualPlayedStation is not None:
            return self.actualPlayedStation
        else:
            return ""