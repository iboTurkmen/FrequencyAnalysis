
def DecryEngChar():
    result = ""
    EngChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']


def DecryTurkChar():
    result = ""
    TurkChar = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J',
                'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U', 'Ü',
                'V', 'Y', 'Z']



def decryption():
    print("you choose Decryption")
    langChose = int(input("Chose a Language Please. 0:English 1:Turkish "))
    if langChose == 0:
        DecryEngChar()
    elif langChose == 1:
        DecryTurkChar()
    else:
        print("You Must Chose Language First?")
        decryption()


def res(cipherValue):
    while not cipherValue.isnumeric():
        print("Please Enter Numbers Only.")
        main()
    if int(cipherValue) == 0:
        exit()
    elif int(cipherValue) == 1:
        decryption()
    elif cipherValue != range(0, 1):
        print("you must choose Encryption or Decryption or Exit first")
        main()


def main():
    cipherType = input("please choose Exit:0 or Decryption:1 ? select : ")
    res(cipherType)


main()