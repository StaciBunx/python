# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def check_double(list_elements, search_string):
    count = 0
    for index in range(len(list_elements)):
        if search_string == list_elements[index]:
            count += 1
        if count == 2:
            print(index)
            break


check_double(['qwe', 'asd', 'qwe', 'adsgasg'], 'qwe')
