#Напишите функцию, которая определяет сумму цифр переданного ей числа (например, входные данные - число 126,
#  выходные - число 9, так как 1 + 2 + 6 равно 9)
def sum_num_str(x: int):
    y = str(x)
    summ = 0
    for i in range(len(y)):
        j = int(y[i])
        summ += j
    return summ


z = (input("Введите число"))
z1 = sum_num_str(z)
print(z1)

#напишите функцию count_words(), которая принимает список строк и возвращает int число уникальных слов в этом списке
# list_of_strings = ['hello', 'hi', 'hello', 'goodbye', 'chao', 'hi']
#result_number = count_words(list_of_strings)
#print(result_number) # на экран появится 4

def count_words(l):
    count = 0
    for i in range(len(l)):
        c = l.count(l[i]) - 1
        count = count + c
    return count

list_of_strings = ['hello', 'hi', 'hello', 'goodbye', 'chao', 'hi']
result_number = count_words(list_of_strings)
print(result_number) # на экран появится 4







