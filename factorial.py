def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Пример использования
result = factorial(8)
print("Факториал числа равен:", result)