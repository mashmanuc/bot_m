file_db='multy_test_11.db'
import sqlite3 
def create_bufer(tema_b):
    try:
        with  sqlite3.connect(file_db)as db:
            """ \Створюєм  базу даних\ """
            cursor=db.cursor()
            query = f"""CREATE TABLE IF NOT EXISTS {tema_b}( 
            nume_test INTEGER PRIMARY KEY AUTOINCREMENT, it_user TEXT, num_zav TEXT, vidpovid TEXT, bukva TEXT)"""
            cursor.execute(query)
            print('Створено буфер')
    except: print('Error1')
    
def del_buf(tema,j):
    """  Видаляє з таблиці радок j """
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.execute(f'''DELETE FROM {tema} WHERE num_zav = ?''', (j,))
    except: print('Error3')    
def save_buf(u_tema,jj):
    """  \Записуєм в  номер завдання, відповідь і буква  """
    create_bufer(u_tema)
    del_buf(u_tema,jj[1])
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.executemany(f"INSERT INTO {u_tema} ( it_user,num_zav,vidpovid, bukva ) VALUES(?,?,?,?)",(jj,)) 
    except:  print('Error7')


def chit_buf(tema):
    """ ф-я зчитує 
    nume_test , num_zav, umova TEXT, vidpoid, bal"""
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f"SELECT * FROM {tema} ORDER BY num_zav")
        return  tuple(record)
    except : return [print('Error2') ] 


def del_all_buf(tema):
    """  Видаляє з таблиці радок j """
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            cursor.execute(f'''DELETE FROM {tema} ''')
            print('Буфер очищено')
    except: print('Error3') 

def mas_vid(tema_b):
    try:
        g=chit_buf(tema_b)
        k=''    
        for i in range(len(g)):
            if i<len(g)-1:
                k=k+(g[i][3].split('[')[-1].split(']')[0])+','
            elif i==len(g)-1:
                k=k+(g[i][3].split('[')[-1].split(']')[0])
        return (k)
    except: return [0,' ',' ',' ',' ']
 
