import time
import json
import discord
from discord.ext import commands

description = '''Gives out bytes for activity, which can turn into ranks, such as kb, mb, gb, etc'''
startup_extensions = ['roles'] #Extensions that will be loaded when the bot is started
bot_prefix = '$' #Bot prefix

bot = commands.Bot(command_prefix=bot_prefix, description=description)

@bot.event
async def on_ready():
    print('Byte Rank Bot logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

'''
@bot.event
async def on_message(message):
    with open('data/bytes.json', 'r') as bytes_file_r:
        bytes_data = json.load(bytes_file_r)
    bytes_to_add = 0
    for char in message.content:
        bytes_to_add = bytes_to_add + 1
    bytes_data[message.author.id] = bytes_data[message.author.id] + bytes_to_add
    with open('data/bytes.json', 'w') as bytes_file_w:
        json.dump(bytes_data, bytes_file_w)'''




@bot.command(hidden=True)
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension('lib.' + extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("Extension `{}` has been loaded.".format(extension_name))

@bot.command(hidden=True)
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("Extension `{}` has been unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension('lib.' + extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run('')
