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

![2021-07-03_191433](https://user-images.githubusercontent.com/27755739/124363168-067cfb00-dc3a-11eb-96bb-debc0d124c9d.png)


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

Sets the station being played back to RNS. List of available stations in the file model.py.
```bash
192.168.1.50:5000/api/Play/RNS
```

Stops playing a station.
```bash
192.168.1.50:5000/api/Stop
```
