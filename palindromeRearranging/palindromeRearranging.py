def palindromeRearranging(inputString):
    char = {}
    for a in inputString:
        if a not in char:
            char[a] = 1
        else:
            char[a] += 1
    odd_char = [i for i in char if char[i]%2==1]
    if len(odd_char)>1:
        return False
    else:
        return True
