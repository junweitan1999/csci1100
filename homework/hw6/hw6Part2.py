'''
This python file is to read a file that contains the names of the movies and the monsters in the movies in a single line. I read the file and store the information in several list and sets to give otu the correct output by modifying these lists and set 

Junwei Tan
'''

# importing textwrap moduel 
import textwrap

# initialize the program 
titlelst=[]
monsterlst=[]
monsterset=set()
newbook=[]
bookdict = dict()
# read the file and strip the \n in the last of the line and split the line by using "|"
for book in open("titles.txt"):
    newbook.append(book.strip("\n").split("|"))

# seperate the name of the movie and the monster in hte movie
# store the name of the movie and the monster in hte movie in a dictionary 
# also store them as string in two list respectively
for book in newbook:
    titlelst.append(book[0])
    monsterlst.append(book[1:])
    bookdict[book[0]]=book[1:]
    for i in range(1,len(book)):
        monsterset.add(book[i])

# this loop makes the program keep asking the user for input file name until user type in stop
while True:
    title=input("Enter a title (stop to end) => ")
    
    print(title)
    title=title.title()
    if title=="Stop":
        break
    else:
        
        find_title =[]
        for each_title in titlelst:
            if title in each_title:
                find_title.append(each_title)
                # if no title is found in the list , then print out 'this title is not found!'
        if(find_title==[]):
            print("")
            print("This title is not found!")
        else:
            # print out the first title in the list 
            print("")
            print("Found the following title: "+find_title[0])            
            title_index = titlelst.index(find_title[0])
            monster_title = []
            for monster in bookdict[find_title[0]]:
                monster_title.append(monster)
            # sort out the list and use a loop to print out beast in this title
            monster_title.sort()
            monster_title_string = "Beasts in this title: "
            for monster in monster_title:
                monster_title_string +=monster+", "
            monster_title_string = monster_title_string.strip()
            monster_title_string = monster_title_string.strip(",")
            # after we get the long string, use the wrap function to split the string into a list
            # after that, use a loop to print out the output
            monster_wrap=textwrap.wrap(monster_title_string)
            for monster in monster_wrap:
                print(monster)
            print()
            
            # use a nested loop to find the title that has the same monster as the founded title does
            monster_set = set(monster_title)
            monster_common_title = set()
            for monster in monster_set:
                for title in bookdict:
                    if monster in bookdict[title]:
                        monster_common_title.add(title)
                # use a loop to print out the outpput 
            monster_common_title=list(monster_common_title)
            monster_common_title.remove(find_title[0])
            monster_common_title.sort()
            monster_common_string = "Other titles containing beasts in common: "
            for monster in monster_common_title:
                monster_common_string +=monster+", "
            monster_common_string = monster_common_string.strip()
            monster_common_string = monster_common_string.strip(",")
            monster_wrap=textwrap.wrap(monster_common_string)
            for monster in monster_wrap:
                print(monster)
            print()            
            # use difference function to print out the difference of two set and use loop to print out the output
            monsterset = set()
            monsterlst.pop(title_index)
            for i in range(len(monsterlst)):
                for monster in monsterlst[i]:
                    monsterset.add(monster)
            only=monster_set.difference(monsterset)
            only=list(only)
            only.sort()
            monster_only_string = "Beasts appearing only in this title: "
            for monster in only:
                monster_only_string +=monster+", "
            monster_only_string = monster_only_string.strip()
            monster_only_string = monster_only_string.strip(",")
            monster_wrap=textwrap.wrap(monster_only_string)            
            for monster in monster_wrap:
                print(monster)
            print()                  