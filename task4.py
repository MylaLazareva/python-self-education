#1.1
def check_number_in_range(num):
    if (1 <= num <= 100) or (200 <= num <= 300):
        return True
    else:
        return False

def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        num = int(lines[1])
        if check_number_in_range(num):
            print("Задача1.1: \nЧисло попадает в заданный диапазон")
            with open("output.txt", "w") as f2:
                f2.write("Задача1.1: \nЧисло попадает в заданный диапазон\n")
        else:
            print("Задача1.1: \nЧисло не попадает в заданный диапазон")
            with open("output.txt", "w") as f2:
                f2.write("Задача1.1: \nЧисло не попадает в заданный диапазон\n")

if __name__ == "__main__":
    main()


#1.2
def read_data(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        temp = int(lines[3])
        return temp

def calculate_time(temp):
    boiling_point = 100
    rate = -0.5
    if temp >= boiling_point:
        return 0
    else:
        time = abs((boiling_point - temp) / rate)
        return time


def write_output(file_name, time):
    with open(file_name, 'a') as f:
        f.write('\nЗадача 1.2:\n')
        f.write(f'Время закипания воды: {time:.2f} минут\n')
        print(f'\nЗадача 1.2:\nВремя закипания воды: {time:.2f} минут')

temp = read_data('input.txt')
time = calculate_time(temp)
write_output('output.txt', time)


#1.3
def generate_row(row_number):
    """
    Функция генерирует строку из трех нулей с указанным номером
    """
    return f"{row_number}: 000"


def main():
    """
    Основная функция программы
    """
    with open("input.txt") as f:
        # Считываем данные из файла
        x = int(f.readlines()[5])

    # Выводим заголовок задачи
    print("\nЗадача1.3:")

    # Открываем файл для записи
    with open("output.txt", "a") as f:
        # Записываем строку перед результатом
        f.write("\nЗадача1.3:\n")

        for i in range(1, x + 1):
            # Генерируем строку и выводим ее на экран
            row = generate_row(i)
            print(row)

            # Записываем строку в файл
            f.write(row + "\n")


if __name__ == "__main__":
    # Запускаем основную функцию программы
    main()


#1.4
def read_height():
    with open('input.txt') as f:
        for i, line in enumerate(f):
            if i == 7:
                return int(line.strip())

def create_triangle(height):
    triangle = ''
    for i in range(1, height+1):
        triangle += '*' * i + '\n'
    return triangle

def write_output(triangle):
    with open('output.txt', 'a') as f:
        f.write('\nЗадача1.4: \n' + triangle + '\n')
    print('\nЗадача1.4: ')
    print(triangle)

height = read_height()
triangle = create_triangle(height)
write_output(triangle)

#2.1


def read_input_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) < 14:
            raise ValueError("Not enough lines in input file")
        try:
            a = int(lines[9])
            b = int(lines[10])
            c = int(lines[11])
            m = int(lines[12])
            k = int(lines[13])
        except ValueError:
            raise ValueError("Invalid input values")
        return a, b, c, m, k

def box_fits_door(a, b, c, m, k):
    if a <= m and b <= k:
        return "Да"
    elif b <= m and a <= k:
        return "Да"
    elif a <= m and c <= k:
        return "Да"
    elif c <= m and a <= k:
        return "Да"
    elif b <= m and c <= k:
        return "Да"
    elif c <= m and b <= k:
        return "Да"
    else:
        return "Нет"


def write_output_file(result):
    with open('output.txt', 'a') as f:
        f.write("Задача2.1:\n" + result + "\n")
    print("Задача2.1:\n" + result)


if __name__ == '__main__':
    a, b, c, m, k = read_input_file('input.txt')  # pass the filename argument
    result = box_fits_door(a, b, c, m, k)
    write_output_file(result)

#2.2
def get_triangle_height():
    with open("input.txt") as f:
        lines = f.readlines()
    height_hex = lines[15].strip() # берем шестнадцатую строку и удаляем символы переноса строки и пробелы
    return int(height_hex, 16) # переводим шестнадцатеричное число в десятичное и возвращаем его

def print_triangle(height):
    for i in range(1, height+1):
        print(" "*(height-i) + "*"*(2*i-1))

height = get_triangle_height()
print("\nЗадача2.2:")
with open("output.txt", "a") as f:
    f.write("\n")
    f.write("Задача2.2:\n")
    for i in range(1, height+1):
        row = " "*(height-i) + "*"*(2*i-1) + "\n"
        f.write(row)
        print(row, end="")

#2.3
def read_n():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[17])
    return n

def read_squares():
    # Предположим, что последовательность квадратов уже определена в программе или загружена из другого файла
    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    return squares

def select_numbers_less_than_n(numbers, n):
    # Создаем пустой список, в который будем добавлять числа, меньшие n
    result = []
    for number in numbers:
        if number < n:
            result.append(number)
    return result

def write_output(result):
    # Открываем файл для дополнительной записи и записываем результат
    with open('output.txt', 'a') as f:
        f.write("\nЗадача2.3:\n")
        f.write(str(result))
        f.write("\n")

    # Выводим результат на экран
    print("\nЗадача2.3:")
    print(result)

n = read_n()
squares = read_squares()
result = select_numbers_less_than_n(squares, n)
write_output(result)


#3.1 новый функций
def can_buy_even_number_of_ice_cream_balls(num_balls):
    return num_balls % 2 == 0

def get_num_balls_to_buy():
    with open('input.txt') as input_file:
        num_balls_to_buy = int(input_file.readlines()[19].strip())
    return num_balls_to_buy

def write_result_to_output_file_and_print(can_buy_even):
    with open('output.txt', 'a') as output_file:
        output_file.write('\nЗадача3.1: \nМожно ли купить ровное количество шариков мороженого?\n')
        output_file.write('Ответ: {}\n'.format('да' if can_buy_even else 'нет'))

    print('\nЗадача3.1: \nМожно ли купить ровное количество шариков мороженого?')
    print('Ответ: {}'.format('да' if can_buy_even else 'нет'))

num_balls_to_buy = get_num_balls_to_buy()
can_buy_even = can_buy_even_number_of_ice_cream_balls(num_balls_to_buy)
write_result_to_output_file_and_print(can_buy_even)


#3.2
import math

def read_input_file():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        D = int(lines[21])
        Y = float(lines[22])
        Z = int(lines[23])
    return D, Y, Z

def calculate_years(D, Y, Z):
    t = math.log(Z/D) / math.log(1 + Y/100)
    return t

def write_output_file(t):
    with open('output.txt', 'a') as f:
        f.write('\nЗадача3.2:\n')
        f.write(f'{round(t, 2)} лет\n')

def main():
    D, Y, Z = read_input_file()
    t = calculate_years(D, Y, Z)
    print('\nЗадача3.2: ')
    print(f'{round(t, 2)} лет')
    write_output_file(t)

if __name__ == '__main__':
    main()



#3.3
def read_input_file(filename):
    with open(filename, "r") as f:
        W = int(f.readlines()[25])
    return W

def calculate_sum_digits(W):
    sum_digits = sum(int(digit) for digit in str(W))
    return sum_digits

def print_result(result, task_name):
    print(f"{task_name}:")
    print(result)

def write_result_to_file(result, task_name, filename):
    with open(filename, "a") as f:
        f.write(f"{task_name}:\n{result}\n")

W = read_input_file("input.txt")
sum_digits = calculate_sum_digits(W)
print_result(sum_digits, "\nЗадача3.3")
write_result_to_file(sum_digits, "\nЗадача3.3", "output.txt")




#   python task4.py