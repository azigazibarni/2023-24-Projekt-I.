sysInput = int(input('Add meg az átváltandó szám számrendszerét (2, 8, 10, 16): '))
numInput = str(input('Add meg az átváltandó számot: '))
destInput = int(input('Add meg a cél számrendszert (2, 8, 10, 16): '))

# sys: 2, 8, 10, 16

def decimal(num, sys):
    out = 0
    if sys == 2:
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

print(decimal(numInput, sysInput))