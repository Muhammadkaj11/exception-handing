try:
    n=int(input("enter a number"))
except ValueError as e:
    print("exception",e)
