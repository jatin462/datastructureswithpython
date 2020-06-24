class unique:
    def __init__(self):
        self.letter_count = {}

    def check_unique(self, word):
        for char in word:
            if not char in self.letter_count:
                self.letter_count[char] = True
            else:
                return "String is not Unique"
        return "String is unique"


u = unique()
print(u.check_unique("qwertyuiopq"))
