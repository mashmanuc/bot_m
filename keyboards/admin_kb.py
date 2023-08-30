from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
'''***********************************************************************************'''
ikb_ad=InlineKeyboardMarkup(row_width=1)
b1=InlineKeyboardButton(text='Результати',callback_data='usery&')
b2=InlineKeyboardButton(text=f'Додати тему ',callback_data='ttema!')

ikb_ad.row( b1,b2)
'''***********************************************************************************'''
ikb_us=InlineKeyboardMarkup(row_width=1)
def us_list(text_us, coll):
    ikb_us=InlineKeyboardMarkup(row_width=1)
    b_u=InlineKeyboardButton(text=text_us,callback_data=coll)
    ikb_us.add(b_u)
    return ikb_us
