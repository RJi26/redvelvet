import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "e!", intents = intents)
bot = commands.Bot(command_prefix = "e!", intents = intents)

load_dotenv()

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = f'{len(bot.guilds)} servers!'))
    print("Bot is up and running!")

@client.event
async def on_member_join(member):
    if member.guild.name == 'red・velvet ♡':  #type your server name
        embed = discord.Embed(title=f'', description = f'welcome to {member.guild.name} {member.mention} \n ˚ ༘♡ ⋆｡ [roles](https://discord.gg/mUcFFgQv2X)﹒[ping](https://discord.gg/xWADmpcGMQ)﹒[chat](https://discord.gg/PH7zb2QPUK)﹒˚ ❀ \n **﹒enjoy your stay + boost us :)**', color = discord.Color.from_rgb(47, 49, 54))
        embed.set_footer(text=".gg/rvelvet・enjoy!")
        await client.get_channel(1059592716238991438).send(f"{member.mention}")
        await client.get_channel(1059592716238991438).send(embed=embed)
        #role = discord.utils.get(member.guild.roles, name="Community")
        #await member.add_roles(role)
    else:
        return



client.run(os.environ['TOKEN'])