code = """VZ FRVSYFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZFGNXRF V NZ BHG BS PBAGEBY
NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF
URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"""

decrypted = ""

def shift_letter(cypher, shift=13):
    global decrypted
    
    decrypted = "" 
    
    
    for e in cypher:
        if e.isupper():
            decrypted += chr((ord(e) - ord('A') - shift) % 26 + ord('A'))
        elif e.islower():
            decrypted += chr((ord(e) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += e
            
            
            
    return decrypted






print(shift_letter(code))
