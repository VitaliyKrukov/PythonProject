import os

from src.decorators import log


def test_log(capsys):
    @log()
    def foo(x, y):
        return x / y

    foo(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "foo ok\n"


def test_log_error(capsys):
    @log()
    def foo(x, y):
        return x / y

    try:
        foo(4, 0)
    except Exception:
        pass
    captured = capsys.readouterr()
    assert captured.out == "foo error: ZeroDivisionError.Inputs: (4, 0), {}\n"


def test_log_error_file():
    @log("test.log")
    def foo(x, y):
        return x / y

    try:
        foo(4, 0)
    except Exception:
        pass

    with open("test.log", "r", encoding="utf-8") as file:
        assert (
            file.read() == "foo error: ZeroDivisionError.Inputs: (4, 0), {}\n"
        )
    os.remove("test.log")


def test_log_file():
    @log("test.log")
    def foo(x, y):
        return x / y

    foo(4, 2)

    with open("test.log", "r", encoding="utf-8") as file:
        assert file.read() == "foo ok\n"
    os.remove("test.log")
