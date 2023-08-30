def f_tem(buc):
    if buc=='u':
        return 'ukrayinska_mova_'
    if buc=='m':
        return 'matematyka_'
# print(vid2('А?1'))
v1='[0, 1, 0, 0, 0]'
v1='[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0]'
# v1="['Правильна відповідь: -8']"

def prap_u(v1):
    # print(len(v1))
    if len(v1)==12 and ']' in v1:
        return 1
    
    elif  len(v1)==15 and ']' in v1:
        return 2
    
    else:
        return 3
  