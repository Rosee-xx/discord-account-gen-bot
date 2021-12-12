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

class MainCog:
    def __init__(self, bot):
        self.bot = bot     

    @commands.command(pass_context=True, aliases=['Disney', 'D'])
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def disney(ctx):
        author = ctx.message.author
        with open('./accounts/disney.txt', 'r') as (f):
            text_spo = f.readlines()
            while True:
                randomline = random.choice(text_spo)
                combo = randomline.split(':')
                User = combo[0]
                Pass = combo[1]
                PassFixed = Pass.rstrip()
                if len(randomline) == 0:
                    continue
                with open('./accounts/disney.txt', 'w') as (c):
                    for line in text_spo:
                        if line.strip('\n') != f"{User}:{PassFixed}":
                            c.write(line)

                break

            print(Fore.GREEN + '')
            print(f"  > User {ctx.author} generated a Disney Account at time {datetime.datetime.now()}")
            print(Fore.WHITE + '')
            await author.send(f"{User}:{PassFixed}")
            await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")   

    @commands.command(pass_context=True, aliases=['Nord', 'N'])
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def nord(ctx):
        author = ctx.message.author
        with open('./accounts/nord.txt', 'r') as (f):
            text_spo = f.readlines()
            while True:
                randomline = random.choice(text_spo)
                combo = randomline.split(':')
                User = combo[0]
                Pass = combo[1]
                PassFixed = Pass.rstrip()
                if len(randomline) == 0:
                    continue
                with open('./accounts/nord.txt', 'w') as (c):
                    for line in text_spo:
                        if line.strip('\n') != f"{User}:{PassFixed}":
                            c.write(line)

                break

            print(Fore.GREEN + '')
            print(f"  > User {ctx.author} generated a NordVpn Account at time {datetime.datetime.now()}")
            print(Fore.WHITE + '')
            await author.send(f"{User}:{PassFixed}")
            await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")
    
    @commands.command(pass_context=True, aliases=['Spotify', 'S'])
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def spotify(ctx):
        author = ctx.message.author
        with open('./accounts/spotify.txt', 'r') as (f):
            text_spo = f.readlines()
            while True:
                randomline = random.choice(text_spo)
                combo = randomline.split(':')
                User = combo[0]
                Pass = combo[1]
                PassFixed = Pass.rstrip()
                if len(randomline) == 0:
                    continue
                with open('./accounts/spotify.txt', 'w') as (c):
                    for line in text_spo:
                        if line.strip('\n') != f"{User}:{PassFixed}":
                            c.write(line)

                break

            print(Fore.GREEN + '')
            print(f"  > User {ctx.author} generated a Spotify Account at time {datetime.datetime.now()}")
            print(Fore.WHITE + '')
            await author.send(f"{User}:{PassFixed}")
            await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")

    @commands.command(pass_context=True, aliases=['Hulu', 'H'])
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def hulu(ctx):
        author = ctx.message.author
        with open('./accounts/hulu.txt', 'r') as (f):
            text_spo = f.readlines()
            while True:
                randomline = random.choice(text_spo)
                combo = randomline.split(':')
                User = combo[0]
                Pass = combo[1]
                PassFixed = Pass.rstrip()
                if len(randomline) == 0:
                    continue
                with open('./accounts/hulu.txt', 'w') as (c):
                    for line in text_spo:
                        if line.strip('\n') != f"{User}:{PassFixed}":
                            c.write(line)

                break

            print(Fore.GREEN + '')
            print(f"  > User {ctx.author} generated a Hulu Account at time {datetime.datetime.now()}")
            print(Fore.WHITE + '')
            await author.send(f"{User}:{PassFixed}")
            await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")

    @commands.command(pass_context=True, aliases=['Nitro', 'N'])
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def nitro(ctx):
        author = ctx.message.author
        code = ''.join(x for x in s)
        url = f"https://discord.gift/{code}"
        print(Fore.GREEN + '')
        print(f"  > User {ctx.author} generated a Nitro Code at time {datetime.datetime.now()}")
        print(Fore.WHITE + '')
        await author.send(f"{User}:{PassFixed}")
        await ctx.send(f"{ctx.author} Account Sent! {datetime.datetime.now()}")

def setup(bot):
    bot.add_cog(MainCog(bot))
