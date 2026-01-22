import tkinter as tk
from tkinter import messagebox
import math
from playsound import playsound
import threading

# ---------------- SETTINGS --------------

AI_ENABLED = True
dark_mode = False
# ----------------- GAME SETTINGS --------------

current_player = "X"
board = [""] * 9
score = {"X": 0, "O": 0}

# ---------------- SOUND ----------------

def play_sound(file):
    threading.Thread(target=playsound, args=(file,), daemon=True).start()

# ---------------- GAME LOGIC --------------

def check_winner(b):
    win_patterns = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a, b1, c in win_patterns:
        if b[a] == b[b1] == b[c] != "":
            return b[a]
    if "" not in b:
        return "Draw"
    return None

# --------------- AI (MINIMAX) ---------------

def minimax(b, is_max):
    winner = check_winner(b)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0
    
    if is_max:
        best = -math.inf
        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = ""
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = ""
        return best
    
def ai_move():
    best_score = -math.inf
    move =None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score_val = minimax(board, False)
            board[i] = ""
            if score_val > best_score:
                best_score = score_val
                move = i
    if move is not None:
        make_move(move)


# --------------- UI ACTIONS ----------------------

def make_move(index):
    global current_player

    if board[index] != "":
        return
    
    board[index] = current_player
    buttons[index].config(text=current_player)
    play_sound("click.wav")

    winner = check_winner(board)
    if winner:
        handle_game_end(winner)
        return
    
    current_player = "O" if current_player == "X" else "X"

    if AI_ENABLED and current_player == "O":
        root.after(300, ai_move)

def handle_game_end(winner):
    if winner != "Draw":
        score[winner] += 1
        play_sound("win.wav")
        messagebox.showinfo("Game Over", f"{winner} wins!")
    else:
        messagebox.showinfo("Game Over", "It's a draw!")

    update_score()
    reset_board()

def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="")

def update_score():
    score_label.config(
        text=f"X: {score['X']}  O: {score['O']}"
    )


# --------------- DARK MODE ---------------

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode

    bg = "#1e1e1e" if dark_mode else "white"
    fg = "white" if dark_mode else "black"
    btn_bg = "#333333" if dark_mode else "SystemButtonFace"

    root.configure(bg=bg)
    score_label.config(bg=bg, fg=fg)

    for btn in buttons:
        btn.configure(bg=btn_bg, fg=fg)


# ----------------- GUI -------------------


root = tk.Tk()
root.title("Ultimate Tic Tac Toe")
root.geometry("300x420")
root.resizable(False, False)

score_label = tk.Label(root, text="X: 0  O: 0", font=("Arial", 14))
score_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

buttons = []
for i in range(9):
    btn = tk.Button(
        frame,
        text="",
        font=("Arial", 24),
        width=4,
        height=2,
        command=lambda i=i: make_move(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

controls = tk.Frame(root)
controls.pack(pady=10)

tk.Button(controls, text="Reset", width=10, command=reset_board).pack(side="left", padx=5)
tk.Button(controls, text="Dark Mode", width=10, command=toggle_dark_mode).pack(side="left", padx=5)

root.mainloop()
