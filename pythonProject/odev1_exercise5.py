#ODEV1
#Exercise5


night = int(input("How many nights?"))
city = input("Please enter city: Tampa ,Los Angeles , Charlotte , Pittsburgh")
rent_day = int(input("How many days will you rent a car? "))
spending_money = int(input("Enter your spending money: "))

def hotel_cost(night):
    hotelcost = int((night*140))
    return hotelcost

def plane_ride_cost(city):


    if city == 'Charlotte':return 183
    elif city =='Tampa': return 220
    elif city =='Pittsburgh': return 222
    elif city =='Los Angeles': return 475
    else:
        print("Please try again")
        return plane_ride_cost(city)


def rental_car_cost(rent_day):

    total_car_cost = int(rent_day*40)
    if rent_day >= 7:
        total_car_cost -= 50
    elif rent_day >= 3:
        total_car_cost -= 20
    elif 0 < rent_day < 3:
        total_car_cost
    else:
        print("invalid input")
    return total_car_cost

def trip_cost(city,days,spending_money):
    print(rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money,"$")

trip_cost(city,rent_day,spending_money)




