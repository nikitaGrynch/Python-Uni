class Point:
    x = 0
    y = 0

def demo1() -> None:
    p1 = Point()
    p2 = Point()
    print(p1.x, p1.y, Point.x)
    Point.x = 10
    print(p1.x, p2.x, Point.x)
    p1.x = 20
    print(p1.x, p2.x, Point.x)
    del p1.x
    print(p1.x, p2.x, Point.x)


class Vector :
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = 0
        self.y = 0

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"<Vector>({self.x}, {self.y})"
    
    def __add__(self, other):
        if(isinstance(other, Vector)) :
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can't add Vector and non-Vector")
        
    
    def __mul__(self, other):
        if(isinstance(other, (int, float))):
            return Vector (self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
    
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y) ** (1/2)
    
    def translate(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy


def demo2() -> None:
    v1 = Vector()
    v2 = Vector(1)
    v3 = Vector(1, -1)
    v4 = Vector(y=-1)
    print(v1, v2, v3 + v4)
    print(v3.magnitude())
    v3.translate(0.1, 0.2)
    print(v3)
    v4 = v3 + v3
    print(repr(v4), repr(v3), repr(v2), repr(v1))
    print(f"{v4} * {v3} =", v1 * v2)
    print(f"{v3} * 2 =", v3 * 2)


def main() -> None:
    demo2()


if __name__ == "__main__" : main()