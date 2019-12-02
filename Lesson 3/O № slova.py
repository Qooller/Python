# Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается
# последовательность непробельных символов идущих подряд, слова разделены одним или большим
# числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Примеры
# входные данные
# one two one tho three
# выходные данные
# 0 0 1 0 0
# входные данные
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
# выходные данные
# 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0
a = open(r'input.txt', 'r')
#b = a.read()
#a.close()
#p = []
#q = []
#b = b.strip()
#c = b.split("\n")
#d = " ".join(map(str, c))
#f = d.split(' ')
#for i in f:
#    p.append(i)
#    q.append(p.count(i)-1)

##if '' in f:
##    print(len(set(f)) - 1)
##else:
##    print(len(set(f)))

#print(" ".join(map(str, q)))


g = a.readline().strip().split(" ")
word_count = {}

for word in g:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
print(len(word_count))

