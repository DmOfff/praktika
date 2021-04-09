# Переставить и вывести на экран слова заданного предложения в соответствии с ростом доли согласных в этих словах.

consonants = 'бвгджзйклмнпрстфхцчшщ'


def get_num_of_consonants(s):
    return sum(s.count(x) for x in consonants)


ss = input().split(' ')

ss.sort(key=lambda s: get_num_of_consonants(s.lower()))

print(ss)
