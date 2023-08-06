def decimalToBinary(decimal):
    global binary    
    binary = ''

    # Check if entered number is a digit
    if not str(decimal).isdigit():
        print('Number entered is not a decimal.')
        return False # Invalid decimal
    
    if decimal > 1:
        decimalToBinary(decimal // 2)
        
    binary += str(decimal % 2) # this is the general formula for working out binary of number
    return True # Valid decimal

def binaryToDecimal(binary):
    global decimal
    decimal = 0
    
    # Check if entered number is valid binary
    for i in binary:
        if i not in ('0', '1'):
            print('Number entered is not valid binary.')
            return False # Invalid binary

    # First reverse the binary number as a list
    reversedBinaryList = list(binary)
    reversedBinaryList.reverse()
    
    for i in range(len(binary)):
        bit = reversedBinaryList[i]
        if bit == '1':
            decimal += 2 ** i
    return True # Valid binary

def decimalToHexadecimal(decimal):
    global hexadecimal
    hexadecimal = ''
    
    # Check if entered number is a digit
    if not decimal.isdigit():
        print('Number entered is not a decimal.')
        return False # Invalid decimal

    decimalInt = int(decimal)

    if decimalInt >= 16:
        decimalToHexadecimal(str(decimalInt // 16))

    # Change decimal to its modulo of 16
    decimalInt = decimalInt % 16

    # Define a list of hexadecimal characters
    hexList = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split()
    
    hexadecimal += hexList[decimalInt]
    return True # Valid decimal

def hexadecimalToDecimal(hexadecimal):
    global decimal
    decimal = 0

    # Check if entered number is valid hexadecimal
    for i in hexadecimal.upper():
        if i not in '0123456789ABCDEF':
            print('Number entered is not valid hexadecimal.')
            return False # Invalid hexadecimal

    reversedHex = hexadecimal[::-1]
    hexList = '0 1 2 3 4 5 6 7 8 9 A B C D E F'.split()
    for i in range(len(reversedHex)):
        h = reversedHex[i]
        d = int(hexList.index(h))
        decimal += d * (16 ** i)
    return True # Valid hexadecimal


def binaryToHexadecimal(binary):
    global hex, decimal, hexadecimal
    hex = ''

    # Check if entered number is valid binary
    for i in binary:
        if i not in ('0', '1'):
            print('Number entered is not valid binary.')
            return False # Invalid binary

    while len(binary) % 4 != 0: # not a multiple of 4
        binary = '0' + binary # adding 0 to beginning of binary
                              # does not affect its value

    # Split binary into a list with each element having a length of 4
    binaryList = []
    for i in range(0, len(binary), 4):
        binaryList.append(binary[i:i + 4])

    for b in binaryList:
        binaryToDecimal(b)
        decimalToHexadecimal(str(decimal))
        hex += hexadecimal
    del decimal
    return True # Valid binary

def hexadecimalToBinary(hexadecimal):
    global binary, decimal, binary
    binary = ''

    # Check if entered number is valid hexadecimal
    for i in hexadecimal.upper():
        if i not in '0123456789ABCDEF':
            print('Number entered is not valid hexadecimal.')
            return False # Invalid hexadecimal

    hexadecimalToDecimal(hexadecimal)
    decimalToBinary(decimal)
    del decimal
    return True # valid hexadecimal

if __name__ == '__main__':
    while True:
        # Run decimalToBinary
        decimal = int(input('\nPlease enter a decimal to convert to binary: '))
        if decimalToBinary(decimal): print(binary)
        del binary
        
        # Run binaryToDecimal
        binary = input('\nPlease enter a binary number to convert to a decimal: ')
        if binaryToDecimal(binary): print(decimal)
        del decimal

        # Run decimalToHexadecimal
        decimal = input('\nPlease enter a decimal to convert to hexadecimal: ')
        if decimalToHexadecimal(decimal): print(hexadecimal)
        del hexadecimal

        # Run hexadecimalToDecimal
        hexadecimal = input('\nPlease enter a hexadecimal number to convert to a decimal: ').upper()
        if hexadecimalToDecimal(hexadecimal): print(decimal)
        del decimal

        # Run binaryToHexadecimal
        binary = input('\nPlease enter a binary number to convert to hexadecimal: ')
        if binaryToHexadecimal(binary): print(hex)
        del hexadecimal

        # Run hexadecimalToBinary
        hexadecimal = input('\nPlease enter a hexadecimal number to convert to binary: ').upper()
        if hexadecimalToBinary(hexadecimal): print(binary)
        del binary
