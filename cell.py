from window import Window
from line import Line, Point
class Cell:
    def __init__(self, window: Window, left_wall = False, right_wall = True, top_wall = False, bottom_wall = True) -> None:
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self._win = window
        self._centre = None
    
    def draw(self, left_x: float, right_x: float, top_y: float, bottom_y: float, fill='blue'):
        self._centre = Point((left_x + right_x) / 2, (top_y + bottom_y) / 2)
        top_left = Point(left_x, top_y)
        bottom_left = Point(left_x, bottom_y)
        top_right = Point(right_x, top_y)
        bottom_right = Point(right_x, bottom_y)
        if self.has_left_wall:
            self._win.draw_line(Line(top_left, bottom_left), fill)

        if self.has_right_wall:
            self._win.draw_line(Line(top_right, bottom_right), fill)

        if self.has_top_wall:
            self._win.draw_line(Line(top_left, top_right), fill)
        
        if self.has_bottom_wall:
            self._win.draw_line(Line(bottom_left, bottom_right),fill)
    
    def draw_move(self, to_cell, undo=False):
        color = 'gray'
        if undo == True:
            color = 'red'
        self._win.draw_line(Line(self._centre, to_cell._centre), color)