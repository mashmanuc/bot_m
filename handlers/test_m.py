from aiogram import types,  Dispatcher
from create_bot import dp, bot
import aiogram.utils.markdown as md
from d_b import   u_bal_db, u_zav_db,chit_tema_db,did1, u_save_v_db_tema,u_del_zv_db
from d_b import   save_buf ,chit_buf, del_all_buf,mas_vid,u_dddel_db,save_user,chit_name_tema
from keyboards import kb_client, ikb_ftema, ikb_tema,ikb_func,ikb_func2,ikb_tema,ikb_func3,ikb_func_finisch, ikb_dali,ikb_pochatok
from vidp_func import vid,abc_f,vid2,prap,did2,did3,cif
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
# ind=[0]
# data_vid='k'
"""********************************************************************************"""
class test_StatesGroup(StatesGroup):
    test3=State()
    test20=State()
    test21=State()
"""********************************************************************************"""
# @dp.message_handler(commands=['start','help'])
async def start(msg:types.Message):
    id_user=str(msg.from_user.id)
    name=msg.from_user.username
    save_user([id_user,name])
    await bot.send_message(msg.from_user.id, "Вітаю на сторінці підготовки до МПТ з математики ",reply_markup=kb_client)
"""********************************************************************************"""
# @dp.message_handler(Text(equals='Відміна',ignore_case=True), state ="*")
async def cancel_handler(message:types.Message, state:FSMContext):
    if message.from_user.id:
        current_state= await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ok') 
"""********************************************************************************"""

async def vibir_temy(msg:types.Message)  :
         tema=chit_name_tema()
        
         await msg.answer('Мультитест',reply_markup=ikb_ftema(tema))
"""********************************************************************************"""
@dp.callback_query_handler(Text(startswith='tem!'))
async def temma2(coll: types.CallbackQuery):
    id_user=str(coll.from_user.id)
    # print('ddd',coll.data.split('!')[-1][0])
    del_all_buf('bufer'+id_user)
    tem_cal=coll.data.split('_')[-1]#!1 
    tema=(coll.data.split('!')[-1])
    u_tema='m'+str(id_user)+'m'+coll.data.split('_')[-1] # 815653794m!1
    num_zav=str(u_zav_db(u_tema))#num_zav= 1
    zx_rad=chit_tema_db(tema,num_zav)
    if zx_rad[0][2]:
        photo=zx_rad[0][2]
    else:
        photo=zx_rad[0][3]
    n_z  =zx_rad[0][1]
    vid=zx_rad[0][-1]
    bukva=' '
    s_buff=chit_buf('bufer'+id_user)
    tem_cal='!'+tem_cal
    if prap(vid)==1:
            mass_text='Виберіть варіант'
            markup=ikb_func(bukva,tem_cal)
            await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
            await bot.send_photo(coll.from_user.id,  photo)
            await coll.message.answer(mass_text, reply_markup=markup)
    elif prap(vid)==2:
            mass_text='Виберіть варіант'
            markup=ikb_func2(s_buff,tem_cal)
            await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
            await bot.send_photo(coll.from_user.id,  photo)
            await coll.message.answer(mass_text, reply_markup=markup)
    elif prap(vid)==3:
        if int(num_zav)==20:
            collbak=ikb_func_finisch(tem_cal)
            await coll.message.answer(text='ТЕСТУВАННЯ ЗАВЕРШЕНО',reply_markup=collbak)
        else:
            buff=[id_user,tem_cal,num_zav,str(11)]
            del_all_buf('bufer'+id_user)
            save_buf('bufer'+id_user,buff)
            await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
            await bot.send_photo(coll.from_user.id,  photo)
            mass_text='У відповідь надішліть тільки число'
            print('vhid 1')
            await bot.send_message(coll.from_user.id,  mass_text)
            await test_StatesGroup.first()
