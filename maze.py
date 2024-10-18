from window import Window
from cell import Cell
import time
class Maze():
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x : int, cell_size_y : int, win: Window) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
            self._cells.append(col)
    
    def _draw_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                left_x = self.x1 + (i * self.cell_size_x)
                right_x = left_x + self.cell_size_x
                top_y = self.y1 + (j * self.cell_size_y)
                bottom_y = top_y + self.cell_size_y

                if j == 0:
                    self._cells[i][j].has_top_wall = True
                
                if i == 0:
                    self._cells[i][j].has_left_wall = True
                
                self._cells[i][j].draw(left_x, right_x, top_y, bottom_y)
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.1)


