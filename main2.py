mport discord
import os
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)



#animals_mem
@bot.command()
async def animals1(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)

@bot.command()
async def animals2(ctx):
    with open('images/mem4.jpg', 'rb') as f:
        picture = discord.File(f)

@bot.command()
async def animals3(ctx):
    with open('images/mem5.jpg', 'rb') as f:
        picture = discord.File(f)



#mem
@bot.command()
async def mem2(ctx):
    with open('images/mem2.jpg', 'rb') as f:
        picture = discord.File(f)


@bot.command()
async def mem3(ctx):
    with open('images/mem3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('images/mem3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem4(ctx):
    with open('images/7f2eeac26d68474f02ef41b17969816b.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem5(ctx):
    with open('images/edc7114df6657af2fab443c901dc9166.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f'Привет! Я бот {bot.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)



@bot.command()
async def help_me(ctx):
    await ctx.send("префикс $")
    await ctx.send("команды mem1, mem2, mem3 и т.д. вызывают мем по программированию")
    await ctx.send("команды animals1, animals2, animals3 мемы по программированию с животными")
    await ctx.send("команда heh нужна для спама в чат")

print random.choice(os.listdir('images'))

bot.run("MTEwNzIxMjk2ODQzMDY2NTgyOQ.G04gRS.uBV4kZVs-BFj4x5B9z1TfIwZXcE6OQQ8UIXxeQ")
