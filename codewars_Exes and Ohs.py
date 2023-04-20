def xo(s):
    a = []
    s = s.lower()
    if len(s) != 0:
        for i in s:
            a.append(i)
        x = a.count('x')
        o = a.count('o')
        if x == o and (x != 0 and o != 0):
            return True
        else:
            return False
    else:
        return True

#тесты
#assert xo('xo') == True
#assert xo('xxoo') == True
#assert xo('xxxoo') == False
#assert xo('xoxoxoxoxo') == True
#assert xo('xoxoxoxoxox') == False
#assert xo('1xoxoooxo') == False
#assert xo('xoxoxoxoxox ') == False
#assert xo('OOXxxxOO') == True
#assert xo('abcd') == False
#assert xo('x1o2x3o4') == True


#другой способ решения

def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')