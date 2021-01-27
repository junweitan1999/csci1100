'''
this file is used to printing out output of the rank of movies based on weight of imdb and weight of twitter during a period of time given by the 
user. The ranking of the movie 

'''


import json
if __name__ == "__main__":
    movies = json.loads(open("movies.json").read())
    ratings = json.loads(open("ratings.json").read())

min_year = int(input("Min year => "))
print(min_year)
max_year =int(input("Max year => "))
print(max_year)
w_imdb = input("Weight for IMDB => ")
print(w_imdb)
w_imdb=float(w_imdb)
if w_imdb %1 ==0:
    w_imdb=int(w_imdb)
w_twitter = float(input("Weight for Twitter => "))
if w_twitter %1 ==0:
    w_twitter=int(w_twitter)
print(w_twitter)
while True:
    print()
    input_genre = input("What genre do you want to see? ")  
    print(input_genre)
    input_genre=input_genre.lower()  
    if input_genre.strip()=="stop":
        break
    
    print()
    
    result=[]
    
    for movie in movies:
        for i in range(len(movies[movie]['genre'])):
            movies[movie]['genre'][i]=movies[movie]['genre'][i].lower()        
        if ((movies[movie]['movie_year'])>=min_year)and((movies[movie]['movie_year'])<=max_year)and(input_genre in movies[movie]['genre']):
            if movie in ratings:
                if len(ratings[movie])>2:
                    imdb=movies[movie]['rating']
                    twitter=sum(ratings[movie])/len(ratings[movie])
                    rate = (w_imdb*imdb + w_twitter*twitter)/(w_imdb+w_twitter)
                    result.append((rate,movies[movie]['name'],movies[movie]['movie_year']))
    result_rate=sorted(result)
    if len(result)==0:   
        input_genre=input_genre.title()
        print("No {} movie found in {} through {}".format(input_genre,min_year,max_year))
    else:        
        best_result=result_rate[-1]
        worst_result=result_rate[0]
        print("Best:\n\tReleased in {}, {} has a rating of {:.2f}".format(best_result[2],best_result[1],best_result[0]))
        print()
        print("Worst:\n\tReleased in {}, {} has a rating of {:.2f}".format(worst_result[2],worst_result[1],worst_result[0]))