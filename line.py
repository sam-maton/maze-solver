class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, pointA: Point, pointB: Point) -> None:
        self.pointA = pointA
        self.pointB = pointB

    def draw(self, canvas, fill):
        pass