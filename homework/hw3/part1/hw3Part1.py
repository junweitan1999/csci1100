import read_names

# read all file and store the data
read_names.read_from_file("top_names_1880_to_2014.txt")

# ask for the input and the completion of example 1
year = int(input("Enter a year (1881-2013) => "))
print(year)
rank = int(input("Enter a rank (1-250) => "))
print(rank)

def number_stars (list_names,list_counts,name):
    if list_names.count(name)==0:
        number_stars=0
        percentage=0.0
    else:
        ranking = list_names.index(name)
        percentage = list_counts[ranking]/sum(list_counts)
        percentage = percentage*100
        number_stars = int(percentage/0.1)
    return (number_stars,percentage)
# the case about the year is not in the range 1881-2013
if year < 1881 or year > 2013 or rank < 1 or rank > 250:
    print("{0} is not in the range 1881-2013 or {1} is not in the range 1-250".format(year,rank))
else:
    (female_names1,female_counts1) = read_names.top_in_year(year-1, 'f')
    (female_names2,female_counts2) = read_names.top_in_year(year, 'f')
    (female_names3,female_counts3) = read_names.top_in_year(year+1, 'f')
    print("The rank {0} most popular female name in {1} is {2}".format(rank,year,female_names2[rank-1]))

    sum_counts = sum(female_counts2)
    percent_counts = female_counts2[rank-1]/sum_counts*100
    print("\t{0} out of {1} or {2:.2f}%".format(female_counts2[rank-1],sum_counts,percent_counts))

#print out the histogram
    print("Histogram for {0}".format(female_names2[rank-1]))
    name=female_names2[rank-1]
    number_stars1 = number_stars(female_names1,female_counts1,name)
    print("{0}:\t".format(year-1)+"*"*number_stars1[0]+"\t({0:.2f}%)".format(number_stars1[1]))
    number_stars2 = number_stars(female_names2,female_counts2,name)
    print("{0}:\t".format(year)+"*"*number_stars2[0]+"\t({0:.2f}%)".format(number_stars2[1]))
    number_stars3 = number_stars(female_names3,female_counts3,name)
    print("{0}:\t".format(year+1)+"*"*number_stars3[0]+"\t({0:.2f}%)".format(number_stars3[1]))
    print()

    #male part of program
    (male_names1,male_counts1) = read_names.top_in_year(year-1, 'M') 
    (male_names2,male_counts2) = read_names.top_in_year(year, 'M') 
    (male_names3,male_counts3) = read_names.top_in_year(year+1, 'M') 
    print("The rank {0} most popular male name in {1} is {2}".format(rank,year,male_names2[rank-1]))
    sum_counts = sum(male_counts2)
    percent_counts = male_counts2[rank-1]/sum_counts*100
    print("\t{0} out of {1} or {2:.2f}%".format(male_counts2[rank-1],sum_counts,percent_counts))
    print("Histogram for {0}".format(male_names2[rank-1]))
    name=male_names2[rank-1]
    number_stars4 = number_stars(male_names1,male_counts1,name)
    print("{0}:\t".format(year-1)+"*"*number_stars4[0]+"\t({0:.2f}%)".format(number_stars4[1]))
    number_stars5 = number_stars(male_names2,male_counts2,name)
    print("{0}:\t".format(year)+"*"*number_stars5[0]+"\t({0:.2f}%)".format(number_stars5[1]))
    number_stars6 = number_stars(male_names3,male_counts3,name)
    print("{0}:\t".format(year+1)+"*"*number_stars6[0]+"\t({0:.2f}%)".format(number_stars6[1]))