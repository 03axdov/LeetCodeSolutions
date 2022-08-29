def uniqueMorseRepresentations(words):
    letters = {'a': ".-", 'b': "-...",'c': "-.-.",'d':"-..",
               'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",
               'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",
               'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",
               't':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
    output = []
    current = ''

    for word in words:
        for char in word:
            current += letters[char]
        if current not in output:
            output.append(current)
        current = ''
    
    return len(output)


print(uniqueMorseRepresentations(["a"]))