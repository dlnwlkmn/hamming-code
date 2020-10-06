from array import *
from tabulate import tabulate


def inputInformVector():

    toReturn = array('i', [])
    inputStr =  input("\nВведите информационный вектор размером \033[7m4 бита\033[0m: ")
    if (len(inputStr) > 4):
        print("\033[33mИнформационный вектор не должен быть больше 4 бит\033[0m")
        return inputInformVector()
    for i in inputStr:
        if (i == "1" or i == "0"):
            toReturn.append(int(i))
        else:
            print("\033[33mВведите корректный информационный вектор\033[0m")
            return inputInformVector()
    return toReturn


def getHemmingCode(infVector):
    hammCode = array('i', [])
    infVectorCounter = 0
    checkBitsCounter = 0
    for i in range(0, 7):
        if i + 1 == 2**checkBitsCounter:
            hammCode.insert(i, -1)
            checkBitsCounter += 1
        else:
            hammCode.insert(i, infVector[infVectorCounter])
            infVectorCounter += 1

        if hammCode[i] == -1:
            if i == 0:
                hammCode[i] = (infVector[0] ^ infVector[1] ^ infVector[3])
            elif i == 1:
                hammCode[i] = (infVector[0] ^ infVector[2] ^ infVector[3])
            elif i == 3:
                hammCode[i] = (infVector[1] ^ infVector[2] ^ infVector[3])
    return hammCode

def factorial(num):
    if num < 0:
        return 0
    if num == 0:
        return 1
    if num == 1:
        return num
    return num * factorial(num - 1)

def getCombinations(n, i):
    return factorial(n)/(factorial(i)*factorial(n-i))

def getBinaryError(num):
    if (num == 0): return "0"
    elif (num == 1): return "1"
    else: return getBinaryError(int(num/2)) + str(num%2)

def decodeDamagedVector(vector):
    syndrome = []
    syndrome.append(vector[0] ^ vector[2] ^ vector[4] ^ vector[6])
    syndrome.append(vector[1] ^ vector[2] ^ vector[5] ^ vector[6])
    syndrome.append(vector[3] ^ vector[4] ^ vector[5] ^ vector[6])
    return syndrome

def getNumberOfOnes(errorVector):
    number = 0
    for i in range(0, 7):
        if errorVector[i] == "1":
            number +=1
    return number

def checkErrorSyndrome(syndrome):
    for i in range(0, 3):
        if syndrome[i] == 1:
            return False
    return True


def main():
    foundErrors = [0,0,0,0,0,0,0]
    fatalErrors = []
    infVector = inputInformVector()
    hammingVector = getHemmingCode(infVector)

    for i in range(1, 128):
        damagedVector = []
        dataTable = []
        dataTableColumns = []
        dataTableColumns.append(("Крастность", "Всего ошибок, шт.", "Выявлено ошибок, шт.", "Обнаруживающая способность кода, %"))
        binaryError = getBinaryError(i)
        length = len(binaryError)
        for j in range(0, 7 - length):
            binaryError = "0" + binaryError
        for j in range(0, 7):
            damagedVector.append(hammingVector[j] ^ int(binaryError[j]))

        errorSyndrome = decodeDamagedVector(damagedVector)
        if checkErrorSyndrome(errorSyndrome) == False:
            foundErrors[getNumberOfOnes(binaryError) - 1] += 1
        else:
            fatalErrors.append(binaryError)

    for i in range(0, 7):
        comb = getCombinations(7, i + 1)
        dataTable.append((i + 1, comb, foundErrors[i], foundErrors[i]/comb))

    print("\033[36mТаблица:\033[0m\n" + "---"*34)
    print(tabulate(dataTable, headers=dataTableColumns[0], tablefmt="pipe", stralign='center'))
    print("---"*34)
    print("\n\033[31mНевыявленные векторы ошибок:\033[0m")
    for i in fatalErrors:
        print("\033[33m" + i + "\033[0m", end=",")


if __name__ == "__main__":
    main()
