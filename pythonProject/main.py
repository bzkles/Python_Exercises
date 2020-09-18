

def shut_down():
    s = input("Are you sure shut_down? Please enter yes / no ")
    if s == 'yes':
        print("shutting down")
    elif s == 'no':
        print("shutdown aborted")
    else:
        print("soryy")


if __name__ == "__main__":
   shut_down()