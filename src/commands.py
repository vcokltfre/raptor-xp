from typing import Optional

from disnake import AllowedMentions, Member
from disnake.ext.commands import Cog, Context, command

from .bot import Bot
from .checks import guild_whitelist


class Commands(Cog):
    def __init__(self, bot: Bot) -> None:
        self._bot = bot

    @command(name="xp")
    @guild_whitelist()
    async def xp(self, ctx: Context[Bot], user: Optional[Member] = None) -> None:
        """Get the XP for a user or yourself."""

        _user = user or ctx.author

        xp = await self._bot.get_xp(_user.id)

        await ctx.reply(
            f"{_user.mention} has {xp} XP.",
            allowed_mentions=AllowedMentions(users=False, replied_user=False),
        )


def setup(bot: Bot) -> None:
    bot.add_cog(Commands(bot))
