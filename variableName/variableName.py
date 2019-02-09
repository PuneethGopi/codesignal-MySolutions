def variableName(name):
    if name[:1].isalpha() or name[:1]=="_":
        for c in name:
            if c != '_' and not c.isalpha() and not c.isdigit():
                return False
        return True
    return False
    
