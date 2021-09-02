import discord 
from discord.ext import commands

class fun(commands.Cog, name='fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gj'], description="compliment me ples")
    async def goodjob(self,ctx):
        await ctx.send("<:smug_ori:881561648907833354>")
        await ctx.send('thank you')

    @commands.command(aliases=['hp'], description="hedpat me ples")
    async def headpat(self,ctx):
        await ctx.send("<a:headpat:882837248146554941>")
        await ctx.send('thank you beri much')
        
    ## POLL
    @commands.command(aliases=['pl'], description="creates a poll")
    async def poll(self, ctx,*,msg):
        channel = ctx.channel
        try:
            op1 , op2 = msg.split("or")
            txt = f"React with ✅ for {op1}, or ❌ for {op2} "
        except:
            await channel.send("Correct Sytax: [Choice] or [Choice2]")
            return
        
        embed = discord.Embed(title="Poll", description = txt,color = discord.Colour.red())
        message_ = await channel.send(embed=embed)
        await message_.add_reaction("✅")
        await message_.add_reaction("❌")
        await ctx.message.delete()

        
def setup(bot):
    bot.add_cog(fun(bot))