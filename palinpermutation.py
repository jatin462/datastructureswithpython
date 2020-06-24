class palinpermu:
    def __init__(self):
        self.wlist = {}

    def count_letter(self, str1):
        for i in str1.replace(" ", ""):
            if not i in self.wlist:
                self.wlist[i] = 1
            else:
                self.wlist[i] += 1
        return self.wlist

    def check_palipermu(self, str1):
        word_count_list = self.count_letter(str1.lower())
        odd_count = 0
        for item in word_count_list:
            if word_count_list[item] % 2 == 1 and odd_count == 0:
                odd_count += 1
            elif word_count_list[item] % 2 == 1 and odd_count != 0:
                return False
        return True


p = palinpermu()
print(p.check_palipermu("termasmind"))