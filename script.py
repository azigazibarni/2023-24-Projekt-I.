sysInput = int(input('Add meg az átváltandó szám számrendszerét (2, 8, 10, 16): '))
numInput = str(input('Add meg az átváltandó számot: '))
destInput = int(input('Add meg a cél számrendszert (2, 8, 10, 16): '))

# sys: 2, 8, 10, 16

def decimal(num, sys):
    if sys == 2:
        out = 0
        num = list(num[::-1])
        for i in range(len(num)):
            if int(num[i]) == 1:
                out += 2**i

    elif sys == 8:
        print(':3')

    elif sys == 10:
        print(':3')

    elif sys == 16:
        print(':3')
    else:
        return
    
    return out

print(decimal(numInput, sys=2))