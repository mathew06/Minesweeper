from tkinter import Toplevel, Label, Button
from timer_manager import get_timer
import settings as st

def game_end(root, status):
    # create new top-level window
    game_end_window = Toplevel(root)
    game_end_window.resizable(False, False)
    width = 300
    height = 200
    game_end_window.geometry(f'{width}x{height}')

    # get dimensions of root window
    root_width = st.WIDTH
    root_height = st.HEIGHT
    
    # get position of root window on the screen
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    
    # calculation to center game_end_window
    x = root_x + (root_width - width) // 2
    y = root_y + (root_height - height) // 2
    
    # position the game_end_window
    game_end_window.geometry(f"{width}x{height}+{x}+{y}")

    if status == 'lost':
        game_end_window.title('Game Over')
        # label with game over message
        message = Label(game_end_window, text="Game Over!\nYou Lost", fg='red', font=("MS Sans Serif", 24))
        message.pack(pady=20)
        # button to close the window
        button = Button(game_end_window, text="OK", width=7, height=2, bg='white', fg='red', font=("MS Sans Serif", 12), command=lambda: [game_end_window.destroy(), root.quit()])
        button.pack(pady=10)
    else:
        game_end_window.title('Game Won')
        game_time = get_timer().get_game_time()
        message = Label(game_end_window, text=f"CONGRATULATIONS!\nYou Won!\n{game_time}", fg='green', font=("", 20))
        message.pack(pady=20)
        button = Button(game_end_window, text="OK", width=7, height=2, bg='white', fg='green', font=("", 12), command=lambda: [game_end_window.destroy(), root.quit()])
        button.pack(pady=10)

    # disable root window while game_end_window is open
    root.attributes("-disabled", True)