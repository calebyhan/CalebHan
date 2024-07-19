import tkinter as tk
import random

BUTTON_SIZE = 50

root = tk.Tk()
root.title("Memory Game")
root.geometry(f"{210}x{210}")

buttons = []

sequence = []
current = [0, []]
start = True
itr = 0

def reset(button, color):
    button.config(bg=color)

def button_click(i, j):
    global current
    global sequence
    global start
    global itr
    if not start:
        current[0] += 1
        current[1].append(j * 4 + i)
    if start:
        n = random.randint(0, 15)
        sequence.append(n)
        x = n % 4
        y = n // 4
        button = buttons[x][y]
        original_color = button.cget("bg")
        button.config(bg="green")
        root.update()
        button.after(100, lambda b=button, c=original_color: reset(b, c))
        itr = len(sequence)
        current = [0, []]
        start = False
    else:
        if itr == 1:
            if current[1] == sequence:
                n = random.randint(0, 15)
                sequence.append(n)
                for b in sequence:
                    x = b % 4
                    y = b // 4
                    button = buttons[x][y]
                    original_color = button.cget("bg")
                    button.config(bg="green")
                    root.update()
                    button.after(100, lambda b=button, c=original_color: reset(b, c))
                    root.after(100)
            else:
                root.quit()
            itr = len(sequence)
            current = [0, []]
        else:
            itr -= 1

for i in range(4):
    row = []
    for j in range(4):
        x = i * BUTTON_SIZE
        y = j * BUTTON_SIZE
        button = tk.Button(root, width=BUTTON_SIZE, height=BUTTON_SIZE, command=lambda i=i, j=j: button_click(i, j))
        button.place(x=x, y=y)
        row.append(button)
    buttons.append(row)

root.mainloop()
