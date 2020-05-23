# def decor(wish):
#     c


# @decor
# def wsh(name):
#     print("Hello",name,"Good Morning!")
    
    
# wsh("Durga")
# wsh("Nag")
# wsh("Anil") 



def decor(original):
    print('decorrr ...')
    def inner1(name): 
        print("Hello, this is before function execution") 
        original(name) 
        print("This is after function execution") 
    return inner1 

@decor
def wsh(name):
    print("Hello",name,"Good Morning!")
    
    
wsh("Durga")
# wsh("Nag")
# wsh("Anil") 