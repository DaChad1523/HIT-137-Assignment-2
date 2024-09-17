def separate_string(s):
    numbers = ''.join(filter(str.isdigit, s))
    letters = ''.join(filter(str.isupper, s))
    return numbers, letters

def convert_to_ascii(s):
    return [ord(c) for c in s]

def decipher_cryptogram(cryptogram, shift):
    decrypted = ''
    for char in cryptogram:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted += char
    return decrypted

# Example string
s = "56aAwkM1984sktr235ZyAaym1d5s785fsd100"

# Separate string
number_string, letter_string = separate_string(s)
print(f"Number string: {number_string}")
print(f"Letter string: {letter_string}")

# Convert even numbers to ASCII
even_numbers = [int(n) for n in number_string if int(n) % 2 == 0]
even_numbers_ascii = convert_to_ascii(''.join(map(str, even_numbers)))
print(f"Even numbers ASCII: {even_numbers_ascii}")

# Convert uppercase letters to ASCII
uppercase_ascii = convert_to_ascii(letter_string)
print(f"Uppercase letters ASCII: {uppercase_ascii}")

# Decipher the cryptogram
cryptogram = """VZ FRVSYFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

for shift in range(1, 26):
    decrypted = decipher_cryptogram(cryptogram, shift)
    if "MARILYN MONROE" in decrypted:
        print(f"Shift key: {shift}")
        print(f"Decrypted message: {decrypted}")
        break