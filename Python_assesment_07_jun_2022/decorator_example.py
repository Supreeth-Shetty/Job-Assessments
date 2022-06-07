import time

def smart_division(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

def time_taken(func):
    def inner(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print("Time taken by function:",func.__name__,"is",end-start)
        return result
    return inner


@smart_division # adding smart_division as a decorator to the division function adds smart_division functionality 
@time_taken # adding time_taken as a decorator to the division function adds time_taken functionality
def division(a,b):
    print(f"The smart divsion result is : {a/b}")

division(2,4)


print("""
1) Decorator helps us to warp one function with another function.
2) This helps us to add some additional functionality to the function without altering existing function.
""")



