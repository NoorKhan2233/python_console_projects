# 🎮 Tic-Tac-Toe Game Variations

This repository contains three variations of the classic Tic-Tac-Toe game implemented in Python. Each variation offers a unique gameplay experience, from **human vs. human** to **AI vs. AI**. Below is a brief description of each project and instructions on how to run them.

---

## 🚀 Projects

### 1. **Player vs Player** (`tic_tac_toe_player_vs_player.py`)
A two-player version of Tic-Tac-Toe where two human players take turns to play on the same computer. Players input their moves by specifying the row and column indices of the grid.

#### Features:
- **3x3 Grid**: Players input moves as `row column` (e.g., `0 0` for the top-left corner).
- **Win/Draw Detection**: The game detects when a player wins or if the game ends in a draw.
- **Input Validation**: Ensures players enter valid moves.


python tic_tac_toe_player_vs_player.py
2. Player vs Computer (tic_tac_toe_player_vs_my_computer.py)
A single-player version where a human player competes against a simple AI. The player can choose to go first or second.

Features:
AI Logic: The computer tries to win, block the player, or make a random move if no winning or blocking move is available.

Player Choice: The player can choose to go first (X) or second (O).

Win/Draw Detection: The game detects when the player or computer wins or if the game ends in a draw.


python tic_tac_toe_player_vs_my_computer.py
3. Computer vs ChatGPT Computer (tic_tac_toe_my_computer_vs_chatgpt_computer.py)
An AI vs. AI version where two computers compete against each other. One computer uses a simple logic, while the other uses a more advanced strategy (simulated as "ChatGPT Computer").

Features:
Advanced AI Logic: The "ChatGPT Computer" uses a more strategic approach to win or block the opponent.

Turn Choice: You can choose which computer goes first.

Win/Draw Detection: The game detects when one of the computers wins or if the game ends in a draw.


python tic_tac_toe_my_computer_vs_chatgpt_computer.py
how to use:
git clone https://github.com/NoorKhan2233/python_console_projects.git
cd python_console_projects/ti_tac_toe_variation
Run the Desired Game:

Navigate to the ti_tac_toe_variation folder.

Run the desired Python script:


python tic_tac_toe_player_vs_player.py
python tic_tac_toe_player_vs_my_computer.py
python tic_tac_toe_my_computer_vs_chatgpt_computer.py
Follow On-Screen Instructions:

Each game will prompt you for input or display the moves made by the computers.

📋 Requirements
Python 3.x: Ensure you have Python installed on your system.

NumPy: Install NumPy using pip if not already installed:

pip install numpy
🗂️ Code Structure
File Name	Description
tic_tac_toe_player_vs_player.py	Two-player Tic-Tac-Toe.
tic_tac_toe_player_vs_my_computer.py	Player vs. Computer Tic-Tac-Toe.
tic_tac_toe_my_computer_vs_chatgpt_computer.py	Computer vs. Computer Tic-Tac-Toe.
🤝 Contributing
Feel free to contribute to this project! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.
## 📝 Note

### **Difference Between My Computer and ChatGPT Computer Algorithms**

- **My Computer**:
  - Uses a **probability-based algorithm** to choose the best move.
  - Assigns higher probabilities to strategic positions (e.g., the center of the grid) and lower probabilities to less strategic positions.
  - If no winning or blocking move is available, it uses a weighted random selection to choose the next move.


- **ChatGPT Computer**:
  - Uses a **rule-based algorithm** to prioritize winning moves, blocking the opponent, and selecting strategic positions.
  - Always tries to win or block the opponent before making a random move.
  - Does not use probability; instead, it follows a fixed set of rules to determine the best move.

The main difference lies in the **decision-making process**:
- **My Computer** relies on **probability** to make strategic moves, which makes it more dynamic and adaptable.
- **ChatGPT Computer** relies on **fixed rules**, which makes it predictable but less flexible.

## ⚠️ Disclaimer
chatgpt is not wrtite all the code , but its just make some changes in my original code (in chatgpt computer code) rest of the code is purly authrised by me.
