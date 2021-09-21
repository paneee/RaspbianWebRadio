import discord
from model import WebRadioEncoder, WebRadiosList
from mpc import Mpc

_mpc = Mpc()
_webRadioList = WebRadiosList

# Discord region
class DiscordClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Ping':
            await message.channel.send('pong')

        if message.content == 'Volume':
            await message.channel.send(_mpc.getVolume())

        if message.content == 'Radios':
            ret = WebRadioEncoder().encode(_webRadioList)
            await message.channel.send(ret)


def readDiscordTokenfromFile():
    with open('token.txt') as f:
        token = f.readline()
    return token


client = DiscordClient()

client.run(readDiscordTokenfromFile())

