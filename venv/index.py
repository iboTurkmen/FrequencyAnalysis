
def DecryEngChar():
    result = ""
    EngChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']
    freq_letters = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R',
                    'D', 'L', 'C', 'U', 'M', 'W', 'F', 'G', 'Y',
                    'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']
    freq_analysis = {}
    ciphertxt = input("Please Enter The Text To Decrypt: ").upper()
    ciphertxt = ciphertxt.replace(' ', '')
    ciphertxt = ciphertxt.replace("'", '')
    ciphertxt = ciphertxt.replace('.', '')
    ciphertxt = ciphertxt.replace(',', '')
    for i in ciphertxt:
        if i not in freq_analysis:
            freq_analysis[i] = 1
        else:
            freq_analysis[i] += 1
    freq_Numbers = sorted(freq_analysis.values())
    freq_Numbers.reverse()

    maxfreq = max(freq_analysis, key=freq_analysis.get)

    print(maxfreq)
    print("Frequencies Of Letters in English Language:- " + str(freq_letters))
    print("Frequencies Of Ciphertext:- " + str(freq_Numbers))
    print("Frequencies Analysis Of Ciphertext:- " + str(freq_analysis))

def DecryTurkChar():
    result = ""
    TurkChar = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H',
                'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P',
                'R', 'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']



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