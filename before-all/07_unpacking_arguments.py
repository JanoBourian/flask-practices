def information(*args):
    for arg in args:
        print(arg)


information(1, 3, 6, 7, "Abelardo")


def users(**kwargs):
    for k in kwargs.values():
        print(k)


users(name="bob", age=19)
