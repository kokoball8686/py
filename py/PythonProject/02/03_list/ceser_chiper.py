plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



cipertext = []
for i,ch in enumerate(plaintext):
    #print(i, ch, plaintext[(i+3)%len(plaintext)])
    cipertext.append(plaintext[(i+3)%len(plaintext)])

print(cipertext)


print(''.join(cipertext))

###################another


cipertext = ''
for i,ch in enumerate(plaintext):
    cipertext += plaintext[(i+3)%len(plaintext)]

print(cipertext)

