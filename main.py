from window import Window
from line import Point,Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 800)
    

    # first_cell = Cell(win)
    # first_cell.draw(20, 120, 20, 120)

    # second_cell = Cell(win)
    # second_cell.draw(310, 590, 20, 300)
    
    # first_cell.draw_move(second_cell)
    new_maze = Maze(10, 10, 9, 9 , 80, 80, win)
    new_maze._break_entrance_and_exit()

    win.wait_for_close()



main()