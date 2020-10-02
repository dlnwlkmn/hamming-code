from array import *


def inputInformVector():

    toReturn = array('i', [])
    inputStr =  input("Введите информационный вектор размером 4 бита: ")
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



def main():
    checkBits = [1,2,4]
    infVector = inputInformVector()
    hammingVector = getHemmingCode(infVector)
    for i in range(0, 7):
        print("Ci/n = " + str(getCombinations(7, i + 1)))

    for i in range(1, 128):
        damagedVector = []
        binaryError = getBinaryError(i)
        length = len(binaryError)
        for j in range(0, 7 - length):
            binaryError = "0" + binaryError
        print("До: " + str(hammingVector))
        print("Ошибка: " + binaryError)
        for j in range(0, 7):
            damagedVector.append(hammingVector[j] ^ int(binaryError[j]))
        print("После : " + str(damagedVector) + "\n")








if __name__ == "__main__":
    main()
