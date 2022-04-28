from os import environ

from disnake.ext.commands import Context, check

from .bot import Bot

GUILDS = [int(guild) for guild in environ["GUILDS"].split(",")]


def guild_whitelist():
    async def predicate(ctx: Context[Bot]) -> bool:
        return bool(ctx.guild) and ctx.guild.id in GUILDS

    return check(predicate)
