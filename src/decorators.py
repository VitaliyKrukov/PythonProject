from typing import Any, Callable


def log(filename: str = "") -> Callable:
    """Декоратор для логирования работы функции."""

    def decor(func: Callable) -> Callable:
        def wrapper(*args: tuple[Any], **kwargs: dict[Any, Any]) -> Any:
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
                    print(
                        f"{func.__name__} error: {type(error).__name__}"
                        f".Inputs: {args}, {kwargs}"
                    )
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"{func.__name__} error: {type(error).__name__}"
                            f".Inputs: {args}, {kwargs}\n"
                        )
                raise error

        return wrapper

    return decor
