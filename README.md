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
flask-bootstrap4

```

## Usage

In the example the server runs on a raspberry pi 3. (ip 192.168.1.50 port 5000)

### Web page
![2021-07-03_191433](https://user-images.githubusercontent.com/27755739/124362448-252cc300-dc35-11eb-99e7-e34ed6e5ff51.png)


### Web API

Available commands
```bash
192.168.1.50:5000/api/getAllStation
192.168.1.50:5000/api/getVolume
192.168.1.50:5000/api/setVolume/+15
192.168.1.50:5000/api/Play/RNS
192.168.1.50:5000/api/Stop
```
