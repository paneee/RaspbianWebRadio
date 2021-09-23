import subprocess
import re

from rpi.radio import WebRadios

class Mpc:
    def __init__(self):
       self.actualPlayedStation = None
       self.webRadios = WebRadios()

    # MPC player command
    def mpcCommand(self, cmd):
        p = subprocess.Popen(['mpc'] + cmd, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        r = p.stdout.read()
        return r

    def play(self, webRadio):
        self.clear()
        self.addStation(webRadio.url)
        self.mpcCommand(["play"])
        self.webRadios.setPlaying(webRadio)

    def stop(self):
        self.mpcCommand(["stop"])
        self.webRadios.setStoped()

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

