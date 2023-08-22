import discord
import pytz
from datetime import datetime
import config
import data
from  webserver import  keep_alive
from discord.ext import commands
from discord import utils



CHANNEL_ID = config.set.cid
# Создание объекта Intents и указание всех нужных опций
intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True
intents.guilds = True
intents.members = True

# Создание клиента Discord с указанными Intents
client = commands.Bot(command_prefix=config.set.prefix, intents=intents, case_insensitive=True)

@client.event
async def on_ready():
    print(f'Бот успешно подключился как {client.user}')
    await client.change_presence(activity=discord.Game(name=f"FoxiEnjoy | V 1.5.2"))

#Enjoy
@client.command()
async def randword(ctx):
    await ctx.send(f'Случайное слово: {data.rand.word}')

@client.command()
async def randnumb(ctx):
    await ctx.send(f'Случайное число: {data.rand.num}')

@client.command()
async def utc_time(ctx):
    city_name = 'UTC'
    try:
        # Проверяем, что название города является допустимым часовым поясом
        if city_name in pytz.common_timezones:
            # Получаем текущее время для указанного города
            timezone = pytz.timezone(city_name)
            current_time = datetime.now(timezone).strftime('%H:%M')

            # Отправляем информацию о текущем времени в текстовый канал
            await ctx.send(f'Сейчас {current_time} по UTC.')
        else:
            await ctx.send(f'Ой... В нашей системе произошла ошибка!')

    except Exception as e:
        await ctx.send(f'Ошибка: {e}')

@client.command()
async def fortune(ctx, vopros):
    await ctx.send(f'{data.rand.ynn}')

@client.command()
async def cat(ctx):
    my_image_id = data.rand.cat
    await ctx.send(file=discord.File(f'cats/{my_image_id}.jpg'))
#help
@client.command()
async def info(ctx):
    await ctx.send(f'Я - {client.user}.')
    await ctx.send(f'Версия: 1.5.2')
    await ctx.send(f'Разработчик: @foximay')
    await ctx.send(f'======================')
    await ctx.send(f'Поддержать разработчика: patreon.com/FoxiBot')
    await ctx.send(f'Пригласить меня: discord.com/api/oauth2/authorize?client_id=1130024531470319636&permissions=8&scope=bot')
    await ctx.sen(f'Больше информации - https://foxisquad-bots-system.gitbook.io/foxienjoy-bot/')

@client.command()
async def commands(ctx):
    await ctx.send(f'Мои команды:')
    await ctx.send(f'/randword')
    await ctx.send(f'/randnumb')
    await ctx.send(f'/info')
    await ctx.send(f'/fortune')
    await ctx.send(f'/utc_time')


keep_alive()
client.run(config.set.btoken)
