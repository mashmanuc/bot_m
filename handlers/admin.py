from aiogram import types,  Dispatcher
from create_bot import dp, bot,ad
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from d_b import save_v_db , chit_user, chit_us_t,tema_a,chit_tema_us
from keyboards import ikb_ad,us_list

"""********************************************************************************"""
def adm(admin):
    if str(admin)==ad:
        return True
    else:
        return False
"""********************************************************************************"""
class a_d(StatesGroup):
    tema=State()
    num_zav=State()
    photo=State()
    vid=State()

pred='istorija_ukrayiny_'
"""********************************************************************************"""
@dp.message_handler(commands='basa')
async def cmd_start(message: types.CallbackQuery):
    await message.answer("tema",reply_markup=ikb_ad)
'''***********************************************************************************'''

@dp.callback_query_handler(Text(startswith='ttema!'))
async def cmd_start_t(coll: types.CallbackQuery):
    if adm(coll.from_user.id):
        await a_d.tema.set()
        await coll.message.answer("tema")
"""******************************"tema"**************************************************"""
@dp.message_handler(state=a_d.tema)
async def process_tema(message: types.Message, state: FSMContext):
    if adm(message.from_user.id):
        async with state.proxy() as data:
            data['tema'] = message.text
        await a_d.next()
        await message.answer("num")
"""*******************"num_zav"*************************************************************"""
@dp.message_handler(state=a_d.num_zav)
async def process_num_zav(message: types.Message, state: FSMContext):
    if adm(message.from_user.id):
        async with state.proxy() as data:
            data['num_zav'] = message.text
        await a_d.next()
        await message.answer("photo")
"""************************"photo********************************************************"""
@dp.message_handler(content_types=['photo'],state=a_d.photo)
async def process_photo(message: types.Message, state: FSMContext):
    if adm(message.from_user.id):
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await a_d.next()
        await message.answer("vid")
"""************************vid********************************************************"""
@dp.message_handler(state=a_d.vid)
async def process_vid(message: types.Message, state: FSMContext):
    if adm(message.from_user.id):
        async with state.proxy() as data:
            data['vid'] = message.text
            u_tema=pred+ data['tema']
            r=['Завдання '+data['num_zav'],'',data['photo'],data['vid']]
            save_v_db(u_tema,r)
        await state.finish()
        await message.answer("Yes",reply_markup=ikb_ad)
'''***********************************************************************************'''
@dp.callback_query_handler(Text(startswith='usery'))
async def cmd_uaery(coll: types.CallbackQuery):
    if adm(coll.from_user.id):
        for i in chit_user():
            markup=us_list(i[2],'uscoll!'+i[1])
            await coll.message.answer('Результат',reply_markup=markup)
'''***********************************************************************************'''
@dp.callback_query_handler(Text(startswith='uscoll!'))
async def tem_uaery(coll: types.CallbackQuery):
    id_us=coll.data.split('!')[-1]
    if adm(coll.from_user.id):
        for i in chit_us_t(id_us):
            markup=us_list(tema_a(i),'us_tema!'+i+'!'+id_us)
            await coll.message.answer('Результат',reply_markup=markup)
'''***********************************************************************************'''
@dp.callback_query_handler(Text(startswith='us_tema!'))
async def tem_ress(coll: types.CallbackQuery):
    id_us=coll.data.split('!')[-1]
    tema=coll.data.split('!')[1]
    if adm(coll.from_user.id):
        for i in chit_tema_us(tema):
            print(i)
            # markup=us_list((i[1],i[3],i[1]),'us_tema!'+id_us)
            await coll.message.answer('Завдання  '+i[2]+'     bal='+i[-1])
    await coll.message.answer('r',reply_markup=ikb_ad)



def register_handler_admin(dp: Dispatcher)   :
    dp.message_handler(cmd_start)
    dp.callback_query_handler(cmd_start_t)
    dp.message_handler(process_tema)
    dp.message_handler(process_num_zav)
    dp.message_handler(process_photo)
    dp.message_handler(process_vid)
    dp.callback_query_handler(cmd_uaery)
    dp.callback_query_handler(tem_uaery)
    dp.callback_query_handler(tem_ress)

