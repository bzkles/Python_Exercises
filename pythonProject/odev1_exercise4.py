#ODEV1
#Exercise4

def computepay():

    hours = int(input("hours: "))
    rate = int(input("rate:"))

    if hours < 40:
        pay = hours*rate
        print("Pay: ", pay)
    else:
        pay = int(40*rate + (hours-40)*rate*1.5)
        print("pay: ", pay)


if __name__ == "__main__":
   computepay()
