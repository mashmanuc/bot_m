#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def ikb_func3():
    ib_z=InlineKeyboardButton(text='ЗБЕРЕГТИ ТА ПЕРЕЙТИ ДАЛІ',callback_data='nextzav_3')

    ikb_ts=InlineKeyboardMarkup()
    ikb_ts.add(ib_z)
    return ikb_ts
def ikb_func_finisch(tem_cal):
    ib_z=InlineKeyboardButton(text='ПЕРЕГЛЯНУТИ СВІЙ РЕЗУЛЬТАТ',callback_data='resul'+tem_cal)

    ikb_ts=InlineKeyboardMarkup()
    ikb_ts.add(ib_z)
    return ikb_ts
def ikb_dali(tem_cal):
    ib_z=InlineKeyboardButton(text='ПРОЙТИ ЩЕ РАЗ',callback_data='dali'+'!'+tem_cal)

    ikb_ts=InlineKeyboardMarkup()
    ikb_ts.add(ib_z)
    return ikb_ts 
def ikb_pochatok(tem_cal):
    ib_z=InlineKeyboardButton(text='ПРОЙТИ ЩЕ РАЗ',callback_data=f'tem!matematyka_'+tem_cal)

    ikb_ts=InlineKeyboardMarkup()
    ikb_ts.add(ib_z)
    return ikb_ts 