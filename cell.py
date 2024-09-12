from tkinter import Button, Label
import random
import settings as st
import gameover
from timer_manager import get_timer

class Cell:
    first_click = True
    all_cells = []
    mines = []
    cells_opened = 0
    mines_left = st.MINE_COUNT
    mines_left_label_obj = None
    def __init__(self, root, x, y, is_mine=False):
        self.root = root
        self.is_first = False # to check if first clicked cell
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.is_opened = False
        self.is_flag = False
        self.x = x
        self.y = y

        # append the object to all_cells list
        Cell.all_cells.append(self)
    
    def create_btn_obj(self, location):
        btn = Button(location, width=7, height=3)
        btn.bind('<Button-1>', self.left_click) #left-click
        btn.bind('<Button-3>', self.right_click) #right-click
        self.cell_btn_obj = btn

    def left_click(self, event):
        if self.is_flag: # no action if flag
            pass
        elif self.is_mine:
            self.show_mine()
            get_timer().stop()
            gameover.game_end(self.root, 'lost')
            self.show_all_mines()
        else:
            if Cell.first_click:
                self.is_first = True
                mine_candidates = []
                # selecting mine_candidates by avoiding first-clicked cell and its adjacents
                for cell in Cell.all_cells:
                    if not cell.is_first and cell not in self.adjacent_cells:
                        mine_candidates.append(cell)
                Cell.pick_mines(mine_candidates)
                get_timer().start()
                Cell.first_click = False
            self.show_cell()

    def show_cell(self):
        # set cell as opened
        self.is_opened = True
        Cell.cells_opened += 1
        # change color to indicate cell opened
        self.cell_btn_obj.configure(bg="#c0c0c0")
        # all opened cell should be unflagged if flagged
        self.is_flag = False
        # cancel mouse click events for opened cells
        self.cell_btn_obj.unbind('<Button-1>')
        self.cell_btn_obj.unbind('<Button-3>')

        # show adjacent_mines_count in different colors
        match self.adjacent_mines_count:
            case 0:
                # to reveal adjacent cells of '0' cells
                for cell in self.adjacent_cells:
                    if not cell.is_opened:
                        cell.show_cell()
            case 1:
                self.cell_btn_obj.configure(text=self.adjacent_mines_count, fg="blue", font=["", 9])
            case 2:
                self.cell_btn_obj.configure(text=self.adjacent_mines_count, fg="green", font=["", 9])
            case 3:
                self.cell_btn_obj.configure(text=self.adjacent_mines_count, fg="red", font=["", 9])
            case 4:
                self.cell_btn_obj.configure(text=self.adjacent_mines_count, fg="indigo", font=["", 9])
            case _:
                self.cell_btn_obj.configure(text=self.adjacent_mines_count, font=["", 9])

        # check if game won
        if Cell.cells_opened == (st.CELL_COUNT - st.MINE_COUNT):
            get_timer().stop()
            gameover.game_end(self.root, 'won')

    @property
    def adjacent_cells(self):
        cells = [                                   # Grid format:
            self.get_cell(self.x-1, self.y-1),      # (x-1,y-1)  (x,y-1)  (x+1,y-1)
            self.get_cell(self.x-1, self.y),        # (x-1,y)    (x,y)    (x+1,y)
            self.get_cell(self.x-1, self.y+1),      # (x-1,y+1)  (x,y+1)  (x+1,y+1)
            self.get_cell(self.x, self.y-1),
            self.get_cell(self.x, self.y+1),
            self.get_cell(self.x+1, self.y-1),
            self.get_cell(self.x+1, self.y),
            self.get_cell(self.x+1, self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells    
    
    @property
    def adjacent_mines_count(self):
        count = 0
        for cell in self.adjacent_cells:
            if cell.is_mine:
                count += 1
        return count

    def get_cell(self, x, y):
        for cell in Cell.all_cells:
            if cell.x == x and cell.y == y:
                return cell

    def show_mine(self):
        self.cell_btn_obj.configure(bg='red')
    
    def right_click(self, event):
        if not self.is_flag:
            self.cell_btn_obj.configure(bg='#FFD700')
            self.is_flag = True
            # updating mines_left label
            Cell.mines_left -= 1
            Cell.mines_left_label_obj.configure(text=f"🚩: {Cell.mines_left}")
        else:
            self.cell_btn_obj.configure(bg='SystemButtonFace')
            self.is_flag = False
            # updating mines_left label
            Cell.mines_left += 1
            Cell.mines_left_label_obj.configure(text=f"🚩: {Cell.mines_left}")

    def show_all_mines(self):
        for mine in Cell.mines: # to show all mines
            mine.show_mine()
        for cell in Cell.all_cells: # to show wrongly flagged cells
            if cell.is_flag and cell not in Cell.mines:
                cell.cell_btn_obj.configure(text="X")

    @staticmethod
    def pick_mines(mine_candidates):
        mines = random.sample(mine_candidates, st.MINE_COUNT)
        Cell.mines = mines
        for mine in mines:
            mine.is_mine = True

    @staticmethod
    def mines_left_label(location):
        lbl = Label(location, text=f"🚩: {Cell.mines_left}", bg='black', fg='green', font=["MS Sans Serif", 24, "bold"])
        Cell.mines_left_label_obj = lbl
    
    # naming each cell object
    def __repr__(self):
        return f"Cell({self.x},{self.y})"