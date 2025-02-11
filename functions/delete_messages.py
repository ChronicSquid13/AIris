import discord
from discord.ext import commands

class DeleteMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name='delete', description='Delete all messages in this channel')
    async def delete(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge()
        feedback_message = await interaction.followup.send('All messages have been deleted.', ephemeral=True)
        
        # Wait for 5 seconds, then delete the feedback message
        await discord.utils.sleep_until(discord.utils.utcnow() + discord.utils.timedelta(seconds=5))
        await feedback_message.delete()

async def setup(bot):
    await bot.add_cog(DeleteMessages(bot))
