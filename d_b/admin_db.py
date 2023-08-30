import sqlite3 
file_db='multy_test_11.db'
"""*1*******************************************************"""

def chit_user():
    """ ф-я зчитує 
    id_user, name"""
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f"SELECT * FROM user")
        return tuple(record)
    except : print('Error2')
"""*2*******************************************************"""
def tema_a(tem):
    num= tem[-1]
    if 'mova' in tem:
        return 'Укр мова '+num
    elif 'istor' in tem:
        return 'Історія '+num
    else: return 'Математика '+num
        

"""*3*******************************************************"""

# for i in chit_user():
#     print(i[1])
    
    
    
    
def chit_us_t(ii='815653794'):
    """ ф-я зчитує 
    id_user, name"""
    data=[]
    try:
        with  sqlite3.connect(file_db)as db:
                cursor=db.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                record=cursor.fetchall()
                d=[a[0] for a in record  if a[0].find(ii)!=-1]
                for j in record:
                    if ii in j[0]:
                        data.append(j[0])
                return d
    except : print('Error22')


def chit_tema_us(tema):
    """ ф-я зчитує 
    nume_test , num_zav, umova TEXT, vidpoid"""
    try:
        with  sqlite3.connect(file_db)as db:
            cursor=db.cursor()
            record=cursor.execute(f"SELECT * FROM {tema}  ")
        return tuple(record)
    except : print('Error23')


