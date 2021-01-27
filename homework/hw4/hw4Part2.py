import hw4_util
import math
# reading all the data in the csv file
zip_codes = hw4_util.read_zip_all()
# this function take a tuple has the meaning of the location of a place and return a list of that zipcodes that the place has
def zip_by_location(zip_codes, location):
    zipcode=[]
    for code in zip_codes :
        location[0] = location[0].capitalize()
        location[1] = location[1].upper()
        
        if code[3] == location[0] and code[4] ==location[1]:
            zipcode.append(code[0])
    if zipcode ==[]:
        return False
    return zipcode

# this function takes a zipcode as input and return the location information as a list
def location_by_zip(zip_codes, code) :
    location=[]
    for zipcode in zip_codes:
        if zipcode[0] == code:
            location.append(zipcode[1])
            location.append(zipcode[2])
            location.append(zipcode[3])
            location.append(zipcode[4])
            location.append(zipcode[5])
    if location ==[]:
        return False
    return location 
# this function take a float as input and change it from degree mode to second mode
def degree_to_second (degree):
    degree_int =int(degree)
    degree_remain = degree - degree_int
    degree_remain = degree_remain *60
    degree_min = int(degree_remain)
    degree_remain = degree_remain - degree_min
    degree_remain =degree_remain *60
    return (degree_int,degree_min,degree_remain)

while True:
    cmd = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(cmd)
    cmd = cmd.lower()
    if cmd =="loc":
        zipcode = input("Enter a ZIP code to lookup => ")
        print(zipcode)
        # if the zipcode that user enters cannot be found in the list, the function will return false and invalid message will appear
        if location_by_zip(zip_codes, zipcode) ==False :
            print("Invalid or unknown ZIP code")
        else:
            # printing out all of the location information from the returned list
            location = location_by_zip(zip_codes, zipcode)
            print("ZIP code {0} is in {1}, {2}, {3} county,".format(zipcode,location[2],location[3],location[4]))
            n_s = degree_to_second (location[0])
            e_w = degree_to_second (location[1])
            n_s_string =""
            e_w_string =""
            # judging whether the longitute and lattitute is positive or not to show "NSEW" followed by the second mode data
            if location[0]< 0:
                locate = abs(location[0])
                n_s = degree_to_second (locate)
                n_s_string = "{0:03d}\xb0{1}'{2:.2f}\"S".format(n_s[0],n_s[1],n_s[2])
            elif location[0]>0:
                n_s_string = "{0:03d}\xb0{1}'{2:.2f}\"N".format(n_s[0],n_s[1],n_s[2])
            if location[1]<0:
                locate = abs(location[1])
                e_w = degree_to_second (locate)
                e_w_string = "{0:03d}\xb0{1}'{2:.2f}\"W".format(e_w[0],e_w[1],e_w[2])
            elif location[1]>0:
                e_w_string = "{0:03d}\xb0{1}'{2:.2f}\"E".format(e_w[0],e_w[1],e_w[2])
            print("\tcoordinates: ({0},{1})".format(n_s_string,e_w_string))
    
    
    elif cmd=="zip":
        city = input("Enter a city name to lookup => ")
        print(city)
        state=input("Enter the state name to lookup => ")
        print(state)
        # put the user input into a list
        location=[]
        location.append(city)
        location.append(state)
        location = zip_by_location(zip_codes, location)

        city = city.lower()
        city = city.capitalize()
        state = state.upper()        
        if location ==False:
            # if the zipcode cannot be found the function will return false and the error message will occur
            print("No ZIP code found for {0}, {1}".format(city,state))
        else:
            zipcode= ""
            # this loop put all of the zipcode into a string
            for i in location :
                zipcode = zipcode + i + ", "
            zipcode = zipcode.strip()
            zipcode = zipcode.strip(",")
            print("The following ZIP code(s) found for {0}, {1}: {2}".format(city,state,zipcode))
        
    elif cmd == "dist" : 
        zipcode1 = input("Enter the first ZIP code => ")
        print(zipcode1)
        zipcode2 = input("Enter the second ZIP code => ")
        print(zipcode2)
        if location_by_zip(zip_codes, zipcode1)==False or location_by_zip(zip_codes, zipcode2)==False :
            # error message pop out
            print("The distance between {0} and {1} cannot be determined".format(zipcode1,zipcode2))
        else:
            # converting degree data to radiant data
            # and then subsistute the data into the formula and return the distant
            location1 = location_by_zip(zip_codes, zipcode1)
            location2 = location_by_zip(zip_codes, zipcode2)
            pi = math.pi
            change_lattitude = location2[0]-location1[0]
            change_longitude = location2[1]-location1[1]
            change_lattitude = change_lattitude * pi / 180
            change_longitude = change_longitude * pi / 180
            lattitude1 = location1[0]*pi/180
            lattitude2 = location2[0]*pi/180
            distance = 2*3959.191*math.asin(math.sqrt((math.sin(change_lattitude/2))**2 + math.cos(lattitude1) * math.cos(lattitude2) * (math.sin(change_longitude/2))**2))
            print("The distance between {0} and {1} is {2:.2f} miles".format(zipcode1,zipcode2,distance))
            # unless user enter end the program wont stop
    elif cmd =="end": 
        print()
        print("Done")
        break
    else:
        print("Invalid command, ignoring")
    print()