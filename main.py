element_of_alphabet = ord('А')
alphabet = [chr(i) for i in range(element_of_alphabet, element_of_alphabet + 32)]
alphabet.remove('Ъ')

dict_alphabet = {}  # Создаем зависимость между буквой в алфавите и его позицией
count = 1
for i in alphabet:
    dict_alphabet[i] = count
    count += 1

print(dict_alphabet)

def get_seq_key(key, text):  # Функция по созданию строки из ключей такой же длиной как зашифрованное слово
    seq_key = ''
    count = 0
    while len(seq_key) < len(text):
        seq_key += key[count]
        count += 1
        if count >= len(key):
            count = 0

    return seq_key


def create_of_num_seq(_str, dict_alphabet = dict_alphabet):  # Создание списка с записями позиций каждой буквы из входящего слова
    _list = list()
    for i in _str:
        _list.append(dict_alphabet[i])

    return _list

def decoder(_list_of_result, dict_alphabet=dict_alphabet): # Перевод из последовательности цифр обратно в строку
    _str = ''
    for i in _list_of_result:
        for k, v in dict_alphabet.items():
            if i == v:
                _str += k

    return _str


text = input('Введите слово которое необходимо зашифровать:\n').upper()
key = input('Введите ключ:\n').upper()

while len(key) > len(text):
    key = input('Введеный ключ длиньше чем итоговое слово, введите ключ короче\n').upper()

seq_key = get_seq_key(key=key, text=text)

_list_text = create_of_num_seq(text)
_list_seq_key = create_of_num_seq(seq_key)
_list_of_result = list()

for i in range(len(text)):
    sum = _list_seq_key[i] + _list_text[i]
    if sum > len(text):
        sum  = sum % len(alphabet)
    _list_of_result.append(sum)

result = decoder(_list_of_result)

print()
print(f'{text}')
print(f'{seq_key}')
print(f'{result}')