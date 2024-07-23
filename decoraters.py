def announce(f):
    def wrapper():
        print("About to run fuction.")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, world")

hello() 

# ex is when user login