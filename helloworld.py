def hello(name):
    return "Hello World! My name is {}.".format(name.title())

x = input("Input your name: ")
print(hello(x))
