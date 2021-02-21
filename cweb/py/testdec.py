def factory(nam):
    def my_decorator(func):
        def wrapper(arg):
            print("Something is happening before the function is called.")
            func(nam)
            print("Something is happening after the function is called.")
        return wrapper
    return my_decorator

@factory("nam")
def say_whee(arg):
    print("Whee!",arg)

say_whee("Hello")
