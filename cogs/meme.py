import discord 
from discord.ext import commands
from PIL import Image,ImageFont,ImageDraw

class meme(commands.Cog, name='memes'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['tf'])
    async def throwfire(self, ctx,*, text = "sample text"):
        img = Image.open("firethrosponge.jpg")
        font = ImageFont.truetype("impact.ttf", 26)
        draw = ImageDraw.Draw(img)

        draw.text((75,175), text, (0,0,0), font=font)

        img.save("text.png")

        await ctx.send(file = discord.File("text.png"))

def setup(bot):
    bot.add_cog(meme(bot))