def logger(func):
    def wrapper():
        print(f"some one called {func.__name__}")
        func()
        print(f" {func.__name__} is executed successfully")
    return wrapper

@logger
def processData():
    print("connecting to db")
    print("data processed")

processData()