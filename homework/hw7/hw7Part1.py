'''
this file is a modified file of hw6 of the auto grading, meaning that this file is also used to correct the wrong word in a file accoding to
a dictionary file and print out the wrong word and the proper word respectively

author:JUNWEI TAN

'''
# this function returns a list of tuple that contains the word adn the frequency of the word
def find_word (word1,dictionary,keyboard):
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'y', 'z' ]
    resultdict = []
    if word1 in dictionary:
        print("{:<15} -> {:<15} :FOUND".format(word1,word1))
        return resultdict
    
    #insert method
    for i in range(len(word1)):
        for j in range(len(letters)):
            test_word=word1[:i]+letters[j]+word1[i:] 
            if test_word in dictionary:
                resultdict.append((dictionary[test_word],test_word))
        
        
        # drop method: drop a letter from the original word
    for i in range(len(word1)-1):
        test_word=word1[:i]+word1[i+1:] 
        if test_word in dictionary:
            resultdict.append((dictionary[test_word],test_word))
    test_word1=word1[:len(word1)-1]
    if test_word1 in dictionary:
        resultdict.append((dictionary[test_word1],test_word1))
            
            
        # swap method:  change the order of two concatenate letter in the word
    for i in range(len(word1)-2):    
        test_word=word1[:i]+word1[i+1]+word1[i]+word1[i+2:]
        if test_word in dictionary:
            resultdict.append((dictionary[test_word],test_word))
    test_word=word1[:len(word1)-2]+word1[len(word1)-1]+word1[len(word1)-2]
    if test_word in dictionary:
        resultdict.append((dictionary[test_word],test_word))
        
    # replace method: replace one letter in the word by using another letter
    for i in range(len(word1)):                  
        for j in range(len(keyboard[word1[i]])):
            test_word=word1[:i]+keyboard[word1[i]][j]+word1[i+1:]
            if test_word in dictionary: 
                resultdict.append((dictionary[test_word],test_word))
        
    if len(resultdict)>0:
        return resultdict
    
    else:
        # no proper word matched in the dictionary
        print("{:<15} -> {:<15} :NO MATCH".format(word1,word1))
        return resultdict
    

dictionaryfile = input("Dictionary file => ")
print(dictionaryfile)
inputfile = input("Input file => ")
print(inputfile)
keyboardfile = input("Keyboard file => ")
print(keyboardfile)

#read the file and store the information in list and dictionary
dictionary = dict()
keyboard=dict()
words=[]
for line in open(dictionaryfile):
    line = line.strip().split(",")
    dictionary[line[0]]=line[1]
for line in open(keyboardfile):
    line=line.strip().split(" ")
    keyboard[line[0]]=line[1:]
for line in open(inputfile):
    line = line.strip()
    words.append(line)
    
    # for each word get the proper sorted list and print them out
for word in words:
    result = find_word (word,dictionary,keyboard)
    if len(result)>0:
        result=set(result)
        result=list(result)
        sorted_dict=sorted(result,reverse=True)
        if len(sorted_dict)== 1:
            print("{:<15} -> {:<15} :MATCH {}".format(word,sorted_dict[0][1],1))
        elif len(sorted_dict)==2:
            print("{:<15} -> {:<15} :MATCH {}".format(word,sorted_dict[0][1],1))
            print("{:<15} -> {:<15} :MATCH {}".format(word,sorted_dict[1][1],2))
        else:
            print("{:<15} -> {:<15} :MATCH {}".format(word,sorted_dict[0][1],1))
            print("{:<15} -> {:<15} :MATCH {}".format(word,sorted_dict[1][1],2))
            print("{:<15} -> {:<15} :MATCH {}".format(word,sorted_dict[2][1],3))