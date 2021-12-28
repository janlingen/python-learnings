def caesar_cipher(string, offset):
    result = ""
    for i in string:
        place = ord(i) - 97 - offset
        if place < 0:
            place = 123 + place
            result += chr(place)
        else:
            result += chr(97+place)
    return result
