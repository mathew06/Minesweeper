# Minesweeper Game

This is a simple Minesweeper game developed using Python and Tkinter.
The game consists of a grid with hidden mines, and the player must reveal cells without triggering any mines.

## Acknowledgments

This game was initially developed by following a YouTube tutorial. You can find the tutorial here: [YouTube Tutorial Link](https://www.youtube.com/watch?v=OqbGRZx4xUc). The tutorial helped build the basic structure of the Minesweeper game.

However, additional features and improvements have been made beyond the tutorial, including:
- **Safe First Click**: Ensured that the first click will never reveal a mine, enhancing the user experience.
- **Auto-Open Adjacent Cells**: Implemented a feature where clicking a cell with zero adjacent mines automatically opens surrounding cells, making gameplay smoother.
- **Timer Integration**: A custom timer that tracks game time and updates dynamically.
- **Game Over Handling**: A custom `gameover.py` script that gracefully handles game termination.
- **Additional Enhancements**: Improved user interface and extended functionality.
  
## File Structure

- `main.py`: The main entry point for the game, initializes the window and runs the game loop.
- `cell.py`: Manages the logic for individual cells in the Minesweeper grid.
- `gameover.py`: Handles the game's end conditions and displays messages for winning or losing.
- `timer.py`: Contains the `Timer` class responsible for handling the stopwatch functionality.
- `timer_manager.py`: Manages interactions between the game logic and the timer objects.
- `settings.py`: Defines game settings such as grid size, number of mines, and window dimensions.
- `utils.py`: Utility functions for calculating grid cell dimensions based on window size.

## Getting Started

These instructions will help you set up the project locally on your machine.

### Prerequisites

- Python 3.x
- Tkinter (included with most Python distributions)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mathew06/Minesweeper.git
2. Navigate to the project directory:
   ```bash
   cd Minesweeper
3. Run the game:
   ```bash
   python main.py

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request or open an issue.
