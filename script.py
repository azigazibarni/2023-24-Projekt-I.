#sysInput = int(input('Add meg az átváltandó szám számrendszerét (2, 8, 10, 16): '))
#numInput = str(input('Add meg az átváltandó számot: '))
# destInput = int(input('Add meg a cél számrendszert (2, 8, 10, 16): '))

# sys: 2, 8, 10, 16

#number to decimal
def decimal(num, sys):
    out = 0
    if sys == 2:
        num = str(num)
        num = list(num[::-1])
        for i in range(len(num)):
            if int(num[i]) == 1:
                out += 2**i

    elif sys == 8:
        num = list(num[::-1])
        for i in range(len(num)):
            out += int(num[i]) * (8 ** i)

    elif sys == 10:
        out = num

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
    return out


#number to binary
def binary(num, sys):
    out = 0
    if sys == 2:
        out = num

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

    elif sys == 10:
        out = ''
        while num > 0:
            remind = num % 2
            out = str(remind) + out
            num = num // 2
    
    elif sys == 16:
        print('16 => 2')

    else:
        return
    return int(out)


print(binary(5007, 8))