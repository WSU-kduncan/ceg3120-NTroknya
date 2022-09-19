import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    lantern_oath_quotes = [
        'IN BRIGHTEST DAY, IN BLACKEST NIGHT, NO EVIL SHALL ESCAPE MY SIGHT, LET THOSE WHO WORSHIP EVIL’S MIGHT, BEWARE MY POWER… GREEN LANTERN’S LIGHT!',
        'IN BLACKEST DAY, IN BRIGHTEST NIGHT, BEWARE YOUR FEARS MADE INTO LIGHT, LET THOSE WHO TRY TO STOP WHAT’S RIGHT, BURN LIKE MY POWER… SINESTRO’S MIGHT!',
        'THE BLACKEST NIGHT FALLS FROM THE SKIES, THE DARKNESS GROWS AS ALL LIGHT DIES, WE CRAVE YOUR HEARTS AND YOUR DEMISE, BY MY BLACK HAND… THE DEAD SHALL RISE!',
        'WITH BLOOD AND RAGE OF CRIMSON RED, RIPPED FROM A CORPSE SO FRESHLY DEAD, TOGETHER WITH OUR HELLISH HATE, WE’LL BURN YOU ALL… THAT IS YOUR FATE!',
	'IN FEARFUL DAY, IN RAGING NIGHT, WITH STRONG HEARTS FULL, OUR SOULS IGNITE, WHEN ALL SEEMS LOST IN THE WAR OF LIGHT, LOOK TO THE STARS… FOR HOPE BURNS BRIGHT!',
	'THIS POWER IS MINE, THIS IS MY LIGHT. BE IT IN BRIGHT OF DAY OR BLACK OF NIGHT. I LAY CLAIM TO ALL THAT FALLS WITHIN MY SIGHT, TO TAKE WHAT I WANT… THAT IS MY RIGHT!',
	'TOR LOREK SAN, BOR NAKKA MUR. NATROMO FAAN TORNEK WOT UR. TER LANTERN KER LO ABIN SUR. TAAN LEK LEK NOK – FORMORROW SUR!',
	'FOR HEARTS LONG LOST AND FULL OF FRIGHT, FOR THOSE ALONE IN BLACKEST NIGHT, ACCEPT OUR RING AND JOIN OUR FIGHT, LOVE CONQUERS ALL… WITH VIOLET LIGHT!',
	'IN DARKEST DAY, IN SILENT NIGHT WITH SOULS FULL OF LIGHT CRUSH THOSE WHO BRING BLACKEST NIGHT BY OUR HAND… WHITE LANTERN’S LIGHT!!',
    ]

    if message.content == 'oath!':
        response = random.choice(lantern_oath_quotes)
        await message.channel.send(response)

client.run(TOKEN)
