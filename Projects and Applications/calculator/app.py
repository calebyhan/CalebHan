import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, master=None):
        self.master = master
        master.title("Calculator")
        master.geometry("500x614")

        self.ft = tkFont.Font(family='Times', size=10)

        self.text = ""
        self.text_box = tk.Label(self.master)

        self.widgets()

    def widgets(self):
        button_0 = tk.Button(self.master)
        button_0["bg"] = "#f0f0f0"
        button_0["font"] = self.ft
        button_0["fg"] = "#000000"
        button_0["justify"] = "center"
        button_0["text"] = "0"
        button_0.place(x=158, y=500, width=70, height=70)
        button_0["command"] = self.button_0_command

        button_1 = tk.Button(self.master)
        button_1["bg"] = "#f0f0f0"
        button_1["font"] = self.ft
        button_1["fg"] = "#000000"
        button_1["justify"] = "center"
        button_1["text"] = "1"
        button_1.place(x=44, y=386, width=70, height=70)
        button_1["command"] = self.button_1_command

        button_2 = tk.Button(self.master)
        button_2["bg"] = "#f0f0f0"
        button_2["font"] = self.ft
        button_2["fg"] = "#000000"
        button_2["justify"] = "center"
        button_2["text"] = "2"
        button_2.place(x=158, y=386, width=70, height=70)
        button_2["command"] = self.button_2_command

        button_3 = tk.Button(self.master)
        button_3["bg"] = "#f0f0f0"
        button_3["font"] = self.ft
        button_3["fg"] = "#000000"
        button_3["justify"] = "center"
        button_3["text"] = "3"
        button_3.place(x=272, y=386, width=70, height=70)
        button_3["command"] = self.button_3_command

        button_4 = tk.Button(self.master)
        button_4["bg"] = "#f0f0f0"
        button_4["font"] = self.ft
        button_4["fg"] = "#000000"
        button_4["justify"] = "center"
        button_4["text"] = "4"
        button_4.place(x=44, y=272, width=70, height=70)
        button_4["command"] = self.button_4_command

        button_5 = tk.Button(self.master)
        button_5["bg"] = "#f0f0f0"
        button_5["font"] = self.ft
        button_5["fg"] = "#000000"
        button_5["justify"] = "center"
        button_5["text"] = "5"
        button_5.place(x=158, y=272, width=70, height=70)
        button_5["command"] = self.button_5_command

        button_6 = tk.Button(self.master)
        button_6["bg"] = "#f0f0f0"
        button_6["font"] = self.ft
        button_6["fg"] = "#000000"
        button_6["justify"] = "center"
        button_6["text"] = "6"
        button_6.place(x=272, y=272, width=70, height=70)
        button_6["command"] = self.button_6_command

        button_7 = tk.Button(self.master)
        button_7["bg"] = "#f0f0f0"
        button_7["font"] = self.ft
        button_7["fg"] = "#000000"
        button_7["justify"] = "center"
        button_7["text"] = "7"
        button_7.place(x=44, y=158, width=70, height=70)
        button_7["command"] = self.button_7_command

        button_8 = tk.Button(self.master)
        button_8["bg"] = "#f0f0f0"
        button_8["font"] = self.ft
        button_8["fg"] = "#000000"
        button_8["justify"] = "center"
        button_8["text"] = "8"
        button_8.place(x=158, y=158, width=70, height=70)
        button_8["command"] = self.button_8_command

        button_9 = tk.Button(self.master)
        button_9["bg"] = "#f0f0f0"
        button_9["font"] = self.ft
        button_9["fg"] = "#000000"
        button_9["justify"] = "center"
        button_9["text"] = "9"
        button_9.place(x=272, y=158, width=70, height=70)
        button_9["command"] = self.button_9_command

        button_a = tk.Button(self.master)
        button_a["bg"] = "#f0f0f0"
        button_a["font"] = self.ft
        button_a["fg"] = "#000000"
        button_a["justify"] = "center"
        button_a["text"] = "+"
        button_a.place(x=386, y=500, width=70, height=70)
        button_a["command"] = self.button_a_command

        button_s = tk.Button(self.master)
        button_s["bg"] = "#f0f0f0"
        button_s["font"] = self.ft
        button_s["fg"] = "#000000"
        button_s["justify"] = "center"
        button_s["text"] = "-"
        button_s.place(x=386, y=386, width=70, height=70)
        button_s["command"] = self.button_s_command

        button_m = tk.Button(self.master)
        button_m["bg"] = "#f0f0f0"
        button_m["font"] = self.ft
        button_m["fg"] = "#000000"
        button_m["justify"] = "center"
        button_m["text"] = "*"
        button_m.place(x=386, y=272, width=70, height=70)
        button_m["command"] = self.button_m_command

        button_d = tk.Button(self.master)
        button_d["bg"] = "#f0f0f0"
        button_d["font"] = self.ft
        button_d["fg"] = "#000000"
        button_d["justify"] = "center"
        button_d["text"] = "/"
        button_d.place(x=386, y=158, width=70, height=70)
        button_d["command"] = self.button_d_command

        button_clear = tk.Button(self.master)
        button_clear["bg"] = "#f0f0f0"
        button_clear["font"] = self.ft
        button_clear["fg"] = "#000000"
        button_clear["justify"] = "center"
        button_clear["text"] = "C"
        button_clear.place(x=44, y=500, width=70, height=70)
        button_clear["command"] = self.button_clear_command

        button_dot = tk.Button(self.master)
        button_dot["bg"] = "#f0f0f0"
        button_dot["font"] = self.ft
        button_dot["fg"] = "#000000"
        button_dot["justify"] = "center"
        button_dot["text"] = "."
        button_dot.place(x=272, y=500, width=70, height=70)
        button_dot["command"] = self.button_dot_command

        button_equal = tk.Button(self.master)
        button_equal["bg"] = "#f0f0f0"
        button_equal["font"] = self.ft
        button_equal["fg"] = "#000000"
        button_equal["justify"] = "center"
        button_equal["text"] = "="
        button_equal.place(x=386, y=44, width=70, height=70)
        button_equal["command"] = self.button_equal_command

        self.text_box["bg"] = "#ffffff"
        self.text_box["font"] = self.ft
        self.text_box["fg"] = "#000000"
        self.text_box["justify"] = "center"
        self.text_box["text"] = self.text
        self.text_box.place(x=44, y=44, width=298, height=70)

    def evaluate(self):
        try:
            return eval(self.text)
        except:
            return "Error"

    def button_0_command(self):
        self.text += "0"
        self.text_box.configure(text=self.text)

    def button_1_command(self):
        self.text += "1"
        self.text_box.configure(text=self.text)

    def button_2_command(self):
        self.text += "2"
        self.text_box.configure(text=self.text)

    def button_3_command(self):
        self.text += "3"
        self.text_box.configure(text=self.text)

    def button_4_command(self):
        self.text += "4"
        self.text_box.configure(text=self.text)

    def button_5_command(self):
        self.text += "5"
        self.text_box.configure(text=self.text)

    def button_6_command(self):
        self.text += "6"
        self.text_box.configure(text=self.text)

    def button_7_command(self):
        self.text += "7"
        self.text_box.configure(text=self.text)

    def button_8_command(self):
        self.text += "8"
        self.text_box.configure(text=self.text)

    def button_9_command(self):
        self.text += "9"
        self.text_box.configure(text=self.text)

    def button_a_command(self):
        self.text += "+"
        self.text_box.configure(text=self.text)

    def button_s_command(self):
        self.text += "-"
        self.text_box.configure(text=self.text)

    def button_m_command(self):
        self.text += "*"
        self.text_box.configure(text=self.text)

    def button_d_command(self):
        self.text += "/"
        self.text_box.configure(text=self.text)

    def button_clear_command(self):
        self.text = ""
        self.text_box.configure(text=self.text)

    def button_dot_command(self):
        self.text += "."
        self.text_box.configure(text=self.text)

    def button_equal_command(self):
        self.text = self.evaluate()
        self.text_box.configure(text=self.text)
