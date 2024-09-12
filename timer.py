from tkinter import Label
import time

class Timer:
    def __init__(self, root, label):
        self.root = root
        self.label = label
        # initialize timer variables
        self.elapsed_time = 0
        self.running = False
    
    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"⏱: {minutes:02}:{seconds:02}"
    
    def update_timer(self):
        if self.running:
            self.elapsed_time += 1
            self.label.config(text=self.format_time(self.elapsed_time))
            self.root.after(1000, self.update_timer)
    
    def start(self):
        self.running = True
        self.start_time = time.time()
        self.update_timer()
    
    def stop(self):
        self.running = False

    def get_game_time(self):
        return self.format_time(self.elapsed_time)
        