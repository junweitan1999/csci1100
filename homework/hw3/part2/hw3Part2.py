import hw3_util


text = input("Enter the coin file name => ")
print(text)
coins = hw3_util.read_change(text)
cost = input("Enter the item cost in cents (0-100) => ")
print(cost)
cost=float(cost)
if cost<0 or cost>100 or cost%1 !=0:
    print("invalid input")
else:
    print()
    print("I have the following coins:")
    print(coins)
    cost=int(cost)
    change = 100-cost

    print("Change from $1.00 is {0} cents".format(change))

    count_50 = coins.count(50)
    count_25 = coins.count(25)
    count_10 = coins.count(10)
    count_5 = coins.count(5)
    count_1 = coins.count(1)
    number_50=0
    number_25=0
    number_10=0
    number_5=0
    remain=0
    if change>=50:
        if change//50<= count_50:
            number_50=change//50
            change = change%50
        else:
            number_50 = count_50
            change=change-count_50*50
    if change>=25:
        if change//25<= count_25:
            number_25=change//25
            change = change%25
        else:
            number_25 = count_25
            change=change-count_25*25
    if change>=10:
        if change//10<= count_10:
            number_10=change//10
            change = change%10
        else:
            number_10 = count_10
            change=change-count_10*10
    if change>=5:
        if change//5<= count_5:
            number_5=change//5
            change = change%5
        else:
            number_5 = count_5
            change=change-count_5*5
    if count_1 >= change:
        remain = change
        print("{0} Half Dollars, {1} Quarters, {2} Dimes, {3} Nickels, {4} Pennies".format(number_50,number_25,number_10,number_5,remain))
    else:
        additional = change-count_1
        print("I cannot make change with my current coins.")
        print("I need an additional {0} cents.".format(additional))