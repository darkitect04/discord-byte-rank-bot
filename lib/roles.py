import os
import json
import discord
from discord.ext import commands

class Roles():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def bytes(self, ctx, member : discord.Member=None):
    #Note: I tried to use an r+, w+ or an a+ but it didn't work for some odd reason.
        with open('data/bytes.json', 'r') as bytes_file_r:
            bytes_data = json.load(bytes_file_r)
        if member == None:
            memberid = ctx.message.author.id
        else:
            memberid = member.id
        try:
            bytes_data[memberid]
        except Exception as e: #This will probably literally never happen, unless this command is used on someone before they've even talked
            bytes_data[memberid] = 0
            with open('data/bytes.json', 'w') as bytes_file_w:
                json.dump(bytes_data, bytes_file_w)
        memberobj = ctx.message.server.get_member(memberid)
        embed = discord.Embed(type='rich', colour=memberobj.roles[-1].colour)
        embed.clear_fields()
        embed.set_author(name=memberobj.name, icon_url=memberobj.avatar_url)
        embed.add_field(name='Total', value=memberobj.name + ' has `' + str(bytes_data[memberid]) + '` bytes in total.')
        await self.bot.say('', embed=embed)

    @commands.command(pass_context=True)
    async def ranks(self, ctx):
        embed = discord.Embed(type='rich', colour=ctx.message.author.roles[-1].colour)
        embed.clear_fields()
        embed.add_field(name='**How It Works**', value='There are `6` ranks, `Kilobyte`, `Megabyte`, `Gigabyte`, `Terabyte`, `Petabyte` and `Exabyte`. You earn these ranks from sending messages, for each message you send you earn bytes based on the length of the message and your current rank, for each rank, byte earnings increase exponentionally. You cannot earn more than `15^r` (r being the number of your rank) bytes in one minute. The amounts needed for earning certains ranks are listed below.')
        embed.add_field(name='Kilobyte', value='Becoming a `Kilobyte` requires `1024` bytes.')
        embed.add_field(name='Megabyte', value='Becoming a `Megabyte` requires `1024` kilobytes.')
        embed.add_field(name='Gigabyte', value='Becoming a `Gigabyte` requires `1024` megabytes.')
        embed.add_field(name='Terabyte', value='Becoming a `Terabyte` requires `1024` gigabytes.')
        embed.add_field(name='Petabyte', value='Becoming a `Petabyte` requires `1024` terabytes.')
        embed.add_field(name='Exabyte', value='Becoming a `Exabyte` requires `1024` petabytes.')
        await self.bot.say('', embed=embed)

def setup(bot):
    bot.add_cog(Roles(bot))
