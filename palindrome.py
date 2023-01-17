def isPalindrome(str):
    start_index = 0
    value = True
    for i in range(  int (len(str) /  2 ):
        if str[i] == str[len(str) - i]:
            value = True
        else:
            value = False 
    return value

