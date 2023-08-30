#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 
file_db='multy_test_11.db'
"""*0*********Створення бази - user name**********************************************"""
def u_create_user():
    try:
        with  sqlite3.connect(file_db)as db:
            """We create a database
            \Створюєм  базу даних\ """
            cursor=db.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS user( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, id_user TEXT, name TEXT)"""
            cursor.execute(query)
    except: print('Error1')
"""*4*******************************************************"""
def posh(jj):
    F=False
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f'''SELECT * FROM user ;''')
        for i in record:
            if (i[1])==jj[0]:
                F=True    
        return F 
    
    except :
        print('Error 7')
        return F 
            
def save_user(jj):
    """  \Записуєм id_user та name_user   """
    u_create_user()
    if not posh(jj):
        try:
            with  sqlite3.connect(file_db)as db:
                cursor=db.cursor()
                cursor.executemany(f"INSERT INTO user ( id_user,name ) VALUES(?,?)",(jj,)) 
        except:  print('Не записав №  --',jj) 
        

def u_create_db_test(tema):
    try:
        with  sqlite3.connect(file_db)as db:
            """We create a database
            \Створюєм  базу даних\ """
            cursor=db.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS {tema}( 
            nume_test INTEGER PRIMARY KEY AUTOINCREMENT, it_user TEXT, num_zav TEXT, vidpoid TEXT, bal TEXT)"""
            cursor.execute(query)
    except: print('Error1')
"""*2*******************************************************"""
def u_chit_db(tema):
    """ ф-я зчитує 
    nume_test , num_zav, umova TEXT, vidpoid, bal"""
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f"SELECT * FROM {tema}  ")
        return (record)
    except : print('Error2')
tema='matematyka_2'    

"""*3*******************************************************"""
def u_del_zv_db(tema,j):
    """  Видаляє з таблиці радок j """
    print('Видаляю ',j)
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.execute(f'''DELETE FROM {tema} WHERE num_zav = ?''', (j,))
    except: print('Error3')
"""*4*******************************************************"""
def u_save_v_db_tema(u_tema,jj):
    """  \Записуєм в  номер завдання, відповідь і бал  """
    u_create_db_test(u_tema)
    try:
        print('Записую',jj,'в тему', u_tema)
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.executemany(f"INSERT INTO {u_tema} ( it_user,num_zav,vidpoid,bal ) VALUES(?,?,?,?)",(jj,)) 
    except:  print('Не записав №  --',jj)  
"""*5*******************************************************"""
def u_bal_db(u_tema):
    try:
        """ ф-я рахує суму балів за всі завдання з даної теми"""
        print('u_tema=',u_tema)
        with  sqlite3.connect(file_db)as db:
                cursor=db.cursor()
                record=cursor.execute(f'''SELECT * FROM {u_tema}''')
        s_bal=0   
        for i in record:
            if i[4].isdigit():
                s_bal+=int(i[4])
        return s_bal
    except:print('Error20')
tema='m815653794m1'
def u_dddel_db(tema):
    """  Видаляє  таблиці  """
    print('Видаляю ',tema)
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.execute(f'''DELETE FROM {tema} ''')
    except: print('Error7')

"""*6*******************************************************"""
def u_zav_db(tema):
    """ ф-я видає останнє завдання з даноъ теми"""
    min=1 
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f'''SELECT * FROM {tema} ;''')
        for i in record:
            if int(i[2])>min:
                min =int(i[2])
        return min
    except :
        # print('min+1=',min+1)
        return min 
"""*7*******************************************************"""
def u_del_db(tema,it_user):
    """ ф-я видаляє всі завдання з даної теми"""
    u_zav_db(tema)
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f'''DELETE  FROM {tema} ;''')
    except : print('Error4') 

def u_vid(tema,vd,bal):
    num=u_zav_db(tema)-1
    try:
        with  sqlite3.connect(file_db)as db:
                cursor=db.cursor()
                cursor.execute(f'''UPDATE {tema} SET vidpoid = ?,  bal=?  WHERE num_zav = {str(num)}  ''',(vd,bal))
    except : print('Error7')     
    
def did1(a,b):
    try:
        if a==b:
            return str(1)
        else: return str(0)
    except:
        print('Eror did1')