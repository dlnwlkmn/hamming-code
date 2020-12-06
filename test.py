# функция рассчета факториала
def factorial(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    if num == 1:
        return num
    return num * factorial(num - 1)


# функция получения кол-ва комбинаций
def getCombinations(n, i):
    return factorial(n)/(factorial(i)*factorial(n-i))

for i in range(0,15):
    print(getCombinations(15, i+1))