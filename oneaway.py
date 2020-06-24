class oneaway:
    def __init__(self):
        self.str1_letter_count = dict()
        self.str2_letter_count = dict()

    def oneedit(self, str1, str2):
        if abs(len(str1) - len(str2)) <= 1:
            for i in str1:
                if not i in self.str1_letter_count:
                    self.str1_letter_count[i] = 1
                else:
                    self.str1_letter_count[i] += 1
            for j in str2:
                if not j in self.str2_letter_count:
                    self.str2_letter_count[j] = 1
                else:
                    self.str2_letter_count[j] += 1
            for element in self.str1_letter_count:


        return True


o = oneaway()
print(o.oneedit("pale", "ple"))
