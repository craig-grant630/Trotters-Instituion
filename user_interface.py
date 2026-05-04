import tkinter as tk
from tkinter import ttk


# https://www.pythontutorial.net/tkinter/ttk-style/
# Colours, fonts for UI
#====================================================================================================
BG_COLOUR = "#1a1a2e"
BG_COLOUR2 = "#16213e"
BG_COLOUR3 = "#0f3460"

BORDER = "#0f3460"

FG_COLOUR = "#eaeaea"
FG_COLOUR2 = "#a0a0b0"

ACCENT = "#e94560"

FONT_BODY = ("Helvetica", 11)
FONT_HEADER = ("Helvetica", 20, "bold")
FONT_SMALL = ("Helvetica", 9)
#=================================================================================================================
#Stlyed Widgets

def card(parent, padx=10, pady=14, bg=BG_COLOUR2):
    frame = tk.Frame(parent, bg=bg, padx=padx, pady=pady,
                     highlightthickness=1, highlightbackground=BORDER)
    return frame

def styled_label(parent, text, font=FONT_BODY, fg=FG_COLOUR, bg=BG_COLOUR2, **kwargs):
    return tk.Label(parent, text=text, font=font,
                    fg=fg, bg=bg, **kwargs)

def separator(parent, bg=BORDER):
    return tk.Frame(parent, bg=bg, height=1)
#============================================================================================================

class StudyBuddyUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TiT Study Buddy")
        self.root.geometry("600x600")
        self.root.configure(bg=BG_COLOUR)
        self.root.resizable(width=True, height=True)

        self.container = tk.Frame(self.root, bg=BG_COLOUR)
        self.container.pack(fill="both", expand=True)

        self.show_login()
        self.root.mainloop()

    def clear(self):
        for w in self.container.winfo_children():
            w.destroy()

    def show_login(self):
        self.clear()
        LoginFrame(self.container, self)

class LoginFrame(tk.Frame):
    def __init__(self, parent, ui):
        #create instance of the login frame:
        super().__init__(parent, bg=BG_COLOUR)
        self.pack(fill="both", expand=True)
        self.ui = ui

        outer = tk.Frame(self, bg=BG_COLOUR)
        outer.place(relx=0.5, rely=0.5, anchor="center")

        c = card(outer, padx=40, pady=36, bg=BG_COLOUR2)
        c.pack()

        styled_label(c, "Welcome to TiT Study Buddy", font=FONT_HEADER, fg=ACCENT, bg=BG_COLOUR2).pack(pady=(0,4))
        styled_label(c, "Trotters Independent Tuition - Peckham, South East London", font=FONT_SMALL,
                     fg=FG_COLOUR2, bg=BG_COLOUR2).pack(pady=(0,20))
        separator(c).pack(fill="x", pady=8)


        nb = ttk.Notebook(c)
        nb.pack(fill="both", expand=True)

        style = ttk.Style()
        style.theme_use('clam')

        style.configure("TNotebook",
                        background=BG_COLOUR2,
                        borderwidth=0,
                        lightcolor=BG_COLOUR2,
                        darkcolor=BG_COLOUR2,
                        bordercolor=BG_COLOUR2)

        style.configure("TNotebook.Tab",
                        background=BG_COLOUR,
                        foreground=FG_COLOUR,
                        padding=[15, 8],
                        font=FONT_BODY,
                        borderwidth=0,
                        lightcolor=BG_COLOUR,
                        bordercolor=BG_COLOUR2)

        style.map("TNotebook.Tab",
                  background=[("selected", BG_COLOUR2), ("active", BG_COLOUR)],
                  lightcolor=[("selected", BG_COLOUR)],
                  bordercolor=[("selected", BG_COLOUR2)])

        login_tab = tk.Frame(nb, background=BG_COLOUR2, padx=16, pady=16, highlightthickness=0)
        reg_tab = tk.Frame(nb, background=BG_COLOUR2, padx=16, pady=16, highlightthickness=0)

        nb.add(login_tab, text="Login")
        nb.add(reg_tab, text="Register")


if __name__=="__main__":
    StudyBuddyUI()