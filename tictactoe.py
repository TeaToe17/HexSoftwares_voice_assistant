import tkinter

def determine_winner():
    global turns, game_over
    turns += 1

    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]) and board[row][0]["text"] != "":
            label.config(text=board[row][0]["text"]+" is the winner!", fg=color_yellow)
            for column in range(3):
                board[row][column].config(fg=color_yellow,bg=light_gray)
            game_over = True
            return  
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]) and board[1][column]["text"] != "":
            label.config(text=board[1][column]["text"] + " is the winner!", fg=red)
            for row in range(3):
                board[row][column].config(fg=red,bg=light_gray)
            game_over = True
            return
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[1][1]["text"] != ""): #()
        label.config(text=board[1][1]["text"] + " is the winner!",fg=red,bg=light_gray)
        for cell in range(3):
            board[cell][cell].config(fg=red,bg=gray)
        game_over = True
        return 
    elif board[2][0]["text"] == board[1][1]["text"] ==board[0][2]["text"] and board[1][1]["text"]  != "":
        label.config(text=board[1][1]["text"] + " is the winner!",fg=color_yellow, bg=gray)
        for cell in range(3):
            board[2-cell][cell].config(fg=color_yellow,bg=gray)
        game_over = True
        return
    elif turns >= 9:
        label.config(text="Tie",fg=color_yellow, bg=gray)
        return

def play_turn(row,column):
    global current_player , game_over

    if game_over:
        return

    if board[row][column]["text"] != "":
        return
    board[row][column]["text"] = current_player    

    if current_player == playerO:
        current_player = playerX
    else:
        current_player = playerO

    label["text"] = current_player + "'s turn"
    determine_winner()

def new_game():
    global turns, game_over
    turns = 0
    game_over = False

    label.config(text=current_player + "'s turn", fg="white", bg=gray)

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", fg=red, bg=gray)

playerX = "X"
playerO = "O"
current_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

red = "#ff0000"
color_yellow = "#ffde57"
gray = "#343434"
light_gray = "#646464"

turns = 0
game_over = False

window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)

frame =tkinter.Frame(window)
label = tkinter.Label(frame,text=current_player + "'s turn",
                      font=("Consolas",20),bg=gray,fg="white")

label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas",50,"bold"),
                                            bg=gray, fg=red,
                                            width=4,height=1,
                                            command=lambda row=row, 
                                            column=column: play_turn(row,column) )
        board[row][column].grid(row=row+1,column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas",20),
                         bg=gray,fg="white", command=new_game) 
button.grid(row=4,column=0,columnspan=3,sticky="we")
frame.pack()

window.update()
window_height = window.winfo_height()
window_width = window.winfo_width()
screen_height = window.winfo_screenheight()
screen_width = window.winfo_screenwidth()

window_y = int((screen_height/2) - (window_height/2))
window_x = int((screen_width/2) - (window_width/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()