# [28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3
def sum(num1, num2):
    if (num2 == 0):
        return (num1)
    else:
        return sum(num1 ^ num2, (num1 & num2) << 1)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print("Сумма: ", sum(num1,num2))   