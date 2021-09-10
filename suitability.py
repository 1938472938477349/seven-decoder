#!/usr/bin/env python

"""
Author: Wei-Hung Hsu
First Task: Discuss a possible algorithm

7 segments a, b, c, d, e, f, g

We represent each segment as a single bit. 7 segments can therefore be represented as a 7 bit string 0000000.
Each segment within the string from MSB to LSB is represented in the following order:

  a
  _
f|_|b
e|_|c
  d

We create a dictionary which maps bit-strings to its respective numeral representative.
We then translate every 7 segment into its numerical representation
"""


def read_number(path):
    seg_code = {0b0110000: 1, 0b1101101: 2, 0b1111001: 3, 0b0110011: 4, 0b1011011: 5, 0b1011111: 6, 0b1110000: 7,
                0b1111111: 8, 0b1111011: 9, 0b1111110: 0}
    seg_lit = [0b0000000 for i in range(9)]
    line_n = 0

    my_digits = []

    with open(path) as file:
        while (line := file.readline()):
            line_class = line_n % 4  # which line am i currently in

            # if len(line) == 28 and line_class != 3:
            #    continue

            if line_class == 0:
                if len(line) == 1:  # handles the double newline
                    continue

                for i in range(len(line) // 3):
                    if line[i * 3 + 1] == '_':
                        seg_lit[i] = seg_lit[i] | 0b1000000
            elif len(line) == 28 and line_class == 1:
                for i in range(len(line) // 3):
                    if line[i * 3] == '|':
                        seg_lit[i] = seg_lit[i] | 0b0000010
                    if line[i * 3 + 1] == '_':
                        seg_lit[i] = seg_lit[i] | 0b0000001
                    if line[i * 3 + 2] == '|':
                        seg_lit[i] = seg_lit[i] | 0b0100000
            elif len(line) == 28 and line_class == 2:
                for i in range(len(line) // 3):
                    if line[i * 3] == '|':
                        seg_lit[i] = seg_lit[i] | 0b0000100
                    if line[i * 3 + 1] == '_':
                        seg_lit[i] = seg_lit[i] | 0b0001000
                    if line[i * 3 + 2] == '|':
                        seg_lit[i] = seg_lit[i] | 0b0010000

                serial = ""
                for seg in seg_lit:
                    if seg in seg_code:
                        converted_num = seg_code[seg]
                        serial += str(converted_num)
                    else:
                        serial += "X"

                # print(serial)
                my_digits.append(serial)
                seg_lit = [0b0000000 for i in range(9)]

            line_n += 1
    return my_digits


print(read_number('bankocr.txt'))
# output: ['000000000', '111111111', '2222XXXXX', '333333333', '444444444', '555555555', '666666666', 'X77777777', '888888888', '999999999', '123456789']

def valid_num(num_str):
    return num_str.isdecimal() and sum([i * int(num_str[::-1][i - 1]) for i in range(1, 10)]) % 11 == 0


print(valid_num("123456789"))
print(valid_num("X14342545"))
