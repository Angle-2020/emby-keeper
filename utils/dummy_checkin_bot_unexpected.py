import asyncio
from io import BytesIO
from pathlib import Path
import random
import string

from loguru import logger
import tomli as tomllib
from pyrogram import filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message, BotCommand

from embykeeper.cli import AsyncTyper
from embykeeper.telegram.pyrogram import Client
from embykeeper.config import config
from embykeeper.telegram.session import API_ID, API_HASH

user_states = {}

app = AsyncTyper()


async def dump(client: Client, message: Message):
    if message.text:
        logger.debug(f"<- {message.text}")


async def start(client: Client, message: Message):
    await client.send_message(message.from_user.id, "你好! 请使用命令进行签到测试!")


async def send_unexpected(client: Client, message: Message):
    await client.send_message(
        message.from_user.id, '你好, 目前本服务器正在排查自动化签到工具, 请输入"我是人"以排除你的嫌疑:'
    )


@app.async_command()
async def main(config_file: Path):
    await config.reload_conf(config_file)
    bot = Client(
        name="test_bot",
        bot_token=config.bot.token,
        proxy=config.proxy.model_dump(),
        workdir=Path(__file__).parent,
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=True,
    )
    async with bot:
        await bot.add_handler(MessageHandler(dump), group=1)
        await bot.add_handler(MessageHandler(start, filters.command("start")))
        await bot.add_handler(MessageHandler(send_unexpected, filters.command("checkin")))
        await bot.set_bot_commands(
            [
                BotCommand("start", "Start the bot"),
                BotCommand("checkin", "Checkin session for test"),
            ]
        )
        logger.info(f"Started listening for commands: @{bot.me.username}.")
        await asyncio.Event().wait()


if __name__ == "__main__":
    app()
