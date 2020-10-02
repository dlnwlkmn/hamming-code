
def inputInformVector():

    toReturn = []
    inputStr =  input("Введите информационный вектор: ")
    for i in inputStr:
        if (i == "1" or i == "0"):
            toReturn.append(int(i))
        else:
            print("\033[33mВведите корректный информационный вектор\033[0m")
            return inputInformVector()
    return toReturn

def getHemmingtonCode(infVector):
    infVector
    #todo реализацию получения кода Хемминга

def main():
    infVector = inputInformVector()
    print(type(infVector))

if __name__ == "__main__":
    main()
