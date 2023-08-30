from aiogram  import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv,find_dotenv
load_dotenv()
ad=os.getenv('AD')
storage=MemoryStorage()
bot = Bot(token=os.getenv('TOKEN'))
dp=Dispatcher(bot,storage=storage)