"""****************************'wid_'*********************************"""
@dp.callback_query_handler(Text(startswith='wid_'))
async def vibir_vid_ts(coll: types.CallbackQuery):
    await bot.delete_message(coll.from_user.id,coll.message.message_id)
    id_user=str(coll.from_user.id)
    tem_cal=(coll.data.split('!')[-1])
    tema='matematyka_'+(tem_cal)
    u_tema='m'+str(id_user)+'m'+(coll.data.split('!')[-1])
    bukva=(coll.data.split('_')[-1].split('!')[0])
    u_vidpovid=vid(bukva)
    num_zav=str(u_zav_db(u_tema))
    zx_rad=chit_tema_db(tema,num_zav)
    vid_b=zx_rad[0][-1]
    r=[u_tema,num_zav,u_vidpovid,did1(u_vidpovid,vid_b)]
    u_del_zv_db(u_tema,num_zav)
    u_save_v_db_tema(u_tema,r)
    s_buff=chit_buf('bufer'+id_user)
    tem_cal='!'+tem_cal
    if prap(vid_b)==1:
        markup=ikb_func(bukva,tem_cal)
    elif prap(vid_b)==2:
        markup=ikb_func2(s_buff,tem_cal)
    await coll.message.answer(  text=f'Ви вибрали варіант  {bukva}',reply_markup=markup)
"""*******************************'nextzav_'******************************"""
@dp.callback_query_handler(Text(startswith='nextzav_'))
async def next_ts(coll: types.CallbackQuery):
    tem_cal=(coll.data.split('!')[-1])
    id_user=str(coll.from_user.id)
    tema='matematyka_'+tem_cal
    u_tema='m'+str(id_user)+'m'+(coll.data.split('!')[-1])
    num_zav=str(u_zav_db(u_tema)+1)#num_zav= 1
    zx_rad=chit_tema_db(tema,num_zav)
    if zx_rad[0][2]:
        photo=zx_rad[0][2]
    else:
        photo=zx_rad[0][3]
    n_z  =zx_rad[0][1]
    bukva='X'
    r=[u_tema,num_zav," ",' ']
    u_save_v_db_tema(u_tema,r)
    s_buff=chit_buf('bufer'+id_user)
    tema='matematyka_'+tem_cal
    zx_rad=chit_tema_db(tema,num_zav)
    tem_cal='!'+tem_cal
    vid=zx_rad[0][-1]
    if prap(vid)==1:
        mass_text='Виберіть варіант'
        markup=ikb_func(bukva,tem_cal)
    elif prap(vid)==2:
        mass_text='Виберіть варіант'
        markup=ikb_func2(s_buff,tem_cal)
    elif prap(vid)==3:
        mass_text='У відповідь запишіть тільки число----'
        markup=ikb_func3()
    await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
    await bot.send_photo(coll.from_user.id,  photo)
    await coll.message.answer(mass_text, reply_markup=markup)

"""******************************'wod_'*******************************"""
@dp.callback_query_handler(Text(startswith='wod_'))
async def vibir_vid_ts2(coll: types.CallbackQuery):
    await bot.delete_message(coll.from_user.id,coll.message.message_id)
    name=coll.from_user.username#
    id_user=str(coll.from_user.id)#
    tem_cal=(coll.data.split('!')[-1])#
    u_tema='m'+str(id_user)+'m'+(coll.data.split('!')[-1])#
    bukva=(coll.data.split('_')[-1].split('!')[0])#
    num_v=(bukva.split('?')[-1])#
    vid_v=vid2(bukva)##
    num_zav=str(u_zav_db(u_tema))#
    tema='matematyka_'+tem_cal#
    zx_rad=chit_tema_db(tema,num_zav)#
    vid_b=zx_rad[0][-1]
    buff=[id_user,num_v,vid_v,bukva]#
    save_buf('bufer'+id_user,buff)#
    u_vidpovid2=mas_vid('bufer'+id_user)#
    r=[u_tema,num_zav,u_vidpovid2,did2(u_vidpovid2,vid_b)]#
    u_del_zv_db(u_tema,num_zav)#
    u_save_v_db_tema(u_tema,r)#
    s_buff=chit_buf('bufer'+id_user)#
    tem_cal='!'+tem_cal
    if prap(vid_b)==1:
        markup=ikb_func(bukva,tem_cal)
    elif prap(vid_b)==2:
        markup=ikb_func2(s_buff,tem_cal)
    await coll.message.answer(  text=f'Ви вибрали варіант  {bukva}',reply_markup=markup)
