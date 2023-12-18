x = 10

def get_x():
    return x

def hello(name: str = "Anonymous") -> str:
    '''Function comment'''
    return f"Hello {name}!"

def change_x(value: int = 20) -> None:
    x = value
    print("Changed to ", x)

def set_x(value):
    global x
    x = value
    print("Set to ", x)

def pair():
    return 1, 2

def main():
    print("x =", get_x())
    
    print(hello(), hello("User"))

    change_x(1.5)
    print("x =", get_x())
    set_x(30)
    print("x =", get_x())

    y, w = pair()
    print(f"y = {y}, w = {w}")
    print("y=%d, w=%d" % pair())

if __name__ == "__main__": main()