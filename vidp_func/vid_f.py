abc=['А','Б','В','Г','Д']

def vid(i=' '):
    try:
        if i=='А':
            return '[1, 0, 0, 0, 0]'
        if i=='Б':
            return '[0, 1, 0, 0, 0]'
        if i=='В':
            return '[0, 0, 1, 0, 0]'
        if i== 'Г':    
            return '[0, 0, 0, 1, 0]'
        if i=='Д':    
            return '[0, 0, 0, 0, 1]'
    except: 
        return '[0, 0, 0, 0, 0]'

def abc_f(i=' '):
    f1=False
    if i in abc:
        f1=True
    return f1
def vid_u1(l_vid=1 , i=' '):
    if l_vid==1:
        try:
            if i=='А':
                return '[1, 0, 0, 0]'
            if i=='Б':
                return '[0, 1, 0, 0]'
            if i=='В':
                return '[0, 0, 1, 0]'
            if i== 'Г':    
                return '[0, 0, 0, 1]'
            
        except: 
            return '[0, 0, 0, 0]'
    else :
        try:
            if i=='А':
                return '[1, 0, 0, 0, 0]'
            if i=='Б':
                return '[0, 1, 0, 0, 0]'
            if i=='В':
                return '[0, 0, 1, 0, 0]'
            if i== 'Г':    
                return '[0, 0, 0, 1, 0]'
            if i=='Д':    
                return '[0, 0, 0, 0, 1]'
        except: 
            return '[0, 0, 0, 0, 0]'
