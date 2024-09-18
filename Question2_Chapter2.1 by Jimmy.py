string = " asA6Ed4asG5das5dDas"

decimal = []
number = []

for e in string:
    if e.isdigit() and int(e) % 2 ==0:
        decimal.append(ord(e))
    elif e.isupper():
        number.append(ord(e))
        

print(f"Decimals: {decimal}")
print(f"Numbers: {number}")