from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600) #Window viewport size (x,y)

    cel1 = Cell(win)
    cel1.has_left_wall = False
    cel1.draw(50, 50, 100, 100)

    cel2 = Cell(win)
    cel2.has_left_wall = False
    cel2.has_bottom_wall = False
    cel2.draw(100, 50, 150, 100)

    cel1.draw_move(cel2)

    cel3 = Cell(win)
    cel3.has_top_wall = False
    cel3.has_right_wall = False
    cel3.draw(100, 100, 150, 150)

    cel2.draw_move(cel3)

    cel4 = Cell(win)
    cel4.has_top_wall = False
    cel4.draw(150, 100, 200, 150)

    cel3.draw_move(cel4, True)

    win.wait_for_close()


main()