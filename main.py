# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

INTENTS = discord.Intents.all()

client = discord.Client(intents=INTENTS)

@client.event
async def on_ready():
    print(f'{client.user} se conectó a Discord!\n')
    
    print(f'{client.user} esta conectado a:\n')
    for guild in client.guilds:
        print(
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ayuda'):
        await message.channel.send(f" __**!hola:**__: Te mando un saludito uwu." +
                                     "\n__**!limpiar_chat**__: Borra todos los mensajes del chat. **__CUIDADO:__ PUEDE LLEVAR UN RATO Y ES IRREVERSIBLE ÒWÓ**" +
                                    "\n__**!ayuda**__: Este mensaje kpo, no se que esperabas que te diga jaja re tonto es." +
                                     "\n__**!invite**__: Link de invitacion para agregarme a otro server." +
                                     "\n__**!uwu**__: uwu"
                                     )

    if message.content.startswith('!hola'):
        await message.channel.send(f'Hola, {message.author.name}! uwu')

    if message.content.startswith('!limpiar_chat'):
        messages = message.channel.history()

        await message.channel.send("**...BORRANDO UWU...**")

        async for m in messages:
            await m.delete()

    if message.content.startswith('!uwu'):
        await message.channel.send("https://assets.change.org/photos/0/tx/qc/VJtXQCOhcJKBaLA-800x450-noPad.jpg?1570672109", tts=False)

    if message.content.startswith('!invite'):
        perm = discord.Permissions(permissions=8)
        await message.channel.send(f'Para invitar a este bot usa: \n {discord.utils.oauth_url(client.user.id,perm)}')

@client.event
async def on_member_join(member):
    for channel in client.get_all_channels():
        if(channel.name == "general"):
            await channel.send(f'Bienvenido/a **{member.name}** a {channel.guild.name}!'+
                                '\nCualquier duda, comunicate con **!ayuda** uwu')
            break

@client.event
async def on_guild_join(guild):
    for channel in guild.get_all_channels():
        if(channel.name == "general"):
            await channel.send('__Hola, acabo de entrar! uwu__ \nCualquier duda, comunicarse con \"**!ayuda**\"')
            break

client.run(TOKEN)

