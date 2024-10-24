from tkinter import Tk, BOTH, Canvas
from line import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, height=height, width=width, background='white')
        self.canvas.pack(fill=BOTH,  expand=1)

        self.running = False
    
    def redraw(self):
        self.canvas.update_idletasks()
        self.canvas.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill: str):
        line.draw(self.canvas, fill)