def is_parsable(anything):
    if type(anything) == int or str:
        return True
    else:
        return False


while True:
    try:
        input1 = input("Type something")
        break
    except ValueError:
        print("Oops number should be integer or string")


is_parsable(input1)
