#1.1#####################################
# Открытие файла и чтение второй строки
with open('input.txt', 'r') as f:
    lines = f.readlines()
    number = int(lines[1])

# Проверка попадания числа в диапазон
if (number >= 1 and number <= 100) or (number >= 200 and number <= 300):
    result = 'число попадает в диапазон от 1 до 100 или от 200 до 300 включительно'
else:
    result = 'число не попадает в диапазон от 1 до 100 или от 200 до 300 включительно'

# Вывод результата на экран и запись в файл
output = f'Задача1.1:\n{result}'
print(output)
with open('output.txt', 'a') as f:
    f.write(output + '\n')

#1.2######################################

# Открываем файл input.txt и считываем четвертую строку
with open('input.txt') as f:
    lines = f.readlines()
water_temperature = int(lines[3])

# Инициализируем переменную для хранения времени и начальную температуру воды
time = 0
temperature = water_temperature

# Увеличиваем температуру каждые 2 минуты на 1 градус до тех пор, пока она не достигнет 100 градусов
while temperature < 100:
    temperature += 1
    time += 2

# Выводим результат на экран и записываем его в файл output.txt
result = f'Задача1.2:\n{time} минут\n'
print(result)
with open('output.txt', 'a') as f:
    f.write(result)

#1.3##################################################

# Открываем файл input.txt для чтения
with open('input.txt', 'r') as f:
    # Читаем все строки файла в список
    lines = f.readlines()
    # Получаем значение X из шестой строки
    X = int(lines[5])

# Открываем файл output.txt для добавления данных в конец файла
with open('output.txt', 'a') as f:
    # Выводим заголовок задачи
    print('Задача 1.3:')
    # Записываем заголовок задачи в файл
    f.write('Задача 1.3:\n')

    # Выводим и записываем X строк с тремя нулями
    for i in range(1, X + 1):
        # Формируем строку с номером и тремя нулями
        line = f'{i}. 000'
        # Выводим строку на экран
        print(line)
        # Записываем строку в файл с переводом строки
        f.write(line + '\n')

#1.4###################################################
# Открываем файл для чтения и считываем высоту треугольника
with open('input.txt', 'r') as f:
    height = int(f.readlines()[7])

# Открываем файл для записи и выводим заголовок задачи
with open('output.txt', 'a') as f:
    f.write('Задача1.4:\n')

    print("Задача1.4:")

    # Рисуем треугольник и выводим его на экран и в файл
    for i in range(height):
        for j in range(i+1):
            print('*', end='')
            f.write('*')
        print()
        f.write('\n')


#2.1#####################################################
# Чтение данных из файла input.txt
with open('input.txt', 'r') as f:
    data = f.readlines()
    a = int(data[9])
    b = int(data[10])
    c = int(data[11])
    m = int(data[12])
    k = int(data[13])

# Сравнение размеров коробки и двери
if a <= m and b <= k:
    if c <= k:
        result = "Коробка войдет в дверь"
    else:
        result = "Коробка не войдет в дверь"
else:
    result = "Коробка не войдет в дверь"

# Вывод результата на экран и запись в файл output.txt
print("Задача2.1: " + result)
with open('output.txt', 'a') as f:
    f.write("\n" + "Задача2.1:\n" + result)

#2.2############################################
# Open the input file and read the 16th line
with open('input.txt', 'r') as file:
    lines = file.readlines()
    height = int(lines[15].strip())

# Build the isosceles triangle using nested loops
triangle = ''
for i in range(height):
    for j in range(height-i-1):
        triangle += ' '
    for k in range(2*i+1):
        triangle += '*'
    triangle += '\n'

print("Задача2.2")

# Print the triangle to the console
print(triangle)

# Append the triangle to the output file
with open('output.txt', 'a') as file:
    file.write('\nЗадача2.2:\n')
    file.write(triangle)

#2.3###########################################
# Открываем файл для чтения и считываем значение N из 18-ой строки
with open('input.txt', 'r') as f:
    lines = f.readlines()
    n = int(lines[17])

# Предположим, что последовательность квадратов уже определена в программе или загружена из другого файла
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Создаем пустой список, в который будем добавлять числа, меньшие N
result = []
for square in squares:
    if square < n:
        result.append(square)

# Выводим результат на экран
print("Задача2.3:")
print(result)

# Открываем файл для дополнительной записи и записываем результат
with open('output.txt', 'a') as f:
    f.write("Задача2.3:\n")
    f.write(str(result))
    f.write("\n")

#3.1#################################################
# Читаем данные из файла input.txt
with open('input.txt', 'r') as f:
    line = f.readlines()[19]  # строка с количествами шариков

# Преобразуем строку в список чисел
counts = list(map(int, line.strip().split()))

# Проверяем, можно ли купить ровное количество шариков мороженного
total = sum(counts)
if total % 2 == 0:
    answer = "да"
else:
    answer = "нет"

# Выводим ответ на экран и записываем его в файл output.txt
print(f"Задача3.1: Можно ли купить ровное количество шариков мороженого? {answer}")
with open('output.txt', 'a') as f:
    f.write(f"\nЗадача3.1:\nМожно ли купить ровное количество шариков мороженого? {answer}\n")

#3.2#################################################
# Чтение данных из файла
with open('input.txt', 'r') as f:
    lines = f.readlines()
    D = int(lines[21])
    Y = float(lines[22])
    Z = int(lines[23])

# Расчет количества лет
import math
t = math.log(Z/D) / math.log(1 + Y/100)

# Вывод результата
print(f'Задача3.2: {round(t, 2)} лет')
with open('output.txt', 'a') as f:
    f.write(f'Задача3.2:\n{round(t, 2)} лет\n')

#3.3#################################################
# Шаг 1: Чтение входных данных из файла
with open("input.txt", "r") as f:
    W = int(f.readlines()[25])

# Шаг 2: Вычисление суммы цифр числа W
sum_digits = sum(int(digit) for digit in str(W))

print("Задача3.3:")

# Шаг 3: Вывод результата на экран
print(sum_digits)

# Шаг 4: Запись результата в файл output.txt
with open("output.txt", "a") as f:
    f.write(f"Задача3.3:\n{sum_digits}\n")


#python task_4.py