import logging
from aiogram.types import Message
from pyrogram import Client

from .. import loader, utils

@loader.module(name="FunModule", author="YourName", version=1)
class FunModule(loader.Module):
    """Fun Module Description"""

    async def on_load(self, app: Client):
        """Called when the module is loaded"""
        logging.info(f"Module {self.name} loaded")

    @loader.on_bot(lambda self, app, message: message.text and message.text.lower() == "ты дурак?")
    async def insult_handler(self, app: Client, message: Message):
        """Responds to insults"""
        return await message.reply("Сам такой!")

    @loader.on(lambda _, __, m: "привет" in m.text.lower())
    async def greet(self, app: Client, message: Message):
        """Greets the user"""
        return await message.reply("Привет! Я здесь, чтобы веселить тебя!")

    @loader.on(lambda _, __, m: "шутка" in m.text.lower())
    async def tell_joke(self, app: Client, message: Message):
        """Tells a joke"""
        jokes = [
            "Почему компьютер завис? Потому что он думал о смысле жизни!",
            "Какой айтишник самый счастливый? Тот, у которого нет багов!",
            "Зачем программисту пачка бумаги? Чтобы записывать исключения!",
        ]
        joke = random.choice(jokes)
        return await message.reply(joke)

    async def on_unload(self, app: Client):
        """Called when the module is unloaded"""
        logging.info(f"Module {self.name} unloaded")
