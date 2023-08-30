st=' cv'
g=[(s) for s in st if s.isdigit()or(s=='.')or(s==',')]


def cif(st):
    si=''
    for s in st:
        if   s.isdigit()or(s=='.')or(s==','):
            si=si+s
    return si    

