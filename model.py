from json import JSONEncoder

class WebRadio:
    def __init__(self, Name, Url):
        self.name = Name
        self.url = Url

class WebRadioEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__   

WebRadiosList = []

WebRadiosList.append(WebRadio("ChiliZet","https://ch.cdn.eurozet.pl/chi-net.mp3"))
WebRadiosList.append(WebRadio("357","https://n06a-eu.rcs.revma.com/ye5kghkgcm0uv?rj-ttl=5&rj-tok=AAABduJfGVcAbh2i1fQT0iMZcA"))
WebRadiosList.append(WebRadio("RNS","https://stream.nowyswiat.online/aac"))
WebRadiosList.append(WebRadio("Record Chillout","http://air2.radiorecord.ru:805/chil_aac_64"))
WebRadiosList.append(WebRadio("Radio Kampus","http://193.0.98.66:8005/"))
WebRadiosList.append(WebRadio("Weszlo","http://radio.weszlo.fm/s7d70a7895/listen"))
WebRadiosList.append(WebRadio("PR3 Trojka","mms://stream.polskieradio.pl/program3"))


