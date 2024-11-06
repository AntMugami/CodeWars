def xo(s):
    if s.lower().count('x') == s.lower().count('o'): return True
    else: return False
# def xo(s):
#     return True if s.lower().count('x') == s.lower().count('o') else False





print(xo("ooxx")) #=> true
print(xo("xooxx")) #=> false
print(xo("ooxXm"))#=> true
print(xo("zpzpzpp")) #=> true // when no 'x' and 'o' is present should return true
print(xo("zzoo")) #=> false



# def xo(s):
#     return s.lower().count('x') == s.lower().count('o')