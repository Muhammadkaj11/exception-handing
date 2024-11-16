try:
    m,a=eval(input("enter 2 numbers seperated by a comma:"))
except ValueError as e:
    print("exception",e)
except ZeroDivisionError as e:
    print("exception",e)
except SyntaxError as e:
    print("exception",e)
finally:
    print("the code will finally execute")