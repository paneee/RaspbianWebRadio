# RaspbianWebRadio

Raspbian Web Radio is a web application created in Flask technology using mpc player (minimalist command line interface to MPD). Originally run on the rasbian system on the rasberry platform. 


## Commissioning

```bash
git clone https://github.com/paneee/RaspbianWebRadio.git
cd RaspbianWebRadio
python3 app.py
```

## Dependencies

```bash
flask
flask-bootstrap4
flask_restful
flask_cors
```

## Usage

Listenable radio stations are in the model.py file in the WebRadio dictionary variable, you can add more...
In the example the server runs on a raspberry pi 3. (ip 192.168.1.50 port 5000)

### Web page

![2021-09-23_150724](https://user-images.githubusercontent.com/27755739/134512421-616ced2f-4f28-41f9-af02-3ee741de101d.png)


### Web API - Available commands

Returns all possible stations.
```bash
192.168.1.50:5000/api/getAllStation
```

Returns the current volume.
```bash
192.168.1.50:5000/api/getVolume
```

Increases the volume by 15%. To decrease, enter the argument -15.
```bash
192.168.1.50:5000/api/setVolume/+15
```

Sets volume to 40.
```bash
192.168.1.50:5000/api/setVolume/40
```

Sets the station being played back to RNS. List of available stations in the file radio.py.
```bash
192.168.1.50:5000/api/Play/RNS
```

Stop playing a station.
```bash
192.168.1.50:5000/api/Stop
```

Speaker On / Off.
```bash
192.168.1.50:5000/api/speakerOnOff/
```

Speaker volume UP.
```bash
192.168.1.50:5000/api/speakerVolumeUP/
```

Speaker volume DOWN.
```bash
192.168.1.50:5000/api/speakerVolumeDOWN/
```
