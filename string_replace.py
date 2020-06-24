class urlfy:
    def replace_function(self, str1):
        print(str1[:13].replace(" ", "%20%"))


u = urlfy()
u.replace_function("Mr John Smith              ")