numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
i = 0
TheIndex = 0
length: int = len(numbers)
for i in range(length):
    i = i+1
    if numbers[i] is None:
        TheIndex = i
        numbers[TheIndex] = 0
        break
Summary: int = sum(numbers)
result: float = Summary/length
numbers[TheIndex] = result
print("Измененный список:", numbers)
