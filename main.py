from window import Window
from line import Point,Line
from cell import Cell

def main():
    win = Window(800, 600)
    

    first_cell = Cell(win)
    first_cell.draw(20, 300, 20, 300)

    second_cell = Cell(win)
    second_cell.draw(310, 590, 20, 300)
    
    first_cell.draw_move(second_cell)
    win.wait_for_close()



main()