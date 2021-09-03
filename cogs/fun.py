import asyncio
import random
import discord 
from discord.ext import commands
import PIL
from PIL import Image
from io import BytesIO

class fun(commands.Cog, name='fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['gj'], description="compliment me ples")
    async def goodjob(self,ctx):
        await ctx.send("<:smug_ori:881561648907833354>")
        await ctx.send('thank you')

    @commands.command(aliases=['hp'], description="hedpat me ples")
    async def headpat(self,ctx):
        await ctx.send("https://imgur.com/a/ZvuypPz.gif")
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

    @commands.command(aliases=['mw', 'wanted'], description='creates a wanted poster of yourself')
    async def mostwanted(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        
        wanted = Image.open("mostwanted.jpg")
        asset = user.avatar_url_as(size= 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((180,189))

        wanted.paste(pfp, (147,289))
        wanted.save("profile.jpg")

        await ctx.send(file = discord.File("profile.jpg"))

    @commands.command(aliases=['event','date'], description='Go on a date with me! \ncool down is 2 minutes')
    @commands.cooldown(1, 20, commands.BucketType.guild)
    async def datevent(self, ctx):
        await ctx.send(file = discord.File('DATEEVENT.jpg'))
        await asyncio.sleep(0.5)
        line = random.randrange(1,3)
        if line == 1:
            await ctx.send("私はあなたを愛しています、あなたは知っています！")
        elif line == 2:
            await ctx.send("I tried untying my hair today, what do you think?")
        else:
            await ctx.send("Looks like we’re the first ones! Erm... And we’re alone too... What would you like to do...?")

            
        
def setup(bot):
    bot.add_cog(fun(bot))
