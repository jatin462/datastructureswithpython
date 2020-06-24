t_dict = {}
i = 0
with open("C:/Users/jatin/Downloads/py-master/DataStructures/4_HashTable_2_Collisions/Solution/nyc_weather.csv", "r") as f:
    for line in f:
        if i != 0:
            tokens = line.split(',')
            day = tokens[0].strip()
            temp = tokens[1].strip()
            t_dict[day] = temp
        i += 1
sum = 0
print(t_dict)
for date in range(1,8):
    sum += int(t_dict["Jan "+ str(date)])

print(sum/7)
print(max(t_dict, key=t_dict.get))
