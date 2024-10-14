from window import Window
from line import Line, Point
class Cell:
    def __init__(self, window: Window, top_left: Point, bottom_right: Point, left_wall = True, right_wall = True, top_wall = True, bottom_wall = True) -> None:
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._top_left = top_left
        self._top_right = Point(top_left.y, bottom_right.x)
        self._bottom_left = Point(bottom_right.y, top_left.x)
        self._bottom_right = bottom_right
        self._win = window
    
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(self._top_left, self._bottom_left), 'blue')

        if self.has_right_wall:
            self._win.draw_line(Line(self._top_right, self._bottom_right), 'blue')

        if self.has_top_wall:
            self._win.draw_line(Line(self._top_left, self._top_right), 'blue')
        
        if self.has_bottom_wall:
            self._win.draw_line(Line(self._bottom_left, self._bottom_right),'blue')