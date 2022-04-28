from os import environ
from typing import Any

from aiomysql import Connection, Cursor, connect
from disnake.ext.commands import Bot as _Bot


class Bot(_Bot):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)  # type: ignore

        self._db: Connection | None = None
        self._xp_id: int = int(environ["XP_ID"])

    async def start(self, token: str, *, reconnect: bool = True) -> None:
        self._db = await connect(
            user="root",
            password=environ["MYSQL_ROOT_PASSWORD"],
            host=environ["MYSQL_HOST"],
            port=3306,
            db="zeppelin",
        )

        await super().start(token, reconnect=reconnect)

    async def get_xp(self, user: int) -> int:
        if self._db is None:
            print("ndb")
            return 0

        async with self._db.cursor() as cursor:
            cursor: Cursor

            await cursor.execute(
                "SELECT value FROM counter_values WHERE user_id = %s AND counter_id = %s;",
                (user, self._xp_id),
            )
            result: int = (await cursor.fetchone())[0]

        return result
