def matching_length(str1, str2):
    result = False
    if len(str1) == len(str2):
        result = True
    return result


class permutation:
    def __init__(self):
        self.param = {}

    def check_permutation(self, str1, str2):
        if not matching_length(str1, str2):
            return False
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        for i in range(0, len(str1)):
            if sorted_str1[i] != sorted_str2[i]:
                return False
        return True

p = permutation()
print(p.check_permutation("hii", "hie  "))

