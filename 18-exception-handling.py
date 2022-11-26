while True:
    try:
        x = int(input("enter the your number : "))
        print(x, ' is the number')
        break
    except NameError:
        print("Only Number Allowed")
        
