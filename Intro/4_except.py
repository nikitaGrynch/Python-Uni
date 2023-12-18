
def throw_msg() -> None :
    print("Raising message error")
    raise ValueError("This is a value error")

def no_throw() -> None :
    print("No error raised")

def main() -> None :

    try:
        throw_msg()
    except TypeError:
        print("TypeError detected")
    except ValueError as err:
        print("ValueError detected: ", err)
    except:
        print("Unknown error detected")
    finally:
        print("Finally action")

    try: 
        no_throw()
    except:
        print("Unknown error detected")
    else:
        print("No error detected")
    finally:
        print("Finally action")


if __name__ == "__main__" : main()