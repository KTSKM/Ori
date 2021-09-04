import random
import nextcord
from nextcord.ext import commands

class Extra(commands.Cog, name='Extra'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description= 'Ill say hello back!')
    async def hello(self, ctx):
        await ctx.reply("Helloo! I'm your local best girl, Ori!")

    @commands.command(description= 'Adds two numbers')
    async def add(self, ctx, num1:int, num2:int):
        await ctx.reply(num1+num2)

    @commands.command(description= 'sends out a random number', aliases= ['randnum', 'rn'])
    async def randomnum(self, ctx, num1:int, num2:int):
        await ctx.reply(random.randrange(num1, num2))

def setup(bot):
        bot.add_cog(Extra(bot))
