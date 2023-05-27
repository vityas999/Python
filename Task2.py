# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите трехзначное число: "))
while num < 100 or num > 999:
    num = int(input("Ошибка вввода!Введите трехзначное число: "))
thirdNumber = num % 10
secondNumber = (num % 100) // 10
firstNumber = num // 100
sumNumbers = firstNumber + secondNumber + thirdNumber
print(sumNumbers, '(',firstNumber, '+', secondNumber, '+', thirdNumber,')')