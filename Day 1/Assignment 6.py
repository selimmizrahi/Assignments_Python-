
def build_pyramid(lenght):
    if lenght > 0:
        for i in range(1, lenght * 2, 2):
            print(" " * lenght + i * "*")
            lenght = lenght - 1
        return True
    else:
        print("Oops input should be integer or larger then 0")
        return False


while True:
    try:
        input1 = int(input("Type number of rows you want in the pyramid"))
        break
    except ValueError:
        print("Oops input should be integer or larger then 0")

build_pyramid(input1)
