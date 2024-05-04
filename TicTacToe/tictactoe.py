import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

def points():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    label_player1 = tk.Label(board_frame, text="player 1", font=("Aviny",16), padx=10)
    label_player2 = tk.Label(board_frame, text="player 2", font=("Aviny",16), padx=10)
    label_player1.grid(row=0, column=0)
    label_player2.grid(row=0, column=2)
    
    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    point_player1 = tk.Label(point_frame, text="0", padx=20, font=("Lalezar", 18))
    point_player2 = tk.Label(point_frame, text="0", padx=20, font=("Lalezar", 18))
    point_player1.grid(row=0, column=0)
    point_player2.grid(row=0, column=1)

def board():
    buttons = []
    counter = 0
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    for row in range(1, 4):
        for column in range(1, 4):
            index = counter
            buttons.append(index)
            buttons[index] = tk.Button(board_frame)
            buttons[index].config(width=10, height=4, font=("None", 18, "bold"))
            buttons[index].grid(row=row, column=column)
            counter += 1

points()
board()   

window.mainloop()