import math

arithmetic_mean = lambda data: sum(data) / len(data)

geometric_mean = lambda data: math.exp(sum(math.log(value) for value in data) / len(data))

harmonic_mean = lambda data: len(data) / sum(1 / value for value in data)

def find_min(data, funcs):
    return min(func(data) for func in funcs)

def main() -> None:
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(find_min(data, [arithmetic_mean, geometric_mean, harmonic_mean]))

if __name__ == "__main__" : main()
