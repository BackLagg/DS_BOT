from discord.ext import commands
import config

bot = commands.Bot(command_prefix=config.NULLPREF)


@bot.event
async def on_ready():
    print('Bot logged as {}'.format(bot.user))



@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.command()
async def Hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def Hi(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def hi(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def Hello_everyone(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def Hello_9S(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
async def Bye(ctx):
    author = ctx.message.author
    await ctx.send(f'See you soon, {author.mention}!')

@bot.command()
async def Goodbye(ctx):
    author = ctx.message.author
    await ctx.send(f'See you soon, {author.mention}!')

@bot.command()
async def Goodbye_everyone(ctx):
    author = ctx.message.author
    await ctx.send(f'See you soon, {author.mention}!')

@bot.command()
async def info(ctx):
    await ctx.send('Привет, я бот поддержки 9S модель - S.\n'
                   'Для подробной информации о моих функциях напишите:\n'
                   '\n'
                   '\t--commands\n'
                   '\t--admin_help\n'
                   '\n'
                   'Удачного для ;-)')

bot.run(config.TOKEN)