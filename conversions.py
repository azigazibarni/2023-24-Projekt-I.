#convert to decimal
def decimal(num, sys):
    out = 0

    #from binary
    if sys == 2:
        num = str(num)
        num = list(num[::-1])
        for i in range(len(num)):
            if int(num[i]) == 1:
                out += 2**i

    #from octal
    elif sys == 8:
        num = list(num[::-1])
        for i in range(len(num)):
            out += int(num[i]) * (8 ** i)

    #from decimal
    elif sys == 10:
        out = num

    #from hexadecimal
    elif sys == 16:
        hex = 0
        num = list(num[::-1])
        for i in range(len(num)):
            if num[i].isdigit() == True:
                out += int(num[i]) * (16 ** i)
            elif num[i].isdigit() == False:
                if num[i].lower() == 'a':
                    hex = 10
                elif num [i].lower() == 'b':
                    hex = 11
                elif num [i].lower() == 'c':
                    hex = 12
                elif num [i].lower() == 'd':
                    hex = 13
                elif num [i].lower() == 'e':
                    hex = 14
                elif num [i].lower() == 'f':
                    hex = 15
                out +=  hex * (16 ** i)
    else:
        return
    return int(out)



#convert to binary
def binary(num, sys):
    out = 0

    #from binary
    if sys == 2:
        out = num

    #from octal
    elif sys == 8:
        out = ''
        num = str(num)
        for i in range(len(num)):
            oct = int(num[i])
            if oct == 0:
                out += '000'
            elif oct == 1:
                out += '001'
            elif oct == 2:
                out += '010'
            elif oct == 3:
                out += '011'
            elif oct == 4:
                out += '100'
            elif oct == 5:
                out += '101'
            elif oct == 6:
                out += '110'
            elif oct == 7:
                out += '111'
            else:
                return

    #from decimal
    elif sys == 10:
        out = ''
        num = int(num)
        while num > 0:
            remind = num % 2
            out = str(remind) + out
            num = num // 2
    
    #from hexadecimal
    elif sys == 16:
        out = ''
        num = str(num)
        for i in range(len(num)):
            hex = str(num[i])
            if hex.isdigit() == True:
                if hex == '0':
                    out += '0000'
                elif hex == '1':
                    out += '0001'
                elif hex == '2':
                    out += '0010'
                elif hex == '3':
                    out += '0011'
                elif hex == '4':
                    out += '0100'
                elif hex == '5':
                    out += '0101'
                elif hex == '6':
                    out += '0110'
                elif hex == '7':
                    out += '0111'
                elif hex == '8':
                    out += '1000'
                elif hex == '9':
                    out += '1001'
            elif hex.isdigit() == False:
                if hex.lower() == 'a':
                    out += '1010'
                elif hex.lower() == 'b':
                    out += '1011'
                elif hex.lower() == 'c':
                    out += '1100'
                elif hex.lower() == 'd':
                    out += '1101'
                elif hex.lower() == 'e':
                    out += '1110'
                elif hex.lower() == 'f':
                    out += '1111'
            else:
                return

    else:
        return
    return int(out)



#convert to octal
def octal(num, sys):
    out = 0

    #from binary
    if sys == 2:

        #add missing 0s to the front
        if 3 - (len(str(num)) % 3) != 3:
            remaind = 3 - (len(str(num)) % 3)
            num = list(num)
            for i in range(remaind):
                num.insert(0, '0')
            num = ''.join(num)

        oct = ''
        for i in range(0, len(num), 3):
            current = num[i] + num[i+1] + num[i+2]
            if current == '000':
                oct += '0'
            elif current == '001':
                oct += '1'
            elif current == '010':
                oct += '2'
            elif current == '011':
                oct += '3'
            elif current == '100':
                oct += '4'
            elif current == '101':
                oct += '5'
            elif current == '110':
                oct += '6'
            elif current == '111':
                oct += '7'
            else:
                return
        out = int(oct)

    #from octal
    elif sys == 8:
        out = num

    #from decimal
    elif sys == 10:
        out = ''
        for i in range(len(num) + 1):
            quot = int(num) // 8
            remaind = int(num) % 8
            num = quot
            out += str(remaind)
        out = out[::-1]
        out = int(out)

    #from hexadecimal
    elif sys == 16:
        num = binary(num, 16)
        out = octal(str(num), 2)

    else:
        return
    return out

#convert to hexadecimal
def hexadecimal(num, sys):
    out = 0

    #from binary
    if sys == 2:
        num = str(num)
        out = ''
        #add missing 0s to the front
        if 4 - (len(str(num)) % 4) != 4:
            remaind = 4 - (len(str(num)) % 4)
            num = list(num)
            for i in range(remaind):
                num.insert(0, '0')
            num = ''.join(num)

        for i in range(0, len(num), 4):
            current = num[i] + num[i+1] + num[i+2] + num[i+3]
            if current == '0000':
                out += '0'
            elif current == '0001':
                out += '1'
            elif current == '0010':
                out += '2'
            elif current == '0011':
                out += '3'
            elif current == '0100':
                out += '4'
            elif current == '0101':
                out += '5'
            elif current == '0110':
                out += '6'
            elif current == '0111':
                out += '7'
            elif current == '1000':
                out += '8'
            elif current == '1001':
                out += '9'
            elif current == '1010':
                out += 'A'
            elif current == '1011':
                out += 'B'
            elif current == '1100':
                out += 'C'
            elif current == '1101':
                out += 'D'
            elif current == '1110':
                out += 'E'
            elif current == '1111':
                out += 'F'
            else:
                return

        #remove 0s from the front of output
        out = list(out)
        while out[0] == '0':
            out.pop(0)
        out = ''.join(out)
                
    #from octal
    elif sys == 8:
        out = binary(num, 8)
        out = hexadecimal(out, 2)

    #from decimal
    elif sys == 10:
        out = ''
        for i in range(len(num) + 1):
            quot = int(num) // 16
            remaind = int(num) % 16
            num = quot
            if remaind > 9:
                if remaind == 10:
                    remaind = 'A'
                elif remaind == 11:
                    remaind = 'B'
                elif remaind == 12:
                    remaind = 'C'
                elif remaind == 13:
                    remaind = 'D'
                elif remaind == 14:
                    remaind = 'E'
                elif remaind == 15:
                    remaind = 'F'
            out += str(remaind)
        out = out[::-1]

        #remove 0s from the front of output
        out = list(out)
        while out[0] == '0':
            out.pop(0)
        out = ''.join(out)

    #form hexadecimal
    elif sys == 16:
        out = num

    else:
        return
    return out