def order(sentence):
  words_list = sentence.split()
  print(words_list)
  sorted_list = []
  for i in range(len(words_list)):
      for word in words_list:
          if str(i+1) in word:
              sorted_list.append(word)
  return ' '.join(sorted_list)

# def order(words):
#   return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))


# def extract_number(word):
#     for l in word:
#         if l.isdigit(): return int(l)
#     return None
#
# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=extract_number))


# def order(sentence):
#   return " ".join(sorted(sentence.split(), key=min))


print(order("is2 Thi1s T4est 3a")) # , "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2")) # , "Fo1r the2 g3ood 4of th5e pe6ople"