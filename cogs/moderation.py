import nextcord as discord
from discord.colour import Color
from discord.ext import commands
from discord.ext.commands.core import command, has_permissions

class moderation(commands.Cog, name='moderation'):
    def __init__(self, bot):
        self.bot = bot

    ## CLEAR
    @commands.command(aliases=['c'], description= 'clears messages, only people who has the "manage messages" perm can use this. ')
    @commands.has_guild_permissions(manage_messages = True)
    async def clear(self, ctx,amount=2):
        await ctx.channel.purge(limit = amount)

    ## KICK
    @commands.command(aliases=['k'], description= 'kicks specified member. only people with "kick_members" perm can use this. ')
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self,ctx, member : discord.Member,*,reason= "No reason provided"):
        try:
            await member.send("You've been kicked from ORiON, my guess: you were naughty. Oh! Here's the real reason: "+reason)
        except:
           await ctx.send("The member you mentioned has their dms closed.")
        await member.kick(reason=reason)


    ## BAN
    @commands.command(aliases=['b'], description= 'bans specified member. only people with "ban_members" perm can use this. ')
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self,ctx, member : discord.Member,*,reason= "No reason provided"):

        await member.send("You've been banned from ORiON, my guess: you were *real* naughty. Oh! Here's the real reason: "+reason)
        await member.ban(reason=reason)


    ## UNBAN
    @commands.command(aliases=['ub'], description= 'unbans specified member. only people with "ban_members" perm can use this. ')
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator)==(member_name,member_disc):

                await ctx.guild.unban(user)
                await ctx.send(member_name + " has been unbanned! good job")
                return


    ## MUTE
    @commands.command(aliases=['m'], description= 'mutes specified member. only people with "kick_members" perm can use this. ')
    @commands.has_guild_permissions(kick_members=True)
    async def mute(self,ctx, member : discord.Member,*,reason="No reason provided"):
        muted_role = ctx.guild.get_role(880016735980363785)

        await member.add_roles(muted_role)
        await ctx.send(member.mention + " has been muted.")


    ## UNMUTE
    @commands.command(aliases=['um'], description= 'unmutes specified member. only people with "kick_members" perm can use this. ')
    @commands.has_guild_permissions(kick_members=True)
    async def unmute(self,ctx,member : discord.Member,*,reason= "No reason provided"):
        muted_role = ctx.guild.get_role(880016735980363785)

        await member.remove_roles(muted_role)
        await ctx.send(member.mention + " has been unmuted.")

    
    ## WHOIS
    @commands.command(aliases=['info', 'user', 'userinfo'], description= 'tells you the information of the user mentioned.')
    @commands.has_guild_permissions(kick_members=True)
    async def whois(self, ctx, member : discord.Member):
        created_at = member.created_at.strftime("%b %d, %Y")
        roles = [role for role in member.roles]

        embed = discord.Embed(title = member.name, description= member.mention, Color= discord.Color.green )
        embed.add_field(name = "ID", value = member.id, inline= True)
        embed.add_field(name = 'account created at', value= created_at)
        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.set_thumbnail(url= member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

    ## SERVERINFO
    @commands.command(aliases=['si','sinfo'], description='tell you the curent information of the server')
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
   
        embed = discord.Embed(
              title=name + " Server Information",
              description=description,
              color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))

    ## UNMUTE
    @commands.command(aliases=['um'], description= 'unmutes specified member. only people with "kick_members" perm can use this. ')
    @commands.has_guild_permissions(kick_members=True)
    async def unmute(self,ctx,member : nextcord.Member,*,reason= "No reason provided"):
        muted_role = ctx.guild.get_role(880016735980363785)

        await member.remove_roles(muted_role)
        await ctx.send(member.mention + " has been unmuted.")

    
    ## WHOIS
    @commands.command(aliases=['info', 'user', 'userinfo'], description= 'tells you the information of the user mentioned.')
    @commands.has_guild_permissions(kick_members=True)
    async def whois(self, ctx, member : nextcord.Member):
        created_at = member.created_at.strftime("%b %d, %Y")
        roles = [role for role in member.roles]

        embed = nextcord.Embed(title = member.name, description= member.mention, Color= discord.Color.green )
        embed.add_field(name = "ID", value = member.id, inline= True)
        embed.add_field(name = 'account created at', value= created_at)
        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.set_thumbnail(url= member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text = f'Requested by {ctx.author.name}')
        await ctx.send(embed=embed)

    ## SERVERINFO
    @commands.command(aliases=['si','sinfo'], description='tell you the curent information of the server')
    async def serverinfo(self,ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
   
        embed = nextcord.Embed(
              title=name + " Server Information",
              description=description,
              color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))
