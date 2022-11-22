word = input ()
num = int(input())
newWord = ''
for i in word:
    char = ord(i)
    print(char)
    if (char >= 65 and char <= 90):
        char = char + num
        if char > 90:
            char = char - 26
        newWord = newWord + chr(char)
    elif char >= 97 and char <= 122:
        char - char + num
        if char > 122:
            char = char - 26
        newWord = newWord + chr(char)
    else:
        newWord = newWord + i
print(newWord)
    
        
