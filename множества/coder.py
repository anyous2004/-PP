'''
Кодирование строк.
На вход подается строка, например: “ААААBBBCCF”
напишите программу, кодирующую эту строку по принципу: “4A3B2C1F”
'''

string = input('[+] Введите строку: ')

result = []
for ch in string:
    num = string.count(ch)
    if f'{num}{ch}' not in result:
        result.append(f'{num}{ch}')

print(''.join(result))
