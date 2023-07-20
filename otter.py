import discord
import os
import random
import asyncio
import aioconsole
import sys

async def get_user_input(self):
    while True:
        print("\n ")
        channelId = await aioconsole.ainput("[ MESSAGE TO ] ID > ")
        channel = self.get_channel(int(channelId))
        user_input = await aioconsole.ainput("> ")
        await channel.send("# 🦦 " + user_input + " 🦦 ")
        print("\n ")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        os.system('clear')
        asyncio.run(await get_user_input(self))
    async def on_message(self, message):
        print(f'[ MESSAGE FROM {message.channel.id} ] {message.author}: {message.content}')
        message.content = message.content.lower()
        if (message.author != self.user):
            if 'are you an otter' in message.content or 'actually an otter' in message.content or 'an actual otter' in message.content or 'are you real' in message.content:
                randMessage = random.randint(0,4)
                if(randMessage == 1):
                    await message.channel.send("# Yeah, I am an otter! 🦦")
                elif(randMessage == 2):
                    await message.channel.send("# Do I look like one? 🦦")
                elif(randMessage == 3):
                    await message.channel.send("# *otter noises* 🦦")
                else:
                    await message.channel.send("# Are you a human? 🦦")
            elif '🦦' in message.content:
                await message.channel.send("🦦")
            elif 'kill otters' in message.content or 'kill an otter' in message.content:
                spamMessage = random.randint(0, 10)
                while(spamMessage > 0):
                    await message.channel.send("# " + message.author.mention + " Please don't 🦦")
                    spamMessage = spamMessage - 1
            elif 'i hate otters' in message.content:
                await message.channel.send("# " + message.author.mention + " I know where you live 🦦")
            elif 'how are you' in message.content or 'cv' in message.content or 'ca va' in message.content:
                randMessage = random.randint(0,3)
                if (randMessage == 1):
                    await message.channel.send("# I'm quite sad today :( 🦦")
                else:
                    await message.channel.send("# I'm utterly fine >:D 🦦")
            elif "do you like" in message.content or "do you hate" in message.content or "do you dislike" in message.content or "do you love" in message.content:
                randMessage = random.randint(0,4)
                if(randMessage == 1):
                    await message.channel.send("# Yea! 🦦")
                elif(randMessage == 2):
                    await message.channel.send("# Uhm! 🦦")
                elif(randMessage ==3):
                    await message.channel.send("# Nah 🦦")
                else:
                    await message.channel.send("# I like cheese 🦦")
            elif "pic" in message.content or "picture" in message.content:
                randMessage = random.randint(0,4)
                if(randMessage == 1):
                    await message.channel.send("https://media.tenor.com/D64aeHA7tTEAAAAd/otter-pet.gif")
                elif(randMessage == 2):
                    await message.channel.send("https://media.tenor.com/9f0TeGj4fosAAAAd/otter-otters.gif")
                elif(randMessage == 3):
                    await message.channel.send("https://media.tenor.com/DImEWhsRqS0AAAAC/otter.gif")
                elif(randMessage == 4):
                    await message.channel.send("https://media.tenor.com/lLx2zqqmbOEAAAAS/otter-sleeping.gif")
                else:
                    await message.channel.send("# I'm too shy to send photos rn! 👉 👈 🦦")
            elif "i hate" in message.content or "i like" in message.content or "i dislike" in message.content or "i love" in message.content:
                randMessage = random.randint(0,4)
                if(randMessage == 1):
                    await message.channel.send("# Your tastes suck 🦦")
                elif(randMessage == 2):
                    await message.channel.send("# Me too 🦦")
                elif(randMessage == 3):
                    await message.channel.send("# What's that? 🦦")
                else:
                    await message.channel.send("# I'm literally an otter 🦦")
            elif 'otter' in message.content or 'hi' in message.content:
                randMessage = random.randint(1, 3)
                if(randMessage == 1):
                    await message.channel.send("https://imgur.com/uUBtUbu")
                else:
                    await message.channel.send("# Hi 🦦")
            elif 'go away' in message.content or 'fuck' in message.content or 'shut up' in message.content:
                hateMessage = random.randint(0,4)
                if(hateMessage == 1):
                    await message.channel.send("# " + message.author.mention + " I hate you 🦦")
                elif(hateMessage == 2):
                    await message.channel.send("# " + message.author.mention + " Stop being mean :( 🦦")
                elif(hateMessage == 3):
                    await message.channel.send("# " + message.author.mention + " Stop saying bad words 🦦")
                else:
                    await message.channel.send("# " + message.author.mention + " I know where you live 🦦")
            elif 'cat' in message.content or 'kitty' in message.content or 'kitties' in message.content:
                await message.channel.send("# Otters are better 🦦")
            else:
                randMessage = random.randint(1,14)
                if(randMessage == 1):
                    await message.channel.send("# Repeat what you just uttered 🦦")
                elif(randMessage == 2):
                    await message.channel.send("# My otter senses are tingling! 🦦")
                elif(randMessage == 3):
                    await message.channel.send("# I agree 🦦")
                elif(randMessage == 4):
                    await message.channel.send("# I disagree 🦦")
                elif(randMessage == 5):
                    await message.channel.send("# Perhaps 🦦")
                elif(randMessage == 6):
                    await message.channel.send("# Do you like Cheese? 🦦")
                elif(randMessage == 7):
                    await message.channel.send("# Nah, I don't like it too much 🦦")
                elif(randMessage == 8):
                    await message.channel.send("# What's a semiconducter? 🦦")
                elif(randMessage == 9):
                    await message.channel.send(message.author.mention)
                elif(randMessage == 10):
                    await message.channel.send("# Nope 🦦")
                elif(randMessage == 11):
                    await message.channel.send("# Did you know that otters utter? 🦦")
                elif(randMessage == 12):
                    await message.channel.send("# You are literally talking to an otter with predefined messages lol :3 I still think you are fren tho! 🦦")
                elif(randMessage == 13):
                    await message.channel.send("# I like you 🦦")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run('')
