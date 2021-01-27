first_word = input("First => ")
print(first_word)
second_word = input("Second => ")
print(second_word)
print("Example variable names")

lower_case=first_word+"_"+second_word
print("Lower case:",lower_case,len(lower_case))

for_constants = lower_case.upper()
print("For constants:",for_constants,len(for_constants))

camel_case = first_word.capitalize()+second_word.capitalize()
print("Camel case:",camel_case,len(camel_case))

system_variables = "_"+first_word+"_"+second_word
print("System variables:",system_variables,len(system_variables))

first_word=first_word.replace("l","_")
second_word=second_word.replace("l","_")
second_word=second_word.replace("o","_")
silly_variable = first_word+"_"+second_word
print("Silly variable:",silly_variable)