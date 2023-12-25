import json

def create_json_file() -> None:
    try:
        with(open("data.json", mode="w", encoding="utf-8")) as file:
            file.write('''{
                        "str": "Hello, world!",
                        "digital": 123,
                        "float": 1.5,
                        "bool1": true, 
                        "null": null,
                        "obj": {
                            "bool0": false,
                            "str": "A string"
                        },
                        "arr": [1, 2, 3, 4, 5]
            }''')
    except IOError as err:
        print("Error: ", err)


def print_json():
    try:
        with open("data.json", mode="r", encoding="utf-8") as file:
            j = json.load(file)
            print(type(j), j)
            for k in j: print(k, j[k])
            j['cyr'] = "Кириллица"
            print('================================')
            print(j)
            print(json.dumps(j))
            print(json.dumps(j, ensure_ascii=False, indent=2))
    except IOError as err:
        print("Error: ", err)

def main():
    #create_json_file()
    print_json()

if __name__ == "__main__": main()