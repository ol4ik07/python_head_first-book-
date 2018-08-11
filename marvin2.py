paranoid_androin="Marvin, the Palaroid Android"
letters=list(paranoid_androin)
for char in letters[:6]:
    print('\t',char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
print()
for char in letters[12:20]:
    print('\t'*3, char)