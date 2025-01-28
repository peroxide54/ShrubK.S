
array = [int(input(f"Введите элемент {i+1}: ")) for i in range(10)]
sum_greater_than_5 = sum(x for x in array if x > 5)
print(f"Сумма чисел, которые больше 5: {sum_greater_than_5}")