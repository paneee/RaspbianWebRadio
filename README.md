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
```

## Usage

Listenable radio stations are in the model.py file in the WebRadio dictionary variable, you can add more...
In the example the server runs on a raspberry pi 3. (ip 192.168.1.50 port 5000)

### Web page

![2021-07-03_191433](https://user-images.githubusercontent.com/27755739/124363168-067cfb00-dc3a-11eb-96bb-debc0d124c9d.png)


### Web API

Available commands

```bash
192.168.1.50:5000/api/getAllStation
```

```bash
192.168.1.50:5000/api/getVolume
```

```bash
192.168.1.50:5000/api/setVolume/+15
```

```bash
192.168.1.50:5000/api/setVolume/+15
```

```bash
192.168.1.50:5000/api/Play/RNS
```

```bash
192.168.1.50:5000/api/Stop
```
