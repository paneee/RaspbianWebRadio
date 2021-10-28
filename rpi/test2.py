from bluetoothctl import Bluetoothctl


_bluetoothctl = Bluetoothctl()

#_bluetoothctl.start_scan()
lista =   _bluetoothctl.get_available_devices()
print(lista)


