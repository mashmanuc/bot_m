
from aiogram.utils import executor
from create_bot import dp
print('''Bottttttttttt''')
from handlers import  admin,test_m,test_u, other
admin.register_handler_admin(dp)
test_m.register_handler_test_m(dp)
test_u.register_handler_test_u(dp)
other.register_handler_other(dp)
 
if __name__=='__main__':
    executor.start_polling(dp) 
    
     