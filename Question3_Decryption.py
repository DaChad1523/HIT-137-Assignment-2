encrypted_code = """
tybony_inenoyr = 100
zl_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inenoyr
    ybpny_inenoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inenoyr > 0:
        vs ybpny_inenoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inenoyr)
        ybpny_inenoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inenoyr = 10
    zl_qvpg['xr14'] = ybpny_inenoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inenoyr
    tybony_inenoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inenoyr)
cevag(zl_qvpg)
cevag(zl_frg)

"""

def decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


key = 13
decrypted_code = decrypt(encrypted_code, key)
print("Decrypted:", decrypted_code)