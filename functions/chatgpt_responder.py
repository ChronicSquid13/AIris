import discord
from discord.ext import commands
import openai
import json

class ChatGPTResponder(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config
        self.openai_api_key = self.config.get("openai_api_key")
        openai.api_key = self.openai_api_key
        self.allowed_channel_id = 1338990268648521891  # Channel ID for "airis"

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself to prevent loops
        if message.author.bot:
            return
        
        # Check if the message is in the "airis" channel
        if message.channel.id != self.allowed_channel_id:
            return
        
        # Start typing indicator
        async with message.channel.typing():
            # Get response from ChatGPT
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message.content}],
                    max_tokens=150
                )
                reply = response.choices[0].message['content'].strip()
            except Exception as e:
                reply = f"Error: {str(e)}"
        
        # Send the response back to the channel
        await message.channel.send(reply)

async def setup(bot):
    config = bot.config
    await bot.add_cog(ChatGPTResponder(bot, config))
