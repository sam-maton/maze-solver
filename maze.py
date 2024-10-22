from window import Window
from cell import Cell
import time
import random
class Maze():
    def __init__(self, x1: int, y1: int, num_rows: int, num_cols: int, cell_size_x : int, cell_size_y : int, win: Window = None, seed = None) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: list[list[Cell]] = []
        self.seed = seed

        if self.seed is not None:
            random.seed(self.seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(self.win))
            self._cells.append(col)
        
        for col in range(len(self._cells)):
            for row in range(len(self._cells[i])):
                self._draw_cell(col,row)
        

    
    def _draw_cell(self, i, j):
        left_x = self.x1 + (i * self.cell_size_x)
        right_x = left_x + self.cell_size_x
        top_y = self.y1 + (j * self.cell_size_y)
        bottom_y = top_y + self.cell_size_y
        
        self._cells[i][j].draw(left_x, right_x, top_y, bottom_y)
    
    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.1)

    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self.num_cols -1][self.num_rows -1]

        entrance.has_top_wall = False
        exit.has_bottom_wall = False

        self._draw_cell(0,0)
        self._draw_cell(self.num_cols -1, self.num_rows -1)

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j]._visited = True

        while True:
            to_visit: list[tuple[int,int]] = []
            if i > 0:
                if self._cells[i - 1][j]._visited is False:
                    to_visit.append((i - 1, j))
            if i < self.num_cols - 1:
                if self._cells[i + 1][j]._visited is False:
                    to_visit.append((i + 1,j))
            if j > 0:
                if self._cells[i][j - 1]._visited is False:
                    to_visit.append((i,j - 1))
            if j < self.num_rows - 1:
                if self._cells[i][j + 1]._visited is False:
                    to_visit.append((i,j + 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            next = to_visit[random.randrange(len(to_visit))]

            if next[0] < i:
                self._cells[next[0]][next[1]].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            if next[0] > i:
                self._cells[next[0]][next[1]].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            if next[1] < j:
                self._cells[next[0]][next[1]].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            if next[1] > j:
                self._cells[next[0]][next[1]].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            self._draw_cell(i,j)
            self._draw_cell(next[0], next[1])

            self._break_walls_r(next[0], next[1])
    
    def _reset_visited(self):
        for col in self._cells:
            for cell in col:
                cell._visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i: int, j: int):
        self._animate()
        self._cells[i][j]._visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        current = self._cells[i][j]
        if i > 0:
            left = self._cells[i - 1][j]
            if not left.has_right_wall and not left._visited and not current.has_left_wall:
                current.draw_move(left)
                move = self._solve_r(i - 1, j)
                if move == True:
                    return True
                else:
                    current.draw_move(left, undo=True)
        
        if i < self.num_cols - 1:
            right = self._cells[i + 1][j]
            if not right.has_left_wall and not right._visited and not current.has_right_wall:
                current.draw_move(right)
                move = self._solve_r(i + 1, j)
                if move == True:
                    return True
                else:
                    current.draw_move(right, undo=True)
        
        if j > 0:
            top = self._cells[i][j - 1]
            if not top.has_bottom_wall and not top._visited and not current.has_top_wall:
                current.draw_move(top)
                move = self._solve_r(i, j - 1)
                if move == True:
                    return True
                else:
                    current.draw_move(top, undo=True)
        
        if j < self.num_rows - 1:
            bottom = self._cells[i][j + 1]
            if not bottom.has_top_wall and not bottom._visited and not current.has_bottom_wall:
                current.draw_move(bottom)
                move = self._solve_r(i, j + 1)
                if move == True:
                    return True
                else:
                    current.draw_move(bottom, undo=True)

        return False
        
        
