sysInput = int(input('Add meg az átváltandó szám számrendszerét (2, 8, 10, 16): '))
numInput = str(input('Add meg az átváltandó számot: '))
destInput = int(input('Add meg a cél számrendszert (2, 8, 10, 16): '))

# sys: 2, 8, 10, 16

def decimal(num, sys):
    if sys == 2:
        out = 0
        num = [num[::-1]]
        for i in len(num):
            if num[i] == 1:
                out += 2**i
        return out

    elif sys == 8:
        print(':3')

    elif sys == 10:
        print(':3')

    elif sys == 16:
        print(':3')
    else:
        return

print(decimal(numInput, 2))
