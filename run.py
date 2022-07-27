import os
import discord
from cfg import cfg
from musicbot.audiocontroller import AudioController
from musicbot.settings import Settings
from musicbot.utils import guild_to_audiocontroller, guild_to_settings
from discord.ext import commands
from cogs.reddit_cog import Subreddity
from cogs.roll_cog import Inne

initial_extensions = ['musicbot.commands.music',
                      'musicbot.commands.general', 'musicbot.plugins.button']

bot = commands.Bot(command_prefix=cfg.BOT_PREFIX,
                   pm_help=True, case_insensitive=True)
bot.add_cog(Subreddity(bot))
bot.add_cog(Inne(bot))

if __name__ == '__main__':

    cfg.ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
    cfg.COOKIE_PATH = cfg.ABSOLUTE_PATH + cfg.COOKIE_PATH

    if cfg.BOT_TOKEN == "":
        print("Error: No bot token!")
        exit

    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)


@bot.event
async def on_ready():
    print(cfg.STARTUP_MESSAGE)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="chuj, type {}help".format(cfg.BOT_PREFIX)))

    for guild in bot.guilds:
        await register(guild)
        print("Joined {}".format(guild.name))

    print(cfg.STARTUP_COMPLETE_MESSAGE)


@bot.event
async def on_guild_join(guild):
    print(guild.name)
    await register(guild)


async def register(guild):

    guild_to_settings[guild] = Settings(guild)
    guild_to_audiocontroller[guild] = AudioController(bot, guild)

    sett = guild_to_settings[guild]

    try:
        await guild.me.edit(nick=sett.get('default_nickname'))
    except:
        pass

    if cfg.GLOBAL_DISABLE_AUTOJOIN_VC == True:
        return

    vc_channels = guild.voice_channels

    if sett.get('vc_timeout') == False:
        if sett.get('start_voice_channel') == None:
            try:
                await guild_to_audiocontroller[guild].register_voice_channel(guild.voice_channels[0])
            except Exception as e:
                print(e)

        else:
            for vc in vc_channels:
                if vc.id == sett.get('start_voice_channel'):
                    try:
                        await guild_to_audiocontroller[guild].register_voice_channel(vc_channels[vc_channels.index(vc)])
                    except Exception as e:
                        print(e)


bot.run(cfg.BOT_TOKEN, bot=True, reconnect=True)
