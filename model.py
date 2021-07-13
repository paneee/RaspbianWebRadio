from json import JSONEncoder

class WebRadio:
    def __init__(self, Name, Url, IsPlaying):
        self.name = Name
        self.url = Url
        self.isPlaying = IsPlaying

class WebRadioEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

WebRadiosList = []

WebRadiosList.append(WebRadio("ChiliZet","https://ch.cdn.eurozet.pl/chi-net.mp3",False))
WebRadiosList.append(WebRadio("Radio 357","https://n06a-eu.rcs.revma.com/ye5kghkgcm0uv?rj-ttl=5&rj-tok=AAABduJfGVcAbh2i1fQT0iMZcA",False))
WebRadiosList.append(WebRadio("Radio Nowy Swiat","https://stream.nowyswiat.online/aac",False))
WebRadiosList.append(WebRadio("Record Chillout","http://air2.radiorecord.ru:805/chil_aac_64",False))
WebRadiosList.append(WebRadio("Radio Kampus","http://193.0.98.66:8005/",False))
WebRadiosList.append(WebRadio("Weszlo FM","http://radio.weszlo.fm/s7d70a7895/listen",False))
WebRadiosList.append(WebRadio("PR3 Trojka","http://stream3.polskieradio.pl:8904",False))
WebRadiosList.append(WebRadio("Radio Kraków", "http://panel.nadaje.com:9160/radiokrakow.aac",False))
WebRadiosList.append(WebRadio("Radiofonia", "https://rs101-krk-cyfronet.rmfstream.pl/radiofonia",False))


