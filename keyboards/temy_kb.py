# from d_b import chit_tema_db
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
ikb_tema=InlineKeyboardMarkup(row_width=3)
for i  in range(7):
      ikb_tema.insert( InlineKeyboardButton(text=f'Математика {i+1}',callback_data=f'tem!matematyka_{i+1}'))
      ikb_tema.insert( InlineKeyboardButton(text=f'Українська мова {i+1}',callback_data=f'teu!ukrayinska_mova_{i+1}'))



      
def ikb_ftema(tema):
   ikb_tema=InlineKeyboardMarkup(row_width=3)
   for i in range(7):
      for tem in tema:
            ikb_tema.insert( InlineKeyboardButton(text=tem[1]+' '+str(i+1),callback_data=tem[2]+str(i+1)))
   return ikb_tema