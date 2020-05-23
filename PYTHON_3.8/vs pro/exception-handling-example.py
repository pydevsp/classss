def divide(a,b):
    try: 
        
        print (a/b)
    except ZeroDivisionError : 
        print (a/1)
    except TypeError as err: 
        print(err)
        print("pass only numbers")
    except : 
        print("Error ")    
        
divide(10,0)

#ZeroDivisionError:
#TypeError: