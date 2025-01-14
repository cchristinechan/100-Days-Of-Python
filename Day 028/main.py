from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    ticks_label.config(text="")
    start_button.config(state="normal", bg=GREEN)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    start_button.config(state="disabled", bg=PINK) # disables the start button to avoid multiple overlapping timers

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        ticks = ""
        for rep in range(math.floor(reps/2)):
            ticks += "✔"
        ticks_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # 224 instead of 223 = work with even numbers
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"),bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)
title_label.config(padx=10, pady=10)

ticks_label = Label(font=(FONT_NAME, 15, "normal"), bg=YELLOW, fg=GREEN)
ticks_label.grid(column=1, row=3)
ticks_label.config(padx=10, pady=10)

# highlight thickness manages the border
start_button = Button(text="Start", highlightthickness=0, command=start_timer, font=(FONT_NAME, 12, "bold"))
start_button.config(width=10, height=2, bg=GREEN, fg=YELLOW)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer, font=(FONT_NAME, 12, "bold"))
reset_button.config(width=10, height=2, bg=GREEN, fg=YELLOW)
reset_button.grid(column=2, row=2)

window.mainloop()
