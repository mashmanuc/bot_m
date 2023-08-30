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
   
