def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    own = sorted([yourLeft, yourRight])
    friend = sorted([friendsLeft, friendsRight])
    if (yourLeft+yourRight !=friendsLeft+friendsRight):
        return False
    elif(own[0] != friend[0]):
        return False
    else:
        return True
