

vid='[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]'
# v1='[0, 1, 0, 0, 0]'
v2='dffd'
v3='[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]'

    
t1='[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]'
t2='0,0,0,1,0,0,1,0,0,0,0,0,0,0,1'
m1=[]
for i in t1:
    # print(i)
    pass
def did2(t1,t2):
    def ggg(vid):
        """Ф-я перетворює рядок в числовий масив масивів
        '[0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]'
        ----->
        [0, 0, 0, 0, 1]
        [0, 0, 0, 1, 0]
        [1, 0, 0, 0, 0]
        """
        g=[int(s) for s in vid if s.isdigit()]
        mas=[]
        k=0
        while k<len(g)//5:
            dor=[g[j] for j in range(k*5,k*5+5)]
            k=k+1
            mas.append(dor)
        return mas 
    bal=0
    try:
        for i in range(3):
            if (ggg(t1)[i])==(ggg(t2)[i]):
                bal+=1
        return bal
    except: return bal
   
# print(did2(t1,t2))
"""************************************"""
abc=['А','Б','В','Г','Д']
def vid2(im=' '):

    try:
        num=im.split('?')[-1]
        i=im.split('?')[0]
        if i=='А':
            return '[1,0,0,0,0]'
        if i=='Б':
            return '[0,1,0,0,0]'
        if i=='В':
            return '[0,0,1,0,0]'
        if i== 'Г':    
            return '[0,0,0,1,0]'
        if i=='Д':    
            return '[0,0,0,0,1]'
    except: 
         pass
im='А?1'
# print(vid2('А?1'))
v1='[0, 1, 0, 0, 0]'
# v1="['Правильна відповідь: -8']"
def prap(v1):
    # print(len(v1))
    if len(v1)==15 and ']' in v1:
        return 1
    elif  'Правильна відповідь:' in v1:
        return 3
    else:
        return 2
    
def did3(t1,t2):
    g1=[int(s) for s in t1 if s.isdigit()]
    g2=[int(s) for s in t2 if s.isdigit()]
    if g1==g2:
        return str(2)
    else:
      return str(0)
