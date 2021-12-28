def create_strings_from_characters(frequencies, string1, string2):
    def freq_check(freq, string):
        for i in string:
            if string.count(i) > freq.get(i, 0):
                return False
        return True
    if freq_check(frequencies, string1+string2):
        return 2 
    elif freq_check(frequencies,string1) or freq_check(frequencies,string2):
        return 1
    else:
        return 0