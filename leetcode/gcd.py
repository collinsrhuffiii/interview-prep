def gcd(a,b):
    if a==0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(b,a%b)
    return gcd(b,a)

a = 54
b = 77
print(f'gcd({a},{b}) = {gcd(a,b)}')
