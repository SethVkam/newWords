import discord
import _json
from discord.ext import commands

bot = commands.Bot("prefix")

@bot.command(name="go")

from.bot_logic import gen_pass

bot = discord.Bot(intents=intents)

intents = discord.Intents.default()
intents.message_content = True

bot = discord.bot(intents=intents)

@bot.command
async def on_ready():
    print(f'We have logged in as {bot.user}')

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

elements = "+-/*!&$#?=@<>"
password = ""
pass_length = int(input("Enter pass length: "))

for i in range(pass_length):
    password += random.choice(elements)

print(password)

@bot.command
async def on_ready():
    print(f'We have logged in as {bot.user}')

bot.run("MTEwNzIxMjk2ODQzMDY2NTgyOQ.GMCVca.9RrsiSeuvFAuV4dL71GhdRmBkWIRoTl4gdtIYQ")
