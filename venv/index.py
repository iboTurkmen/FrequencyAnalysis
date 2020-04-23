
def DecryEngChar():
    result = ""
    freq_letters = [' ', 'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r',
                    'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y',
                    'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    freq_analysis = {}
    ciphertxt = input("Please Enter The Text To Decrypt: ").upper()
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

    for each in freq_letters:
        maxfreq = max(freq_analysis, key=freq_analysis.get)
        if each == " ":
            result = ciphertxt.replace(maxfreq, each)
            del freq_analysis[maxfreq]
        if each == "e":
            result = result.replace(maxfreq, each)
            del freq_analysis[maxfreq]
        if each == "t":
            result = result.replace(maxfreq, each)
            del freq_analysis[maxfreq]
        if each == "i":
            result = result.replace("I", "h")
        if each == "g":
            result = result.replace("G", "o")
        if each == "f":
            result = result.replace("F", "n")
        if each == "s":
            result = result.replace("L", "s")
        if each == "d":
            result = result.replace("D", "l")
        if each == "v":
            result = result.replace("V", "v")
        if each == "k":
            result = result.replace("K", "r")
        if each == "q":
            result = result.replace("Q", "u")
        if each == "r":
            result = result.replace("R", "g")
        if each == "n":
            result = result.replace("N", "c")
        if each == "e":
            result = result.replace("E", "m")
        if each == "m":
            result = result.replace("M", "a")
        if each == "w":
            result = result.replace("W", "w")
        if each == "x":
            result = result.replace("X", "x")
        if each == "y":
            result = result.replace("Y", "y")
        if each == "z":
            result = result.replace("Z", "z")
        if each == "c":
            result = result.replace("C", "f")
        if each == "b":
            result = result.replace("B", "k")
        if each == "u":
            result = result.replace("U", "d")
        if each == "j":
            result = result.replace("J", "q")
        if each == "h":
            result = result.replace("H", "p")
        if each == "p":
            result = result.replace("P", "i")
    print("Frequencies Of Letters in English Language:- " + str(freq_letters))
    print("Frequencies Of Ciphertext:- " + str(freq_Numbers))
    print("Frequencies Analysis Of Ciphertext:- " + str(freq_analysis))
    print(result)
    main()

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