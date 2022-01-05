def generate_string(string, frequency):
    for i in string:
        for x in range(frequency):
            yield i


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency
    
    def __iter__(self):
        self.cnt = 0
        self.curr_spot = 0
        return self
    
    def __next__(self):
        self.cnt += 1
        if self.cnt > len(self.string)*self.frequency:
            raise StopIteration
        result = self.string[self.curr_spot]
        self.curr_spot = self.cnt  // self.frequency
        return result
