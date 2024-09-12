from tkinter import *
from cell import Cell
from timer import Timer
from timer_manager import initialize_timer
import settings as st
import utils

root = Tk()

# window settings
root.configure(bg='black')
root.geometry(f'{st.WIDTH}x{st.HEIGHT}+540+80')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(root, bg='black', width=st.WIDTH, height=utils.height_percent(15))
top_frame.place(x=0, y=0)

game_title = Label(top_frame, text='MINESWEEPER', bg='black', fg='green', font=('MS Sans Serif', 38))
game_title.place(x=50, y=15)

# right_frame = Frame(root, bg='black', width=utils.width_percent(21), height=utils.height_percent(69))
# right_frame.place(x=utils.width_percent(79), y=utils.height_percent(10))

game_frame = Frame(root, bg='grey', width=utils.width_percent(80), height=utils.height_percent(70))
game_frame.place(x=0, y=utils.height_percent(15))

bottom_frame = Frame(root, bg='black', width=st.WIDTH, height=utils.height_percent(15))
bottom_frame.place(x=0, y=utils.height_percent(85))

# create timer-label
timer_label = Label(bottom_frame, text="⏱: 00:00", bg='black', fg='green', font=["MS Sans Serif", 24, "bold"])
timer_label.place(x=300, y=10)
initialize_timer(root, timer_label)

# make the board
for i in range(st.GRID_SIZE):
    for j in range(st.GRID_SIZE):
        c = Cell(root, i, j)
        c.create_btn_obj(game_frame)
        c.cell_btn_obj.grid(row=i, column=j)

# call mines_left label
Cell.mines_left_label(bottom_frame)
Cell.mines_left_label_obj.place(x=20, y=10)

#Cell.pick_mines()

# to run the window
root.mainloop()