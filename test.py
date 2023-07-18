import discord
import os
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        os.system('clear')
    async def on_message(self, message):
        print(f'{message.author}: {message.content}')
        if (message.author != self.user):
            if '🦦' in message.content:
                await message.channel.send("🦦")
            elif 'kill otters' in message.content:
                spamMessage = random.randint(0, 10)
                while(spamMessage > 0):
                    await message.channel.send("# " + message.author.mention + " Please don't 🦦")
                    spamMessage = spamMessage - 1
            elif 'I hate otters' in message.content:
                await message.channel.send("# " + message.author.mention + " I know where you live 🦦")
            elif 'I hate' in message.content:
                await message.channel.send("# You hate? 🦦")
            elif 'otter' in message.content:
                await message.channel.send("# Hi 🦦")
            elif 'go away' in message.content:
                await message.channel.send("# " + message.author.mention + " I know where you live 🦦")
            elif 'cat' in message.content:
                await message.channel.send("# Otters are better 🦦")
            elif 'kitty' in message.content:
                await message.channel.send("# Otters are better 🦦")
            elif 'kitties' in message.content:
                await message.channel.send("# Otters are better 🦦")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('')