"""******************************'next2zav_'*******************************"""
# @dp.message_handler()
@dp.callback_query_handler(Text(startswith='next2zav_'),state=None)
async def next_ts2(coll: types.CallbackQuery,state: FSMContext):
    tem_cal=(coll.data.split('!')[-1])
    id_user=str(coll.from_user.id)
    tema='matematyka_'+tem_cal
    del_all_buf('bufer'+id_user)
    u_tema='m'+str(id_user)+'m'+(coll.data.split('!')[-1])
    num_zav=str(u_zav_db(u_tema)+1)#num_zav= 1
    zx_rad=chit_tema_db(tema,num_zav)
    if zx_rad[0][2]:
        photo=zx_rad[0][2]
    else:
        photo=zx_rad[0][3]
    n_z  =zx_rad[0][1]
    vid=zx_rad[0][-1]
    bukva='X'
    tem_cal='!'+tem_cal
    r=[u_tema,num_zav," ",' ']
    u_save_v_db_tema(u_tema,r)
    s_buff=chit_buf('bufer'+id_user)
    if prap(vid)==1:
        mass_text='Виберіть варіант'
        markup=ikb_func(bukva,tem_cal)
        await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
        await bot.send_photo(coll.from_user.id,  photo)
        await coll.message.answer(mass_text, reply_markup=markup)
    elif prap(vid)==2:
        mass_text='Виберіть варіант'
        markup=ikb_func2(s_buff,tem_cal)
        await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
        await bot.send_photo(coll.from_user.id,  photo)
        await coll.message.answer(mass_text, reply_markup=markup)
    elif prap(vid)==3:
            buff=[id_user,tem_cal,num_zav,str(11)]
            save_buf('bufer'+id_user,buff)
            await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
            await bot.send_photo(coll.from_user.id,  photo)
            mass_text='У відповідь надішліть тільки число'
            await coll.message.answer(  mass_text)
            await test_StatesGroup.next()
        
"""*************************'wud_3'**************************"""
@dp.message_handler(Text(startswith='wud_'),state=None)
async def vibir_vid_ts3(coll: types.CallbackQuery,state: FSMContext):
    await bot.delete_message(coll.from_user.id,coll.message.message_id)
    id_user=str(coll.from_user.id)
    tem_cal=(coll.data.split('!')[-1])
    u_tema='m'+str(id_user)+'m'+(coll.data.split('!')[-1])
    num_zav=str(u_zav_db(u_tema))
    u_del_zv_db(u_tema,num_zav)
    tema='matematyka_'+tem_cal
    zx_rad=chit_tema_db(tema,num_zav)
    vid_b=zx_rad[0][-1]
    tem_cal='!'+tem_cal
    await coll.message.answer(  text=f'Введіть відповідь')
    await test_StatesGroup.test3.set()    
        
"""*************************'wud_'**************************"""
@dp.callback_query_handler(state=test_StatesGroup.test3)
@dp.message_handler(state=test_StatesGroup.test3)
async def vibir_vid_ts19(msg: types.Message,state:FSMContext):
    tx=cif(msg.text)
    if  tx!='':
        id_user=str(msg.from_user.id)
        s_buff=chit_buf('bufer'+id_user) 
        u_tema=('m'+str(id_user)+'m'+s_buff[0][2].split('!')[-1])
        tema='matematyka_'+s_buff[0][2].split('!')[-1]
        num_zav=s_buff[0][3]
        next_num_zav=str(int(num_zav)+1)
        zx_rad=chit_tema_db(tema,next_num_zav)
        vid_3=chit_tema_db(tema,num_zav)[0][-1]
        r=[u_tema,num_zav,tx,did3(vid_3,tx)]
        u_del_zv_db(u_tema,num_zav)
        u_save_v_db_tema(u_tema,r)
        if len(zx_rad)>0:
            n_z  =zx_rad[0][1]
            photo=zx_rad[0][2]
            vid=zx_rad[0][-1]
            await msg.answer(md.text('ЗБЕРЕЖЕНО ВІДПОВІДЬ('+md.bold(tx)+')'),parse_mode=ParseMode.MARKDOWN)
            await msg.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {n_z} 🧠🧠🧠')
            await bot.send_photo(msg.from_user.id,  photo)
            mass_text='У відповідь надішліть тільки число'
            await msg.answer( mass_text)
            await test_StatesGroup.next()  
    else:   
        await msg.answer('У ВІДПОВІДІ МАЄ БУТИ ЧИСЛО')
        state=test_StatesGroup.test3
            
