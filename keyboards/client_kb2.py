#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
vid='[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]'
v1='[0, 1, 0, 0, 0]'
v2='[0, 1, 0, 0, 0]'
v3='[0, 1, 0, 0, 0]'
jjj=['815653794', '2', '[0,1,0,0,0]', 'Б?2']
['2', '[1,0,0,0,0]']
im='5'
jm='[0,0,0,0,1]'
def bu(im,jm):
    try:
       
        if jm=='[1,0,0,0,0]':
            t= '0'
        if jm=='[0,1,0,0,0]':
            t= '1'
        if jm=='[0,0,1,0,0]':
            t= '2'
        if jm== '[0,0,0,1,0]':    
            t='3'
        if jm=='[0,0,0,0,1]':    
            t= '4'
    except: 
         pass
    # ch=int(im+t)
    # print(ch)
    # print(ch//5)
    return 5*(int(im)-1)+int(t)



def ikb_func2(jjj,tem_cal):   
    buk=['А','Б','В','Г','Д']
    I=[InlineKeyboardButton(text=' ',callback_data=f'wod_{j}_{kin}?{i}'+tem_cal)  for i in range(1,6) for j, kin in enumerate(buk, start=1)]
    # print(len(I))
    f=False
    ib_z=InlineKeyboardButton(text='ЗБЕРЕГТИ ТА ПЕРЕЙТИ ДАЛІ',callback_data='next2zav_'+tem_cal)
    ib_p=InlineKeyboardButton(text=' ',callback_data='w1')
    
    ib_a=InlineKeyboardButton(text='А',callback_data='id_1_А')
    ib_b=InlineKeyboardButton(text='Б',callback_data='id_2_Б')
    ib_v=InlineKeyboardButton(text='В',callback_data='id_3_В')
    ib_h=InlineKeyboardButton(text='Г',callback_data='id_4_Г')
    ib_d=InlineKeyboardButton(text='Д',callback_data='id_5_Д')    
                              
    ib_1=InlineKeyboardButton(text='1',callback_data='1')
    ib_2=InlineKeyboardButton(text='2',callback_data='2')
    ib_3=InlineKeyboardButton(text='3',callback_data='3')
    ib_4=InlineKeyboardButton(text='4',callback_data='4')
    ib_5=InlineKeyboardButton(text='5',callback_data='5')
    ikb_ts=InlineKeyboardMarkup(row_width=6)
   
    for n in jjj:
        try:
            if n:
                bk=n[4].split('?')[0]
                I[bu(n[2],n[3])]=InlineKeyboardButton(text='+',callback_data=f'wod_{n[2]}_{bk}?{n[2]}'+tem_cal)
            
        except: pass 
       
    ikb_ts.add(ib_p,ib_a, ib_b, ib_v, ib_h,ib_d)
    ikb_ts.add(ib_1,I[0], I[1], I[2], I[3],I[4])
    ikb_ts.add(ib_2,I[5], I[6], I[7], I[8],I[9])
    ikb_ts.add(ib_3,I[10], I[11], I[12], I[13],I[14])
    if len(jjj)==3:
        ikb_ts.row(ib_z)
    # ikb_ts.add(ib_4,I[15], I[16], I[17], I[18],I[19])
    # ikb_ts.add(ib_5,I[20], I[21], I[22], I[23],I[24])
    return ikb_ts


