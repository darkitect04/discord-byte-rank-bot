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

    @commands.command(pass_context=True)
    async def lur(self, ctx):
        embed = discord.Embed(type='rich', colour=16777215)
        embed.clear_fields()
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/207138942850564096/42e71a9c04a3dfc40c7f46d22f91b0b3.webp')
        embed.add_field(name='__**WELCOME**__', value='Hello, and welcome to the discord server for `LUReborn`. We are a group that is restoring LEGO Universe by creating a server emulator.')
        embed.add_field(name='__**RULES**__', value="• Use common sense\n• No advertising your discord server\n• Don't ask for a role\n• Don't spam\n• Be respectful\n• Keep chat safe for work")
        embed.add_field(name='__**CHANNEL**__', value='• <#283012262908788736> - Server information\n• <#207138942850564096> - General LEGO Universe chat\n• <#267483754119823361> - Non-LEGO Universe chat')
        embed.add_field(name='__**EMOTES**__', value='• <:imagination:283019209695428629> `:imagination:`\n• <:bob:283019959905288203> `:bob:`')
        await self.bot.say('', embed=embed)

def setup(bot):
    bot.add_cog(Roles(bot))
