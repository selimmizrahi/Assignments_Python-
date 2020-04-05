def is_even(number1):
    if number1 % 2 == 0:
        print(number1)
        return True


while True:
    try:
        number = int(input("Type a number"))
        break
    except ValueError:
        print("Oops number should be integer")

is_even(number)