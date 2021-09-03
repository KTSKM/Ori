import discord
from discord.ext import commands
from itertools import cycle

filtered_words = ["nigger", "whore", "tranny", "terrorist", "chink", "faggot", "nword", "nigga", "ching", "chong", "chingchong", "nig", "niger", "slut", "retarded", "retard", "nigtard", "fagtard", "sissy"]

bot = commands.Bot(command_prefix='ori!')

status = cycle(
    ['Try ori!help','Prefix - ori!'])

### EVENTS #############    
@bot.event
async def on_ready():
    print("bot is ready v2.5")
 
@bot.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
    
    if "69" in msg.content:
        await msg.add_reaction("<:smug_ori:881561648907833354>")
    if "420" in msg.content:
        await msg.add_reaction("<:smug_ori:881561648907833354>")

    await bot.process_commands(msg)


### ERROR HANDLING ###
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.reply("You cant do that dummy!")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("You're forgetting something... \n ||(Hint: try saying ori!help <the command you just said>)|| ")
        await ctx.message.delete()
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.reply("Thats not a command dumdum")
    elif isinstance(error, commands.errors.CommandOnCooldown):
        await ctx.reply("I know you wanna go on a date with me that much, but please let me rest a little!")
        await ctx.send("<:poutori:883284813220577300>")
    else:
        await ctx.reply("something went wrong. \n Please wait until kermoa is active, and send the screenshot of the bug")
        raise error

## if ur gonna add a category, make the python file in cogs, and add it here
initial_extensions = ['cogs.moderation', 'cogs.ORiON','cogs.Extra', 'cogs.fun'] 

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run('ODgyNDU1MTE1MjQ2NzM5NDc2.YS7oXg.v_5aza8iHbkJNEc_DrN_8S_BHhA', bot=True, reconnect=True)
