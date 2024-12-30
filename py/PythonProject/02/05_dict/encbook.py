encbook = {'A': 'F', 'B': 'G', 'C': 'H', 'D': 'I', 'E': 'J', 'F': 'K', 'G': 'L',
           'H': 'M', 'I': 'N', 'J': 'O', 'K': 'P', 'L': 'Q', 'M': 'R', 'N': 'S',
           'O': 'T', 'P': 'U', 'Q': 'V', 'R': 'W', 'S': 'X', 'T': 'Y', 'U': 'Z',
           'V': 'A', 'W': 'B', 'X': 'C', 'Y': 'D', 'Z': 'E'}



plaintext = 'HELLO WORLD Happy New Year'



ciphertext = ''
for ch in plaintext:
    # print(ch, encbook[ch])
    if ch in encbook:
        ciphertext += encbook[ch]
    else:
        ciphertext += ch

print("plaintext  :", plaintext)


print("ciphertext :", ciphertext)


input()

decbook = {}

for k,v in encbook.items():
    #print(k, v)
    decbook[v] = k


print("encbook :", encbook)
print("decbook :", decbook)


decrypted = ''
for ch in ciphertext:
    # print(ch, decbook[ch])
    if ch in decbook:
        decrypted += decbook[ch]
    else:
        decrypted += ch
print("decrypted :", decrypted)