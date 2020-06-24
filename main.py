from pip._vendor.distlib.compat import raw_input
import sys


def check_mapping(str1, str2):
    mapping = {}
    duplicate_mapping_flag = False
    #Checking if length of str1 and str2 is same
    if len(str1) == len(str2):
        #Storing the occurance of each character mapping dict
        for ch in str1:
            mapping[ch] = [pos for pos, char in enumerate(str1) if char == ch]
        for item in mapping:
            #Checking if any character has multiple occurances in str1
            if len(mapping[item]) > 1:
                for position in mapping[item]:
                    #Here checking whether multiple occured char in str1 assigned to the same char in str2
                    if str1[position] != str2[position]:
                        duplicate_mapping_flag = True
    if duplicate_mapping_flag == False:
        return True
    else:
        return False


if __name__ == '__main__':
    if len(sys.argv) == 3:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
        print(check_mapping(str1, str2))
    else:
        print("Program requires Only 2 input parameters to execute")
