
array = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]
average = sum(array) / len(array)
max_element = max(array)
count = sum(1 for x in array if x < max_element and x > average)
print(f"Среднее арифметическое: {average}")
print(f"Количество элементов, меньших максимального ({max_element}) и больших среднего арифметического: {count}")