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


def getHemmingtonCode(infVector):
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
    for i in range(0, 7):
        if hammCode[i] == -1:
            if i == 0:
                hammCode[i] = (infVector[0] ^ infVector[1] ^ infVector[3])
            elif i == 1:
                hammCode[i] = (infVector[0] ^ infVector[2] ^ infVector[3])
            elif i == 3:
                hammCode[i] = (infVector[1] ^ infVector[2] ^ infVector[3])
    return hammCode


def main():
    checkBits = [1,2,4]
    infVector = inputInformVector()
    hammingVector = getHemmingtonCode(infVector)
    print(hammingVector)




if __name__ == "__main__":
    main()
