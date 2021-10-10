from discord.ext import commands
import config

client = commands.Bot(command_prefix=config.PREF)

@client.command()
async def commands(ctx):
    await ctx.send('Моя модель ещё не доработана, данная команда пока не доступна...')

@client.command()
async def admin_help(ctx):
    await ctx.send('Моя модель ещё не доработана, данная команда пока не доступна...')


client.run(config.TOKEN)