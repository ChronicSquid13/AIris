import discord
from discord.ext import commands

class EchoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = 1338990268648521891  # Channel ID for "airis"

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself to prevent loops
        if message.author.bot:
            return
        
        # Check if the message is in the "airis" channel
        if message.channel.id == self.channel_id:
            await message.channel.send(message.content)

async def setup(bot):
    await bot.add_cog(EchoCog(bot))
