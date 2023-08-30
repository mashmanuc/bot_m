"""*1*********Створення бази - user  тестів**********************************************"""
import sqlite3 
file_db='multy_test_11.db'
t= ['Завдання 3333', 'https://zno.osvita.ua/doc/images/znotest/63/6312/Matematika_126_32.png', None, ['Правильна відповідь: 110.5']]
tema='matematyka_2'
"""*1*******************************************************"""

def create_db_tema(tema):
    try:
        with  sqlite3.connect(file_db)as db:
            """We create a database
            \Створюєм  базу даних\ """
            cursor=db.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS {tema}( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, num_zv TEXT, img_zv TEXT, text_zv TEXT, vidpoid TEXT)"""
            cursor.execute(query)
    except: print('Error create_db_tema')
"""*2*******************************************************"""
def  save_v_db(tema,*jj):
    """  \Записуєм в  номер завдання, відповідь і бал  """
    create_db_tema(tema)
    try:       
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.executemany(f"INSERT INTO {tema} ( num_zv, img_zv , text_zv, vidpoid ) VALUES(?,?,?,?)",(jj))  
    except: print('Error  save_v_db_tema')

def chit_tema_db(tema,num_zv):
    """ ф-я зчитує 
    nume_test , num_zav, umova TEXT, vidpoid"""
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f"SELECT * FROM {tema} WHERE num_zv= 'Завдання {num_zv}';  ")
        return tuple(record)
    except : print('Error2')
def chit_vid(tema,num_zv):
    """ Ф-я повертає правильну відповідь з бази та тип завдання->(1,2,3)"""
    v=chit_tema_db(tema,num_zv)
    if 'відповідь' in (v[0][4]).strip():
        return (v[0][4]),3
    elif (not 'відповідь' in (v[0][4]).strip())and(len((v[0][4]))==15):
        return (v[0][4]),1
    else:
        return (v[0][4]),2

def create_db_tema(tema):
    try:
        with  sqlite3.connect(file_db)as db:
            """We create a database
            \Створюєм  базу даних\ """
            cursor=db.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS {tema}( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, num_zv TEXT, img_zv TEXT, text_zv TEXT, vidpoid TEXT)"""
            cursor.execute(query)
    except: print('Error create_db_tema')

def create_name_tema():
    try:
        with  sqlite3.connect(file_db)as db:
            """ \Створюєм  базу даних\ """
            cursor=db.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS name_tema( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, call TEXT)"""
            cursor.execute(query)
    except: print('Error create_name_tema')
def  save_name_tema(*jj):
    """  \Записуєм в  номер завдання, відповідь і бал  """
    create_name_tema()
    try:       
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.executemany(f"INSERT INTO name_tema ( name, call  ) VALUES(?,?)",(jj))  
    except: print('Error  save_name_tema')   

def chit_name_tema():
    """ ф-я зчитує     name, call"""
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f"SELECT * FROM name_tema  ")
        return tuple(record)
    except : print('Error2') 
# for i in chit_name_tema():
#     print(i)