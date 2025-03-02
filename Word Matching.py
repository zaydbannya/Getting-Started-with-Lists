def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(words)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("list of words with first and last character are same\n",lst)
    return ctr
count=match_words(['abc','cfc','xyz','aba','1221'])
print("number of words having first and last same character:",count)