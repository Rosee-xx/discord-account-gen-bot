from discord.ext import commands
import json
config = json.load("config.json")
bot = commands.Bot(command_prefix='!')
await bot.change_presence(activity=discord.Game(name=config["bot-status"]))

bot.load_extension("maincog")
bot.load_extension("Adminstuff")

bot.run(config["token"])
