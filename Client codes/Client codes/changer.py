import discord
from discord import GuildSubscriptionOptions
import asyncio
from random import randint

limit = 24

class MainClient(discord.Client):
    def __init__(self, serial,**kwargs):
        super().__init__(**kwargs)
        self.serial = serial

    async def on_ready(self):
        print("Logged in as", self.user)
        await asyncio.sleep(randint(1, 10))
        with open(f'avatars/{self.serial % limit + 1}.png', 'rb') as avatar:
            await self.user.edit(avatar=avatar.read())
        print("Changed avatar for", self.user)
        await self.close()
        print("Logged out from", self.user)

with open('tokens.txt', 'r') as tokenfile:
    tokens = [i.split(':') for i in tokenfile.read().split()]

loop = asyncio.get_event_loop()

for i in range(len(tokens)):
    token = tokens[i]
    bot = MainClient(i, max_messages=0, chunk_guilds_at_startup=False, guild_subscription_options=GuildSubscriptionOptions.off())
    loop.create_task(bot.start(token))

try:
    loop.run_forever()
finally:
    print("Closing all bots!")
    loop.stop()