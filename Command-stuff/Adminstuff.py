from discord.ext import commands
import getpass
from typing import Text
from colorama import Fore, Style
from colorama import init, Fore, Back, Style
from discord import channel
from discord.client import Client
import os, time, datetime, random, asyncio, aiohttp, json, discord, time, colorama, requests
from itertools import cycle
from discord import Game, File
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
from pyfiglet import Figlet

class Adminstuff:
    def __init__(self, bot):
        self.bot = bot     

    @commands.command(pass_context=True, aliases=[""])
    async def ban()

    @client.command()
    @commands.has_permissions(ban_members = True)
    async def ban(ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(f"{member} banned.")
    
## more coming soon i guess idk.
def setup(bot):
    bot.add_cog(Adminstuff(bot))
