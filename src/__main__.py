from os import environ

from disnake import Intents
from dotenv import load_dotenv

from .bot import Bot


def main() -> None:
    load_dotenv()

    intents = Intents.default()
    intents.members = True

    bot = Bot(
        help_command=None,
        command_prefix="!",
        intents=intents,
    )

    bot.load_extension("src.commands")

    bot.run(environ["TOKEN"])


if __name__ == "__main__":
    main()
