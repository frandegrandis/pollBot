# bot.py
import os
import random
from string import ascii_lowercase

from discord.ext import commands
from dotenv import load_dotenv


def get_emoji(letter):
    return ':regional_indicator_' + letter + ':'


emojis = {'a': '🇦', 'b': '🇧', 'c': '🇨', 'd': '🇩', 'e': '🇪',
          'f': '🇫', 'g': '🇬', 'h': '🇭', 'i': '🇮', 'j': '🇯', 'k': '🇰',
          'l': '🇱', 'm': '🇲', 'n': '🇳', 'o': '🇴', 'p': '🇵', 'q': '🇶',
          'r': '🇷', 's': '🇸', 't': '🇹',
          'u': '🇺', 'v': '🇻', 'w': '🇼', 'x': '🇽', 'y': '🇾', 'z': '🇿'}
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
letters = ascii_lowercase

bot = commands.Bot(command_prefix=',')


def get_days_between(from_day, to_day):
    return days.index(from_day), days.index(to_day)


def build_message(day, from_time, to_time):
    msg = day + '\n'
    i = 0
    for time in range(from_time, to_time + 1):
        msg += get_emoji(letters[i])
        i += 1
        msg += str(time) + ' est'
        msg += '\n'
    return msg


async def add_reaction(msg, from_time, to_time):
    i = 0
    for time in range(from_time, to_time + 1):
        await msg.add_reaction(emojis[letters[i]])
        i += 1


@bot.command(name='poll')
async def nine_nine(ctx, from_day, to_day, from_time: int, to_time: int):
    from_day = from_day.capitalize()
    to_day = to_day.capitalize()
    start, finish = get_days_between(from_day, to_day)
    for day in days[start:finish]:
        msg = await ctx.send(build_message(day, from_time, to_time))
        await add_reaction(msg, from_time, to_time)


bot.run(TOKEN)
