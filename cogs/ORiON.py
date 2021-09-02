import discord
from discord.ext import commands

class ORiON(commands.Cog, name='ORiON'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(description= "Tells you how to join ORiON!")
    async def join(self, ctx):
        embed=discord.Embed(title="read the pinned message at announcements u dumdum", url="https://discord.com/channels/880016735980363776/880036716377948190/880497534357864558", description="u didn't read the rules didn't u")
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(ORiON(bot))