from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600) #Window viewport size (x,y)

    cel = Cell(win)
    cel.has_left_wall = False
    cel.draw(50, 50, 100, 100)

    cel = Cell(win)
    cel.has_right_wall = False
    cel.draw(125, 125, 200, 200)

    cel = Cell(win)
    cel.has_bottom_wall = False
    cel.draw(225, 225, 250, 250)

    cel = Cell(win)
    cel.has_top_wall = False
    cel.draw(300, 300, 500, 500)

    win.wait_for_close()


main()