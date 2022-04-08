c, o, n = 0, 0, 0
string = ''
while True:

    letter = input()

    if c == 1 and o == 1 and n == 1:
        print(f'{string} ', end='')
        c, o, n = 0, 0, 0
        string = ''

    if letter == 'End':
        break

    if letter.isalpha():

        if letter in 'con':
            if letter == 'c':
                if c == 0:
                    c = 1
                else:
                    string += letter
            elif letter == 'o':
                if o == 0:
                    o = 1
                else:
                    string += letter
            elif letter == 'n':
                if n == 0:
                    n = 1
                else:
                    string += letter
        else:
            string += letter
