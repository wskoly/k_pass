from random import randrange as rg
allowed_upper = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U',
                 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
allowed_lower = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k',
                 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u',
                 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}
allowed_special = {0: '@', 1: '%', 2: '+', 3: '*', 4: '/', 5: '!', 6: '#', 7: '$', 8: '^', 9: '?', 10: ':',
                   11: ';', 12: '(', 13: ')', 14: '{', 15: '}', 16: '[', 17: ']', 18: '~', 19: '-',
                   20: '_', 21: '.', 22: '`', 23: '='}
allowed_number = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

n = rg(16,33)
def GenPass(length = n, upper=False, lower= False, special= False, number =False):
    """
    The function to generate a random password or otp
    :param length: Length of the password(int)
    :param upper: Password consists of UpperCase letters(bool)
    :param lower: Password consists of LowerCase letters(bool)
    :param special: Password consists of Special characters(bool)
    :param number: Password consists of Numbers(bool)
    :return: Returns the generated password as a string(str)
    """
    if not isinstance(length,int):
        raise ValueError("length should be an Integer")

    list_char_cat = []
    if(upper):
        list_char_cat.append(allowed_upper)
    if(lower):
        list_char_cat.append(allowed_lower)
    if(special):
        list_char_cat.append(allowed_special)
    if(number):
        list_char_cat.append(allowed_number)

    if not list_char_cat:
        list_char_cat = [allowed_upper,allowed_lower,allowed_special,allowed_number]

    password = ''
    for i in range(length):
        rand_dict = list_char_cat[rg(0,len(list_char_cat))]
        password += rand_dict[rg(0,len(rand_dict))]
    return password

if __name__ == "__main__":
    pass