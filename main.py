from window import Window
from line import Point,Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    firstPoint = Point(20,20)
    secondPoint = Point(300,300)

    first_cell = Cell(win, firstPoint, secondPoint)
    first_cell.draw()
    
    
    win.wait_for_close()



main()