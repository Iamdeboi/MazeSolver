from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    li = Line(Point(0, 50), Point(600, 200))
    win.draw_line(li, "black")
    win.wait_for_close()


main()