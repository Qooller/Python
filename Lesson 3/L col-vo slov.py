# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных символов идущих подряд, слова
# разделены одним или большим числом пробелов или символами конца строки.
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
# Определите, сколько различных слов содержится в этом тексте.
# a = "She sells sea shells on the sea shore; " \
#    "The shells that she sells are sea shells I'm sure. " \
#    "So if she sells sea shells on the sea shore, " \
#    "I'm sure   that the shells are sea shore shells."

a = open('input.txt', 'r')
b = a.read()
c = b.split("\n")
d = " ".join(map(str, c))
f = d.split(' ')
if '' in f:
    print(len(set(f)) - 1)
else:
   print(len(set(f)))


#g = a.readline().strip().split(" ")
#word_count = set(g)

#a.close()
#print(word_count)
#print(len(word_count))



