import discord
from app import _mpc
from app import _speaker

class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if str(message.author) == 'panee#9393':
            if message.content == 'Ping':
                await message.channel.send('pong')

            if message.content == 'Volume':
                await message.channel.send(_mpc.getVolume())

            if message.content == 'VolumeUP':
                _mpc.volumeChange('+10')
                await message.channel.send(_mpc.getVolume())

            if message.content == 'VolumeDOWN':
                _mpc.volumeChange('-10')
                await message.channel.send(_mpc.getVolume())

            if message.content == 'SpeakerOnOff':
                _speaker.OnOff()
                await message.channel.send('OK')

            if message.content == 'SpeakerOnOff':
                _speaker.OnOff()
                await message.channel.send('OK')


def readDiscordTokenFromFile():
    with open('/home/pi/RaspbianWebRadio/rpi/token.txt') as f:
        token = f.readline()
    return token






