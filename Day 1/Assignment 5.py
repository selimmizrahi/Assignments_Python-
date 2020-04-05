
def build_pyramid(lenght):
    for i in range(0,lenght,2):
        print(" "*lenght + i*"*")
        lenght = lenght - 1

build_pyramid(12)

