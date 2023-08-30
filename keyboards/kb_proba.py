#!/usr/bin/python
# -*- coding: utf-8 -*-
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
vid='[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]'
v1='[0, 1, 0, 0, 0]'
v2='[0, 1, 0, 0, 0]'
v3='[0, 1, 0, 0, 0]'


def bu(i):
    try:
       
        if i=='1,0,0,0,0':
            return 'А'
        if i=='0,1,0,0,0':
            return 'Б'
        if i=='0,0,1,0,0':
            return 'В'
        if i== '0,0,0,1,0':    
            return 'Г'
        if i=='0,0,0,0,1':    
            return 'Д'
    except: 
         pass

def ikb_func2(j,tem_cal):
    a,b,w,h,d='А','Б','В','Г','Д'
    
    f=False
    ib_1=InlineKeyboardButton(text='1',callback_data='wod_1_1')
    ib_2=InlineKeyboardButton(text='2',callback_data='wod_2_2')
    ib_3=InlineKeyboardButton(text='3',callback_data='wod_3_3')
    ib_4=InlineKeyboardButton(text='4',callback_data='wod_4_4')
    ib_5=InlineKeyboardButton(text='5',callback_data='wod_5_5')

    ib_a1=InlineKeyboardButton(text=a,callback_data='wod_1_А?1'+tem_cal)
    ib_b1=InlineKeyboardButton(text=b,callback_data='wod_2_Б?1'+tem_cal)
    ib_v1=InlineKeyboardButton(text=w,callback_data='wod_3_В?1'+tem_cal)
    ib_h1=InlineKeyboardButton(text=h,callback_data='wod_4_Г?1'+tem_cal)
    ib_d1=InlineKeyboardButton(text=d,callback_data='wod_5_Д?1'+tem_cal)
    ib_a2=InlineKeyboardButton(text=a,callback_data='wod_1_А?2'+tem_cal)
    ib_b2=InlineKeyboardButton(text=b,callback_data='wod_2_Б?2'+tem_cal)
    ib_v2=InlineKeyboardButton(text=w,callback_data='wod_3_В?2'+tem_cal)
    ib_h2=InlineKeyboardButton(text=h,callback_data='wod_4_Г?2'+tem_cal)
    ib_d2=InlineKeyboardButton(text=d,callback_data='wod_5_Д?2'+tem_cal)
    ib_a3=InlineKeyboardButton(text=a,callback_data='wod_1_А?3'+tem_cal)
    ib_b3=InlineKeyboardButton(text=b,callback_data='wod_2_Б?3'+tem_cal)
    ib_v3=InlineKeyboardButton(text=w,callback_data='wod_3_В?3'+tem_cal)
    ib_h3=InlineKeyboardButton(text=h,callback_data='wod_4_Г?3'+tem_cal)
    ib_d3=InlineKeyboardButton(text=d,callback_data='wod_5_Д?3'+tem_cal)
    ib_a4=InlineKeyboardButton(text=a,callback_data='wod_1_А?4'+tem_cal)
    ib_b4=InlineKeyboardButton(text=b,callback_data='wod_2_Б?4'+tem_cal)
    ib_v4=InlineKeyboardButton(text=w,callback_data='wod_3_В?4'+tem_cal)
    ib_h4=InlineKeyboardButton(text=h,callback_data='wod_4_Г?4'+tem_cal)
    ib_d4=InlineKeyboardButton(text=d,callback_data='wod_5_Д?4'+tem_cal)
    ib_a5=InlineKeyboardButton(text=a,callback_data='wod_1_А?5'+tem_cal)
    ib_b5=InlineKeyboardButton(text=b,callback_data='wod_2_Б?5'+tem_cal)
    ib_v5=InlineKeyboardButton(text=w,callback_data='wod_3_В?5'+tem_cal)
    ib_h5=InlineKeyboardButton(text=h,callback_data='wod_4_Г?5'+tem_cal)
    ib_d5=InlineKeyboardButton(text=d,callback_data='wod_5_Д?5'+tem_cal)

    ib_p=InlineKeyboardButton(text=' ',callback_data='wod_0_0')

    ib_z=InlineKeyboardButton(text='Зберегти',callback_data='nextzav_'+tem_cal)

    ib_1=InlineKeyboardButton(text='1',callback_data='w1_1')
    ib_2=InlineKeyboardButton(text='2',callback_data='w2_2')
    ib_3=InlineKeyboardButton(text='3',callback_data='w3_3')
    ib_4=InlineKeyboardButton(text='4',callback_data='w4_4')
    ib_5=InlineKeyboardButton(text='5',callback_data='w5_5')
    ikb_ts=InlineKeyboardMarkup(row_width=6)
    ikb_ts.add(ib_1,ib_a1, ib_b1, ib_v1, ib_h1,ib_d1)
    ikb_ts.add(ib_2,ib_a2, ib_b2, ib_v2, ib_h2,ib_d2)
    ikb_ts.add(ib_3,ib_a3, ib_b3, ib_v3, ib_h3,ib_d3)
    ikb_ts.add(ib_4,ib_a4, ib_b4, ib_v4, ib_h4,ib_d4)
    ikb_ts.add(ib_5,ib_a5, ib_b5, ib_v5, ib_h5,ib_d5)
    return ikb_ts
buk=['А','Б','В','Г','Д']
IIn=[f'wod_{j}_{kin}?{i}'  for i in range(1,6) for j, kin in enumerate(buk, start=1)]
print(len(IIn))
for i in IIn:
    print(i)
    
"""wod_1_А?1
wod_2_Б?1
wod_3_В?1
wod_4_Г?1
wod_5_Д?1
wod_1_А?2
wod_2_Б?2
wod_3_В?2
wod_4_Г?2
wod_5_Д?2
wod_1_А?3
wod_2_Б?3
wod_3_В?3
wod_4_Г?3
wod_5_Д?3
wod_1_А?4
wod_2_Б?4
wod_3_В?4
wod_4_Г?4
wod_5_Д?4
wod_1_А?5
wod_2_Б?5
wod_3_В?5
wod_4_Г?5
wod_5_Д?5
"""  
    
    
# def ikb_func2(j,tem_cal):   
#     buk=['А','Б','В','Г','Д']
#     IIn=[InlineKeyboardButton(text=f'{j}',callback_data=f'wod_{kin}_Д?5'+tem_cal)  for i in range(1,6) for j, kin in enumerate(buk, start=1)]
#     print(len(IIn))
#     ikb_ts=InlineKeyboardMarkup(row_width=6)
#     for i in IIn:
#         ikb_ts.add(i)
#     return ikb_ts
# ikb_func2(j,tem_cal)

# s=vid_list(v1)


