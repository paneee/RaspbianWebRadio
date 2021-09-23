from gpiozero import LED
from time import sleep

# Define GPIO
Speaker_ON_OFF = LED(18)
Speaker_Vol_UP = LED(23)
Speaker_Vol_DOWN = LED(24)

class Speaker:
    def OnOff(self):
        Speaker_ON_OFF.off()
        Speaker_ON_OFF.on()
        sleep(3)
        Speaker_ON_OFF.off()

    def VolumeUP(self):
        Speaker_Vol_UP.off()
        Speaker_Vol_UP.on()
        sleep(0.7)
        Speaker_Vol_UP.off()

    def VolumeDOWN(self):
        Speaker_Vol_DOWN.off()
        Speaker_Vol_DOWN.on()
        sleep(0.7)
        Speaker_Vol_DOWN.off()

