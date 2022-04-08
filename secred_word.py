import string
letter = input()

c_counter = 0
o_counter = 0
n_counter = 0
used_letters = ""
need_letters = ""
while letter != "end":
    if letter in string.ascii_letters:
        if letter == "c":
            c_counter += 1
            if c_counter <= 1:
                used_letters += letter
            elif c_counter > 1:
                need_letters += letter
                used_letters += letter

        elif letter == "o":
            o_counter += 1
            if o_counter <= 1:
                used_letters += letter
            elif o_counter > 1:
                need_letters += letter
                used_letters += letter

        elif letter == "n":
            n_counter += 1
            if n_counter <= 1:
                used_letters += letter
            elif n_counter > 1:
                need_letters += letter
                used_letters += letter
        else:
            need_letters += letter
            used_letters += letter

    letter = input()


print(f"{need_letters} ", end=" ")

