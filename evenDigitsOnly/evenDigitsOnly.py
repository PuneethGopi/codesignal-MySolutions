def evenDigitsOnly(n):
     if all(([int(d)%2==0 for d in str(n)])) is True:
          return True
     else:
          return False
