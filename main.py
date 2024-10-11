from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(height=height, width=width)
        self.canvas.pack()

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

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()