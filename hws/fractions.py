import json

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"[{self.numerator}/{self.denominator}]"

    def to_dict(self):
        return {'numerator': self.numerator, 'denominator': self.denominator}

    def from_dict(cls, data):
        try:
            numerator = data['numerator']
            denominator = data['denominator']
            return cls(numerator, denominator)
        except KeyError:
            raise ValueError("Invalid JSON format")

    def to_json(self):
        return json.dumps(self.to_dict())

    def from_json(cls, json_str):
        try:
            data = json.loads(json_str)
            return cls.from_dict(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.to_json())

    def load_from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                return cls.from_json(json_str)
        except FileNotFoundError:
            raise ValueError(f"File '{filename}' not found")
        except ValueError as e:
            raise e
        
    def reduce(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        common_divisor = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // common_divisor, self.denominator // common_divisor)

    def reduce(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        common_divisor = gcd(self.numerator, self.denominator)
        return Fraction(self.numerator // common_divisor, self.denominator // common_divisor)

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type")

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator).reduce()
        else:
            raise TypeError("Unsupported operand type")

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("Unsupported operand type")


fraction1 = Fraction(2, 3)
fraction2 = Fraction(3, 4)

# sum
result_add = fraction1 + fraction2
print(result_add)

# Subtraction
result_subtract = fraction1 - fraction2
print(result_subtract) 

# Multiplication
result_multiply = fraction1 * fraction2
print(result_multiply)

# Division
result_divide = fraction1 / fraction2
print(result_divide) 
