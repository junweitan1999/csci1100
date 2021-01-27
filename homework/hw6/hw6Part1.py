'''
This python file is going to correct the word in a text file to appropriate form according to another dictionary file 

Junwei Tan
'''

# this is the function return the appropriate form of the word and a string of the method that i replace the word 

def find_word(word1):
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'y', 'z' ]
    if word1 in dictionary:
        return (word1,"FOUND")
    for i in range(len(word1)):
        # drop method: drop a letter from the original word
        for i in range(len(word1)-1):
            test_word=word1[:i]+word1[i+1:] 
            if test_word in dictionary:
                return (test_word,"DROP")
        test_word1=word1[:len(word1)-1]
        if test_word1 in dictionary:
            return (test_word1,"DROP")
        # swap method:  change the order of two concatenate letter in the word
    for i in range(len(word1)-2):    
        test_word=word1[:i]+word1[i+1]+word1[i]+word1[i+2:]
        if test_word in dictionary:
            return (test_word,"SWAP")
    test_word=word1[:len(word1)-2]+word1[len(word1)-1]+word1[len(word1)-2]
    if test_word in dictionary:
        return (test_word,"SWAP")
    # replace method: replace one letter in the word by using another letter
    for i in range(len(word1)):                  
        for j in range(len(letters)):
            test_word=word1[:i]+letters[j]+word1[i+1:]
            if test_word in dictionary: 
                return (test_word,"REPLACE")
    else:
        return (word1,"NO MATCH")

# ask user for the input word file and the dictionary file
dictionary = input("Dictionary file => ")
print(dictionary)
inputfile = input("Input file => ")
print(inputfile)
# read all the lines and store them in the variable
dictionary_name=open(dictionary,"r")
dictionary=dictionary_name.readlines()
dictionary_name.close()
input_name=open(inputfile,"r")
input_file =input_name.readlines()
# strip the \n in the last of the line 
for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].strip()
for i in range(len(input_file)):
    input_file[i] = input_file[i].strip()
dictionary = set(dictionary)


for word in input_file :
    result= find_word(word)
    print("{:<15} -> {:<15} :{}".format(word,result[0],result[1]))