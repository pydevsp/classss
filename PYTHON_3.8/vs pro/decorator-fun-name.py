def print_name_decorator(xxxxxx):
    def decoration_function(name):
        print("............")
        xxxxxx(name.upper())
        print("---------------")
    return decoration_function


@print_name_decorator
def print_name(name):
    print("Mr." , name)





print_name("Suman")