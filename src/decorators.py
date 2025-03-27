def log(filename=""):
    def decor(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename == "":
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                return result
            except Exception as error:
                if filename == "":
                    print(f"{func.__name__} error: {type(error).__name__}.Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {type(error).__name__}.Inputs: {args}, {kwargs}\n")
                raise error

        return wrapper

    return decor
