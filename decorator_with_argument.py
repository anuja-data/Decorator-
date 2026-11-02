def my_decorator(func):
    def wrapper(name):
        print("Welcome!")
        func(name)
        print("Thank you!")
    return wrapper

@my_decorator
def greet(name):
    print("Hello", name)

greet("Rahul")