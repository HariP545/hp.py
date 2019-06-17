p=input()
if((p>='a' and p<='z') or (p>='A' and p<='Z')):
    if(p=='a' or p=='A' or p=='e'or p=='E'or p=='i'or p=='I'or p=='o'or p=='O'or p=='u'or p=='U'):
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")
