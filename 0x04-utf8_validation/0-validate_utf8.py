#!/usr/bin/python3
""" 0x04-utf8_validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """

    nbytes = 0
    for bytes in data:
        if nbytes == 0:
            if bytes >> 7 == 0b0:
                continue
            elif bytes >> 4 == 0b1110:
                nbytes = 2
            elif bytes >> 3 == 0b11110:
                nbytes = 3
            else:
                return False
        else:
            if bytes >> 6 != 0b10:
                return False
            nbytes -= 1
    return nbytes == 0
