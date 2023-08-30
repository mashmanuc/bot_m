from aiogram import types,  Dispatcher
from create_bot import dp, bot
import aiogram.utils.markdown as md
from d_b import   u_bal_db, u_zav_db,chit_tema_db,did1, u_save_v_db_tema,u_del_zv_db
from d_b import   save_buf ,chit_buf, del_all_buf,mas_vid,u_dddel_db,save_user
from keyboards import ikb_tema,u_ikb_func_finisch,u_ikb_dali,u_ikb_pochatok,ikb_func_u,ikb_func3u
from vidp_func import vid,vid2,prap,did2,did3,cif,prap_u,vid_u1
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import aiogram.utils.markdown as md
from aiogram.types import ParseMode

"""********************************************************************************"""
class test_u(StatesGroup):
    test3=State()
    test20=State()
    test21=State()
def sup(coll: types.CallbackQuery):
    
    pass

"""**********************************teu!**********************************************"""
@dp.callback_query_handler(Text(startswith='teu!'))
async def temma2_u(coll: types.CallbackQuery):
    
    id_user=str(coll.from_user.id)
    u=coll.data.split('!')[-1][0]
    tem_cal=(coll.data.split('!')[-1])
    tema=tem_cal
    u_tema=u+str(id_user)+u+tema # 815653794m!1
    num_zav=str(u_zav_db(u_tema))#num_zav= 1
    
    del_all_buf('bufer'+id_user)
    if num_zav=='21':
         collbak=u_ikb_func_finisch(tem_cal)
         await coll.message.answer(text='ТЕСТУВАННЯ ЗАВЕРШЕНО',reply_markup=collbak)
    else:
        zx_rad=chit_tema_db(tema,num_zav)
        photo=zx_rad[0][3]
        vid=zx_rad[0][-1]
        l_vid=prap_u(vid)
        bukva=' '
        if prap_u(vid)!=3:
                mass_text='Виберіть варіант'
                markup=ikb_func_u(bukva,tem_cal,l_vid)
                await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
                await bot.send_photo(coll.from_user.id,  photo)
                await coll.message.answer(mass_text, reply_markup=markup)
        elif prap_u(vid)==3:
                mass_text='Виберіть варіант!'
                markup=ikb_func3u(bukva,tem_cal)
                await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
                await bot.send_photo(coll.from_user.id,  photo)
                await coll.message.answer(mass_text, reply_markup=markup)
"""****************************'uwi_'*********************************"""
@dp.callback_query_handler(Text(startswith='uwi_'))
async def vibir_vid_ts_u(coll: types.CallbackQuery):
    await bot.delete_message(coll.from_user.id,coll.message.message_id)
    
    id_user=str(coll.from_user.id)
    u=coll.data.split('!')[-1][0]#u
    tem_cal=(coll.data.split('!')[-1])
    tema=tem_cal
    u_tema=u+str(id_user)+u+(coll.data.split('!')[-1])
    
    num_zav=str(u_zav_db(u_tema))
    
    bukva=(coll.data.split('+')[-1].split('!')[0])
    
    
    zx_rad=chit_tema_db(tema,num_zav)
    vid=zx_rad[0][-1]
    l_vid=prap_u(vid)
    u_vidpovid=vid_u1(l_vid,bukva)
    r=[u_tema,num_zav,u_vidpovid,did1(u_vidpovid,vid)]
    u_del_zv_db(u_tema,num_zav)
    u_save_v_db_tema(u_tema,r)
    s_buff=chit_buf('bufer'+id_user)
    if prap(vid)!=3:
        markup=ikb_func_u(bukva,tem_cal,l_vid)
    elif prap(vid)==3:
        markup=ikb_func3u(s_buff,tem_cal)
    await coll.message.answer(  text=f'Ви вибрали варіант  {bukva}',reply_markup=markup)