"""*************************'wud_20'**************************"""
@dp.message_handler(state=test_StatesGroup.test20)
@dp.callback_query_handler(state=test_StatesGroup.test20)
async def next_ts20(msg: types.CallbackQuery,state: FSMContext):
    tx=cif(msg.text)
    if  tx!='':
        id_user=str(msg.from_user.id)
        s_buff=chit_buf('bufer'+id_user)
        num_zav=str(int(s_buff[0][3])+1)
        tem_cal=s_buff[0][2]
        tema='matematyka_'+s_buff[0][2].split('!')[-1]
        vid_3=chit_tema_db(tema,num_zav)[0][-1]
        u_tema=('m'+str(id_user)+'m'+s_buff[0][2].split('!')[-1])
        r=[u_tema,num_zav,tx,did3(vid_3,tx)]
        u_del_zv_db(u_tema,num_zav)
        u_save_v_db_tema(u_tema,r)
        del_all_buf('bufer'+id_user)
        await state.finish()
        await msg.answer(md.text('ЗБЕРЕЖЕНО ВІДПОВІДЬ('+md.bold(tx)+')'),parse_mode=ParseMode.MARKDOWN)
        await msg.answer( text='ТЕСТ ПРОЙДЕНО',reply_markup=ikb_func_finisch(tem_cal))
    else:   
        await msg.answer('У ВІДПОВІДІ МАЄ БУТИ ЧИСЛО')
        state=test_StatesGroup.test20
'************************resul***********************************'
@dp.callback_query_handler(Text(startswith='resul'))
async def vibir_vid_ts(coll: types.CallbackQuery):  
    tem_cal=coll.data.split('!')[-1]  
    # print('1    ',tem_cal)
    u_tema='m'+str(coll.from_user.id)+'m'+tem_cal
    s_bal=u_bal_db(u_tema)
    await coll.message.answer(md.text(' З можливих  30 балів ВИ набрали '+md.bold(s_bal)),parse_mode=ParseMode.MARKDOWN)
    await coll.message.answer(text=(' ПРОЙТИ ЩЕ РАЗ(ВІДПОВІДІ З ПОТОЧНОГО ТЕСТУ ВИДАЛЯТЬСЯ)'),reply_markup=ikb_dali(tem_cal))
@dp.callback_query_handler(Text(startswith='dali'))
async def vibir_vid_po(coll: types.CallbackQuery):  
    tem_cal=coll.data.split('!')[-1]  
    # print('2   ',tem_cal)
    tema='matematyka_'+tem_cal
    u_tema='m'+str(coll.from_user.id)+'m'+str(tem_cal)
    # print('u_tema   ',u_tema)
    u_dddel_db(u_tema)
    await coll.message.answer(text=(f'Ваші відповіді до теми {tema} видалено'),reply_markup=ikb_pochatok(tem_cal))





def register_handler_test_m(dp: Dispatcher)   :
    dp.register_message_handler(start, commands=['start','help','menu'])
    dp.register_message_handler(vibir_temy, commands=['Виберіть_тест'])
    
    
    
    dp.callback_query_handler(vibir_vid_ts2)
    dp.callback_query_handler(next_ts2)
    dp.callback_query_handler(temma2)
    dp.callback_query_handler(next_ts20)
    dp.callback_query_handler(vibir_vid_ts)
    dp.callback_query_handler(vibir_vid_po)



