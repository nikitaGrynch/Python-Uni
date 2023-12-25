def create_file1():
    filename = "file1.txt"
    file = None
    try:
        file = open(filename, "w")
        file.write("Latin data\n")
        file.write("Клириллица\n")
    except OSError as err:
        print("OSError: ", err)
    else:
        file.flush()
        print("File created")
    finally:
        if file is not None:
            file.close()

def read_all_text1(filename: str) -> str:
    file = None
    try:
        file = open(filename, "r")
    except IOError as err:
        print("IOError: ", err)
    else:
        return file.read()
    finally:
        if file is not None:
            file.close()

def create_headers(filename: str) -> None:
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write("Host: localhost\r\n")
            file.write("Connection: close\r\n")
            file.write("Content-Type: text/css\r\n")
            file.write("Content-Length: 100500\r\n")
    except IOError as err:
        print("Create headers error: ", err)
    else:
        print("Headers created")

def print_headers(filename: str) -> None:
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            for line in file:
                print(line)
    except IOError as err:
        print("Read headers error: ", err)

def parse_headers(filename: str) -> dict:
    headers = {}
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            #for line in file:
                # if(":" in line):
                #     key, value = line.split(":")
                #     headers[key.strip()] = value.strip()
            # same but in functional style
            #headers = dict(map(lambda line: line.strip().split(":") if ":" in line else None, file))
            return { k: v
                    for k, v in (
                        map(str.strip,
                            line.split(":") )
                        for line in file
                        if ":" in line
                    )}
    except IOError as err:
        print("Read headers error: ", err)
    else:
        return headers


def main() -> None:
    #create_file1()
    #print(read_all_text1("file1.txt"))
    #create_headers("headers.txt")
    #print_headers("headers.txt")

    for k, v in parse_headers("headers.txt").items():
        print(k, v)

    # lam = lambda : print()
    # lam.name = "lam"
    # print(lam.name)
    pass

if __name__ == "__main__" : main()