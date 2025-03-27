from src.decorators import log


@log("mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)