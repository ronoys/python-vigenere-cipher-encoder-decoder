def vigenere(text,key,z):
    
    letters = list('abcdefghijklmnopqrstuvwxyz')
    newletters = letters
    
    keylist = list(key)
    copykeylist = keylist
    textlist = list(text)
    copytextlist = textlist
    length = len(keylist)
    emptyList = []

    # Creates keystream - stores in emptyList ----------------------|
    for x in range(0,len(textlist)): 
        emptyList.append(keylist[x % length])

    keyStream = emptyList
    emptyList = []

    if z == 'e':
        for x in range(0,len(keyStream)):
            textLetter = textlist[x]
            keyLetter = keyStream[x]
            letterIndex = letters.index(textLetter)
            letterIndex2 = letters.index(keyLetter)
            new_letter = letters[(letterIndex+letterIndex2) % len(letters)]
            emptyList.append(new_letter)
    elif z == 'd':
        for x in range(0,len(keyStream)):
            textLetter = textlist[x]
            keyLetter = keyStream[x]
            letterIndex = letters.index(textLetter)
            letterIndex2 = letters.index(keyLetter)
            new_letter = letters[(letterIndex-letterIndex2) % len(letters)]
            emptyList.append(new_letter)
            
    str1 = ''.join(emptyList)
    print (str1)
     
def main():
        
    text_input = str(input("Enter the string: "))
    key_input = str(input("Enter the key: "))
    true_false = str(input("Enter e(encrypt) or d(decrypt): "))
    vigenere(text_input,key_input,true_false)
    
    
    
main() # calls procedure
