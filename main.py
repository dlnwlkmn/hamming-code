from array import *
from tabulate import tabulate


# функция ввода инфомрационного вектора
def inputInformVector():
    toReturn = array('i', [])   # объявление массива литералом
    inputStr =  input("\nВведите информационный вектор размером \033[7m4 бита\033[0m: ")    # ввод вектора

    if (len(inputStr) > 4):     # проверка на четырёхразрядность
        print("\033[33mИнформационный вектор не должен быть больше 4 бит\033[0m")
        return inputInformVector()

    for i in inputStr:          # проверка на бинарный введеный вектор
        if (i == "1" or i == "0"):
            toReturn.append(int(i))
        else:
            print("\033[33mВведите корректный информационный вектор\033[0m")
            return inputInformVector()
    return toReturn


# функция рассчета кода Хемминга
def getHemmingCode(infVector):
    hammCode = array('i', [])   # объявление массива литералом
    infVectorCounter = 1
    checkBitsCounter = 0
    for i in range(0, 7):
        if i + 1 == 2**checkBitsCounter:    # провека разряда контрольной суммы
            hammCode.insert(i, -1)          # помечаем такие разряды -1
            checkBitsCounter += 1           # увеличиваем степень двойки на единицу
        else:
            hammCode.insert(i, infVector[len(infVector)-infVectorCounter])  # инсерт значения инф. вектора
            infVectorCounter += 1

        if hammCode[i] == -1:               # рассчет разрядов контрольной суммы
            if i == 0:
                hammCode[i] = (infVector[0] ^ infVector[2] ^ infVector[3])
            elif i == 1:
                hammCode[i] = (infVector[0] ^ infVector[1] ^ infVector[3])
            elif i == 3:
                hammCode[i] = (infVector[0] ^ infVector[1] ^ infVector[2])
    return hammCode


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


# функция получения вектора ошибки в двоичном виде
def getBinaryError(num):
    if (num == 0): return "0"
    elif (num == 1): return "1"
    else: return getBinaryError(int(num/2)) + str(num%2)


# фукнция, декодирующая поврежденный код Хемминга
def decodeDamagedVector(vector):
    syndrome = []
    syndrome.append(vector[0] ^ vector[2] ^ vector[4] ^ vector[6])
    syndrome.append(vector[1] ^ vector[2] ^ vector[5] ^ vector[6])
    syndrome.append(vector[3] ^ vector[4] ^ vector[5] ^ vector[6])
    return syndrome


# функция по подсчёту единиц в векторе (str)
def getNumberOfOnes(errorVector):
    number = 0
    for i in range(0, 7):
        if errorVector[i] == "1":
            number +=1
    return number


# функция по проверке синдрома ошибки (на ноль)
def checkErrorSyndrome(syndrome):
    for i in range(0, 3):
        if syndrome[i] == 1:
            return False
    return True

# главная функция
def main():
    # Кортеж с заголовками таблицы 1
    dataTableColumns = ("Крастность", "Всего ошибок, шт.", "Выявлено ошибок, шт.", "Обнаруживающая способность кода", "%")
    # Кортеж с заголовками таблицы 2
    errorTableColumns = ("Крастность", "Ошибки")

    foundErrors = [0,0,0,0,0,0,0]                 # список для подсчета ошибок (всех кратностей (7))
    fatalErrors = ["","","","","","",""]          # список ошибок, которые не были обнаружены
    dataTable = []                                # список кортежей с иформацией для вывода в таблице
    errorTable = []                               # список кортежей с ненайденными ошибками по кратностям

    infVector = inputInformVector()               # вызываем метод ввода информационного вектора
    hammingVector = getHemmingCode(infVector)     # вызоваем метод рассчета кода Хемминга
    hammingVector.reverse()


    for i in range(1, 128):                 # цикл по всем ошибкам

        damagedVector = []                  # список для хранения поврежденного вектора
        binaryError = getBinaryError(i)     # вызываем метод, возвращающий ошибку в бинарном виде

        for j in range(0, 7 - len(binaryError)):    # в цикле дописываются нули до 7ми разрядов
            binaryError = "0" + binaryError

        for j in range(0, 7):                       # в цикле получаем поврежденные код
            damagedVector.append(hammingVector[j] ^ int(binaryError[j]))

        errorSyndrome = decodeDamagedVector(damagedVector)  # декодируем поврежденный вектор (получаем синдром ошибки)

        if checkErrorSyndrome(errorSyndrome) == False:      # проверка на нулевой синдром
            foundErrors[getNumberOfOnes(binaryError) - 1] += 1              # учитываем обнаруженную ошибку по кратности
        else:
            fatalErrors[getNumberOfOnes(binaryError) - 1] += str(binaryError)+"\n"   # записываем код необнаруженной ошибки

    for i in range(0, 7):   # заполнение (с рассчетом) данных для таблицы

        comb = getCombinations(7, i + 1)    # рассчет общего количества ошибок (i+1)-й кратности
        k = foundErrors[i]/comb
        dataTable.append((i + 1, comb, foundErrors[i], k, round(k*100, 2)))

    # печать таблицы в консоль
    print("\033[36mТаблица:\033[0m\n" + "---"*36)
    print(tabulate(dataTable, headers=dataTableColumns, tablefmt="pipe", stralign='center'))
    print("---"*36)

    for i in range(0, 7):   # заполнение кратностей и не найденных ошибок
        errorTable.append((i + 1, fatalErrors[i]))

    # печать списка невыявленных ошибок в консоль
    print("\n\033[31mНевыявленные векторы ошибок по кратностям:\033[0m\n" + "---"*9)
    print(tabulate(errorTable, headers=errorTableColumns, tablefmt="pipe", stralign='center'))
    print("---" * 9)


if __name__ == "__main__":  # точка входа в программу
    main()