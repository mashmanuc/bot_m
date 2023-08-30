#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
b1=KeyboardButton('/menu')
b2=KeyboardButton('/Наступне_завдання')
b3=KeyboardButton('/Виберіть_тест')
b4=KeyboardButton('/Виберіть_тему')

kb_client=ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1,b3).add(b2)

kb_ts=ReplyKeyboardMarkup(resize_keyboard=True)

"""***************************************************"""
ib_a=InlineKeyboardButton(text='А',callback_data='wid_1_А')
ib_b=InlineKeyboardButton(text='Б',callback_data='wid_2_Б')
ib_v=InlineKeyboardButton(text='В',callback_data='wid_3_В')
ib_h=InlineKeyboardButton(text='Г',callback_data='wid_4_Г')
ib_d=InlineKeyboardButton(text='Д',callback_data='wid_5_Д')
ikb_ts=InlineKeyboardMarkup(row_width=5)
ikb_ts.add(ib_a, ib_b, ib_v, ib_h,ib_d)

def ikb_func(bukva,tem_cal):
    f=False
    ib_a=InlineKeyboardButton(text='А',callback_data='wid_1_А'+tem_cal)
    ib_b=InlineKeyboardButton(text='Б',callback_data='wid_2_Б'+tem_cal)
    ib_v=InlineKeyboardButton(text='В',callback_data='wid_3_В'+tem_cal)
    ib_h=InlineKeyboardButton(text='Г',callback_data='wid_4_Г'+tem_cal)
    ib_d=InlineKeyboardButton(text='Д',callback_data='wid_5_Д'+tem_cal)
    ib_z=InlineKeyboardButton(text='ЗБЕРЕГТИ ТА ПЕРЕЙТИ ДАЛІ',callback_data='nextzav_'+tem_cal)
    if bukva=='А':
        ib_a=InlineKeyboardButton(text='А+',callback_data='wid_1_А'+tem_cal)
        f=True
    if bukva=='Б':
        ib_b=InlineKeyboardButton(text='Б+',callback_data='wid_2_Б'+tem_cal)
        f=True
    if bukva=='В':
        ib_v=InlineKeyboardButton(text='В+',callback_data='wid_3_В'+tem_cal)
        f=True
    if bukva=='Г':    
        ib_h=InlineKeyboardButton(text='Г+',callback_data='wid_4_Г'+tem_cal)
        f=True
    if bukva=='Д':    
        ib_d=InlineKeyboardButton(text='Д+',callback_data='wid_5_Д'+tem_cal)
        f=True
    ikb_ts=InlineKeyboardMarkup(row_width=5)
    ikb_ts.add(ib_a, ib_b, ib_v, ib_h,ib_d)
    if f:
        ikb_ts.row(ib_z)
    return ikb_ts
 