# function to define the word is alternating or not 
def is_alternating(word):
    #initializing
    vowels = []
    letter=['a','b','c','d','e','f','g','h','j','k','l','i','o','u','m','n','p','q','r','s','t','v','w','x','y','z']
    judge = True
    same_or_not = True
    judgment =False        
    word_copy=word
    word=word.lower()
    if len(word) <8:
        print("The word '{0}' is not alternating".format(word))
        return False
    for i in word:
        if i not in letter:
            print("The word '{0}' is not alternating".format(word))
            return False
    else:
        #see the first letter is vowel or not 

        if word[0] == "a" or word[0]== "e" or word[0]=="o" or word[0]=="u" or word[0]=="i":
            judgement = True
        else:
            judgement = False
        # the following loop make sure that the next letter is different from the previous letter by changing from vowel to consonant
        for i in word:
            if i == "a" or i== "e" or i=="o" or i=="u" or i=="i":
                vowels.append(i)
                judge =False
            else :
                judge =True
            # if the next word has the same judge as the previous one , then it is not alternating
            if judgement ==judge :
                print("The word '{0}' is not alternating".format(word_copy))
                return False
            judgement=judge
        # copy the vowel list and sort it to see whether the sequence of the vowels follows the rule
        check_vowels = vowels.copy()
        vowels.sort()            
        # if two list is inconsistent then the word is not alternating
        if vowels != check_vowels:
            print("The word '{0}' is not alternating".format(word_copy))
            return False
        # else, it is
        else:
            print("The word '{0}' is alternating".format(word_copy))
            return True
    # the main program
    # unless the word is "" , the program will pop up Enter a word until the user enter""
while True:
    word = input("Enter a word: ")    
    if  word =="":
        break
    print(word)
    is_alternating(word)
    print()

    