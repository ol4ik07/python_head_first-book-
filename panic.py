phrase="Don't panic!"
plist=list(phrase)
print (phrase)
print (plist)
plist.pop(0)
plist.remove("'")

for letter in range (4):
        plist.pop()
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))

new_phrase=''.join(plist)
print (plist)
print (new_phrase)