import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+', intents=discord.Intents.all())

id=os.environ["CHANNEL"]


@bot.event
async def on_member_join(member):
    embed = discord.Embed(color=0x44944A)
    embed.add_field(name="✅️  |  Зашел на сервер", value=f"{member.mention}, добро пожаловать!", inline=False)
    await bot.get_channel(id).send(embed=embed)


@bot.event
async def on_member_remove(member):
    embed = discord.Embed(color=0xc11f1f)
    embed.add_field(name="❌  |  Покинул сервер", value=f"{member.name} покинул сервер(", inline=False)
    await bot.get_channel(id).send(embed=embed)


@bot.event
async def on_message_edit(before, after):
    embed = discord.Embed(color=0xf7f21a)
    embed.add_field(name="✏  |  Редактирование сообщения", value=f"{before.author.mention} изменил сообщение:",
                    inline=False)
    embed.add_field(name="До:", value=f">>> {before.content}", inline=False)
    embed.add_field(name="После:", value=f">>> {after.content}", inline=False)
    embed.set_footer(text="")
    await bot.get_channel(id).send(embed=embed)


@bot.event
async def on_message_delete(message):
    embed = discord.Embed(color=0xc11f1f)
    embed.add_field(name="🗑  |  Удаление сообщения", value=f"{message.author.mention} удалил сообщение:", inline=False)
    embed.add_field(name="Текст сообщения:", value=f">>> {message.content}", inline=False)
    embed.set_footer(text="")
    await bot.get_channel(id).send(embed=embed)


@bot.event
async def on_voice_state_update(member, before, after):
    embed = None
    if before.channel is None:
        embed = discord.Embed(color=0x30d5c8)
        embed.add_field(name="🎵  | Голосовые каналы", value=f"{member.mention} зашел в канал {after.channel.mention}",
                        inline=False)
    elif after.channel is None:
        embed = discord.Embed(color=0x30d5c8)
        embed.add_field(name="🎵  | Голосовые каналы", value=f"{member.mention} покинул канал {before.channel.mention}",
                        inline=False)
    elif before.channel != after.channel:
        embed = discord.Embed(color=0x30d5c8)
        embed.add_field(name="🎵  | Голосовые каналы",
                        value=f"{member.mention} перешёл из {before.channel.mention} в {after.channel.mention}",
                        inline=False)
    else:
        return
    await bot.get_channel(id).send(embed=embed)

bot.run(os.environ["TOKEN"])