"""*******************************'nexu_'******************************"""
@dp.callback_query_handler(Text(startswith='nexu_'))
async def next_ts_u(coll: types.CallbackQuery):
    
    id_user=str(coll.from_user.id)
    u=coll.data.split('!')[-1][0]
    tem_cal=(coll.data.split('!')[-1])
    tema=tem_cal
    u_tema=u+str(id_user)+u+(coll.data.split('!')[-1])
    
    num_zav=str(u_zav_db(u_tema)+1)#num_zav= 1
    
    del_all_buf('bufer'+id_user)
    if num_zav=='21':
         collbak=u_ikb_func_finisch(tem_cal)
         await coll.message.answer(text='ТЕСТУВАННЯ ЗАВЕРШЕНО',reply_markup=collbak)
    else:
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
        zx_rad=chit_tema_db(tema,num_zav)
        
        vid=zx_rad[0][-1]
        l_vid=prap_u(vid)
        bukva=' '
        s_buff=chit_buf('bufer'+id_user)              
        if prap_u(vid)!=3:
                mass_text='Виберіть варіант'
                markup=ikb_func_u(bukva,tem_cal,l_vid)
                await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
                await bot.send_photo(coll.from_user.id,  photo)
                await coll.message.answer(mass_text, reply_markup=markup)
        elif prap_u(vid)==3:
                mass_text='Виберіть варіант!'
                markup=ikb_func3u(bukva,tem_cal)
                await coll.message.answer(text=f'🧠🧠🧠 ЗАВДАННЯ {num_zav} 🧠🧠🧠')
                await bot.send_photo(coll.from_user.id,  photo)
                await coll.message.answer(mass_text, reply_markup=markup)   

"""******************************'uwo_'*******************************"""
@dp.callback_query_handler(Text(startswith='uwo_'))
async def vibir_vid_ts2_u(coll: types.CallbackQuery):
    await bot.delete_message(coll.from_user.id,coll.message.message_id)
    id_user=str(coll.from_user.id)#
    u=coll.data.split('!')[-1][0]#u
    tem_cal=(coll.data.split('!')[-1])#
    tema=tem_cal#
    u_tema=u+str(id_user)+u+(coll.data.split('!')[-1])#
    
    bukva=(coll.data.split('_')[2].split('!')[0])#
    
    num_v=(bukva.split('?')[-1])#
    vid_v=vid2(bukva)##
    num_zav=str(u_zav_db(u_tema))#
    zx_rad=chit_tema_db(tema,num_zav)#
    buff=[id_user,num_v,vid_v,bukva]#
    save_buf('bufer'+id_user,buff)#
    u_vidpovid2=mas_vid('bufer'+id_user)#
    vid=zx_rad[0][-1]
    l_vid=prap_u(vid)
   
    r=[u_tema,num_zav,u_vidpovid2,did2(u_vidpovid2,vid)]#
    u_del_zv_db(u_tema,num_zav)#
    u_save_v_db_tema(u_tema,r)#
    s_buff=chit_buf('bufer'+id_user)#
    if prap_u(vid)!=3:
        markup=ikb_func_u(bukva,tem_cal,l_vid)
    else    :
        if int(num_zav)==21:
            collbak=u_ikb_func_finisch(tem_cal)
            await coll.message.answer(text='ТЕСТУВАННЯ ЗАВЕРШЕНО',reply_markup=collbak)
        else:
                markup=ikb_func3u(s_buff,tem_cal)
    await coll.message.answer(  text=f'Ви вибрали варіант  {bukva}',reply_markup=markup)
'************************ures***********************************'
@dp.callback_query_handler(Text(startswith='ures'))
async def vibir_vid_ts_u(coll: types.CallbackQuery):  
    
    id_user=str(coll.from_user.id)
    u=coll.data.split('!')[-1][0]#u
    tem_cal=(coll.data.split('!')[-1])
    u_tema=u+str(coll.from_user.id)+u+tem_cal
    
    
    s_bal=u_bal_db(u_tema)
    
    await coll.message.answer(md.text(' З можливих  30 балів ВИ набрали '+md.bold(s_bal)),parse_mode=ParseMode.MARKDOWN)
    await coll.message.answer(text=(' ПРОЙТИ ЩЕ РАЗ(ВІДПОВІДІ З ПОТОЧНОГО ТЕСТУ ВИДАЛЯТЬСЯ)'),reply_markup=u_ikb_dali(tem_cal))
@dp.callback_query_handler(Text(startswith='udal'))
async def vibir_vid_po_u(coll: types.CallbackQuery):  
    u=coll.data.split('!')[-1][0]#u
    tem_cal=(coll.data.split('!')[-1])
    tema=tem_cal
    u_tema=u+str(coll.from_user.id)+u+tem_cal
    u_dddel_db(u_tema)
    await coll.message.answer(text=(f'Ваші відповіді до теми {tema} видалено'),reply_markup=ikb_tema)


def register_handler_test_u(dp: Dispatcher)   :
    # dp.callback_query_handler(vibir_vid_ts2_u)
    # dp.callback_query_handler(next_ts2_u)
    dp.callback_query_handler(temma2_u)
    # dp.callback_query_handler(next_ts20_u)
    dp.callback_query_handler(vibir_vid_ts_u)
    # dp.callback_query_handler(vibir_vid_po_u)



