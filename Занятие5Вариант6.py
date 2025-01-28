
total_sum = 0
count = 0
num = int(input("Введите число (0 для завершения): "))
while num != 0:
    total_sum += num
    count += 1
    num = int(input("Введите следующее число (0 для завершения): "))
if count > 0:
    average = total_sum / count
    print(f"Среднее значение: {average}")
else:
    print("Последовательность не содержит элементов.")