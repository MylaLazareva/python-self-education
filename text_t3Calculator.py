print("1) Створити простий калькулятор, який зчитує три рядки введених користувачем даних: перше число, друге число та операцію.\nПісля цього калькулятор застосовує операцію до введених чисел  (" + "\"перше числo\" \"операція\" \"друге число\"" + ") і виводить результат на екран.\nПідтримувані операції: +, -, /, *, mod, pow, div, де:\nmod - це отримання залишку від ділення,\npow - піднесення до степеня,\ndiv - цілочисельне ділення. ")

# Запит користувача на введення першого числа
num1 = float(input("Введіть перше число: "))

# Запит користувача на введення другого числа
num2 = float(input("Введіть друге число: "))

# Запит користувача на введення операції
operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")

# Обчислення результату в залежності від введеної операції
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '/':
    result = num1 / num2
elif operation == '*':
    result = num1 * num2
elif operation == 'mod':
    result = num1 % num2
elif operation == 'pow':
    result = num1 ** num2
elif operation == 'div':
    result = num1 // num2
else:
    print("Неправильна операція")

# Виведення результату на екран
print("Результат: ", result)


print("\n2) Маємо 2 числа a і b. Визначте, чи ділиться a на b націло. Чи ділиться b на a?")

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

if a % b == 0:
    print(a, "ділиться на", b, "націло.")
else:
    print(a, "не ділиться на", b, "націло.")

if b % a == 0:
    print(b, "ділиться на", a, "націло.")
else:
    print(b, "не ділиться на", a, "націло.")


print("\n3) Дано трицифрове число. Визначте, чи є серед його цифр однакові.")

number = int(input("Введіть трицифрове число: "))
first_digit = number // 100  # отримуємо першу цифру числа
second_digit = (number // 10) % 10  # отримуємо другу цифру числа
third_digit = number % 10  # отримуємо третю цифру числа

if first_digit == second_digit or first_digit == third_digit or second_digit == third_digit:
    print("У числі є однакові цифри.")
else:
    print("У числі немає однакових цифр.")



#python text_t3Calculator.py