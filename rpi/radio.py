from json import JSONEncoder

class WebRadio:
    def __init__(self, Name, Url, IsPlaying):
        self.name = Name
        self.url = Url
        self.isPlaying = IsPlaying

class WebRadioEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class WebRadios:
    def __init__(self): 
        self.WebRadiosList = []
        self.WebRadiosList.append(WebRadio("ChiliZet","https://ch.cdn.eurozet.pl/chi-net.mp3",False))
        self.WebRadiosList.append(WebRadio("Radio 357","https://n06a-eu.rcs.revma.com/ye5kghkgcm0uv?rj-ttl=5&rj-tok=AAABduJfGVcAbh2i1fQT0iMZcA",False))
        self.WebRadiosList.append(WebRadio("Radio Nowy Swiat","https://stream.nowyswiat.online/aac",False))
        self.WebRadiosList.append(WebRadio("Record Chillout","http://radiorecord.hostingradio.ru/chil96.aacp",False))
        self.WebRadiosList.append(WebRadio("Radio Kampus","http://193.0.98.66:8005/",False))
        self.WebRadiosList.append(WebRadio("Weszlo FM","http://radio.weszlo.fm/s7d70a7895/listen",False))
        self.WebRadiosList.append(WebRadio("PR3 Trojka","http://stream3.polskieradio.pl:8904",False))    
        self.WebRadiosList.append(WebRadio("Radio Kraków", "http://panel.nadaje.com:9160/radiokrakow.aac",False))
        self.WebRadiosList.append(WebRadio("Radiofonia", "https://rs101-krk-cyfronet.rmfstream.pl/radiofonia",False))

    def getAll(self):
        return self.WebRadiosList

    def getPlaying(self):
        ret = ''
        for item in self.WebRadiosList:
            if item.isPlaying == True:
                ret = item
        return ret

    def setPlaying(self, radio):
        for item in self.WebRadiosList:
            item.isPlaying = False
        for item in self.WebRadiosList:
            if radio.name == item.name and radio.url == item.url:
                item.isPlaying = True 

    def setStoped(self):
        for item in self.WebRadiosList:
            item.isPlaying = False

    def fromName(self, radioName):
        radio = ''
        for item in self.WebRadiosList:
            if item.name == radioName:
                radio = item
                return radio

    def existName(self, radioName):
        ret = False
        for item in self.WebRadiosList:
            if item.name == radioName:
                ret = True
                return ret


