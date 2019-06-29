from discord.ext import commands
import discord
import music

TOKEN = 'NTkzOTM4NTU5OTk2Nzg4NzY2.XRVKxg.G3zzPadn-m1tKgEGyfeLfDhSrSk'

description = '''metalbot QwQ'''
bot = commands.Bot(command_prefix='~', description=description)

print('wtf')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


COGS = [music.Music]


def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot))

add_cogs(bot)
bot.run(TOKEN)

