import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ecology(ctx):
        await ctx.send("АБИОТИЧЕСКИЕ ФАКТОРЫ СРЕДЫ": "совокупность условий неорганической среды, влияющих на организмы")
        await ctx.send("АБРАЗИЯ": "разрушение берегов крупных водоемов волнами и прибоем")
        await ctx.send("АБСОРБЦИЯ": "поглощение вещества или энергии всей массой (объемом) поглощающего тела")
        await ctx.send("БИОГЕОЦЕНОЗ": "сложная природная система, объединяющая на основе обмена веществ и энергии совокупность живых организмов (биоценоз) с неживыми компонентами — условиями обитания; к живым компонентам биогеоценоза относятся автотрофные и гетеротрофные организмы")
        await ctx.send("БИОЦЕНОЗ": "совокупность популяции различных видов растений, животных и микроорганизмов, населяющих относительно однородное жизненное пространство")
        await ctx.send("ГЕНОФОНД": "1) совокупность генов (аллелей) одной группы особей (популяции, группы популяции или вида), в пределах которой они характеризуются определенной частотой встречаемости; 2) вся совокупность видов живых организмов с их проявившимися и потенциальными наследственными задатками")
        await ctx.send("ГУМУС": "перегной — органическая часть почвы, образующаяся в результате биохимического превращения растительных и животных остатков; содержание гумуса показатель плодородия почвы")
        await ctx.send("ОМНИЦИД — уничтожение всего живого на Земле. Может возникнуть как под воздействием естественных (например, общепланетарная или космическая катастрофа), так и антропогенных (мировая ядерная война, глобальная экологическая катастрофа и др.) факторов")
        await ctx.send("АБРАЗИЯ": "разрушение берегов крупных водоемов волнами и прибоем")

@bot.command()
async def mudrost(ctx):
     await ctx.send("Я тебе советую")
     
     words_list = ["Сортировать мусор по группам пластик в пластик стекло в стекло и т.д.", "Не бросать мусор в неположенных местах", "Экономить топливо", " Экономить воду"]
     
     random_word = random.choice(words_list)
     
     await ctx.send(random_word)

bot.run("token")
