#function
def number_happy(sentence):
    happynumber = sentence.count("laugh")
    happynumber += sentence.count("happiness")
    happynumber += sentence.count("love")
    happynumber += sentence.count("excellent")
    happynumber += sentence.count("good")
    happynumber += sentence.count("smile")
    return happynumber
def number_sad(sentence) :
    sadnumber = sentence.count("bad")
    sadnumber += sentence.count("sad")
    sadnumber += sentence.count("terrible")
    sadnumber += sentence.count("horrible")
    sadnumber += sentence.count("problem")
    sadnumber += sentence.count("hate")
    return sadnumber

#main body
sentence = input("Enter a sentence => ")
print(sentence)
sentence = sentence.lower()
happy = number_happy(sentence)
sad = number_sad(sentence)
print("Sentiment: "+"+"*happy+"-"*sad)
if happy > sad:
    print("This is a happy sentence.")
elif sad > happy:
    print("This is a sad sentence.")
else:
    print("This is a neutral sentence.")

