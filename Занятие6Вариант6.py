
s = input('Введите строку: ')
count = s.count('a')
new_string = s.replace('a', '')
print(f"Строка после удаления букв 'a': {new_string}")
print(f"Количество удаленных символов 'a': {count}")