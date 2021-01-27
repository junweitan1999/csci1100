word = input("Word => ")
print(word)
columns = int(input("#columns => "))
print(columns)
rows = int(input("#rows => "))
print(rows)  

print("Your word is:",word+"\n")

print("(a)")
print(("*** "*columns + "\n")*rows)

print("(b)")
print(("*** "*columns +"\n")*int(((rows-1)/2))+"*** "*int(((columns-1)/2))+"CS1 "+"*** "*int(((columns-1)/2)))
print(("*** "*columns +"\n")*int(((rows-1)/2)))


print("(c)")
print("*** "*int(((columns-1)/2))+" ^  "+"*** "*int(((columns-1)/2)))
print("*** "*int(((columns-3)/2))+" /  ***  \\  "+"*** "*int(((columns-3)/2))+("\n"+"*** "*int(((columns-3)/2))+" |  ***  |  "+"*** "*int(((columns-3)/2)))*int(((rows-5)/2)))
print("*** "*int(((columns-3)/2))+" |  CS1  |  "+"*** "*int(((columns-3)/2)))
print(("*** "*int(((columns-3)/2))+" |  ***  |  "+"*** "*int(((columns-3)/2))+"\n")*int(((rows-5)/2))+"*** "*int(((columns-3)/2))+" \\  ***  /  "+"*** "*int(((columns-3)/2)))
print("*** "*int(((columns-1)/2))+" v  "+"*** "*int(((columns-1)/2)))