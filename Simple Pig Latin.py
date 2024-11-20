def pig_it(text):
    text_list = []
    el = 0
    
    text_list = text.split(' ')
    print(text_list)
    for i in text_list:
    #    print(text_list, '\n')
        # print(i)
        # if i not in ['!', '.', '?']:
        if i.isalpha():
            text_list[el] = i[1:] + i[0] + 'ay'
            el += 1
    
    return " ".join(word for word in text_list)
    

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !') )

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])