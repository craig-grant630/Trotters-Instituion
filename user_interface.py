import tkinter as tk
from tkinter import ttk
from application import StudyBuddyApp

# Styling references
# https://www.pythontutorial.net/tkinter/ttk-style/
# https://tkdocs.com/tutorial/widgets.html
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry.html
# https://ttkbootstrap.readthedocs.io/en/version-0.5/widgets/combobox.html
# https://tkdocs.com/tutorial/customstyles.html
# https://stackoverflow.com/questions/68883001/how-to-make-tkinter-combobox-dark-themed
# Colours, fonts for UI
#====================================================================================================
BG_COLOUR = "#1a1a2e"
BG_COLOUR2 = "#16213e"
BG_COLOUR3 = "#0f3460"

BORDER = "#0f3460"
ENTRY_BG="#0d2137"
FG_COLOUR = "#eaeaea"
FG_COLOUR2 = "#a0a0b0"

ACCENT = "#e94560"

FONT_BODY = ("Helvetica", 12)
FONT_HEADER = ("Helvetica", 20, "bold")
FONT_SMALL = ("Helvetica", 10)
FONT_BUTTON= ("Helvetica", 12, "bold")
#=================================================================================================================
#Stlyed Widgets

def card(parent, padx=10, pady=14, bg=BG_COLOUR2):
    frame = tk.Frame(parent, bg=bg, padx=padx, pady=pady,
                     highlightthickness=1, highlightbackground=BORDER)
    return frame

def styled_label(parent, text, font=FONT_BODY, fg=FG_COLOUR, bg=BG_COLOUR2, **kwargs):
    return tk.Label(parent, text=text, font=font,
                    fg=fg, bg=bg, **kwargs)

def styled_combobox(parent, options, width, **kwargs):

    parent.option_add("*TCombobox*Listbox.background", BG_COLOUR3)
    parent.option_add('*TCombobox*Listbox.foreground', 'white')
    parent.option_add('*TCombobox*Listbox.selectBackground', ACCENT)
    parent.option_add('*TCombobox*Listbox.font', FONT_BODY)

    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Dark.TCombobox", background=BG_COLOUR3, font=FONT_BODY,
                    fieldbackground=ENTRY_BG, foreground=FG_COLOUR,arrowcolor=ACCENT,
                    bordercolor=BORDER, lightcolor="white", darkcolor="white")
    style.map("Dark.TCombobox", fieldbackground=[("readonly",BG_COLOUR3), ("focus", BG_COLOUR3), ("pressed",BG_COLOUR3)], foreground=[("readonly",FG_COLOUR)],
              selectbackground=[("readonly",BG_COLOUR3), ("pressed",BG_COLOUR3)], selectforeground=[("readonly","white")])

    combobox = ttk.Combobox(parent, state="readonly", values=options, width=width, style="Dark.TCombobox", font=FONT_BODY, **kwargs)
    return combobox

def separator(parent, bg=BORDER):
    return tk.Frame(parent, bg=bg, height=1)
#============================================================================================================

class StudyBuddyUI:

    def __init__(self):
        self.app = StudyBuddyApp()

        self.root = tk.Tk()
        self.root.title("TiT Study Buddy")
        self.root.geometry("700x700")
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

    def show_register(self):
        self.clear()
        RegisterFrame(self.container, self)

# =====================================================================================
class WelcomeHeader(tk.Frame):
    def __init__(self, parent, ui):
        #create instance of the login frame:
        super().__init__(parent, bg=BG_COLOUR2)
        self.pack(fill="both")
        self.ui = ui

        styled_label(self, "Welcome to TiT Study Buddy", font=FONT_HEADER, fg=ACCENT, bg=BG_COLOUR2).pack(pady=(0,4))
        styled_label(self, "Trotters Independent Tuition - Peckham, South East London", font=FONT_SMALL,
                     fg=FG_COLOUR2, bg=BG_COLOUR2).pack(pady=(0,10))
        separator(self).pack(fill="x", pady=10)


#==============================================================================================

class LoginFrame(tk.Frame):
    def __init__(self, parent, ui):
        # create instance of the login frame:
        super().__init__(parent, bg=BG_COLOUR)
        self.pack(fill="both", expand=True)
        self.ui = ui

        outer = tk.Frame(self, bg=BG_COLOUR2,padx=40, pady=36)
        outer.place(relx=0.5, rely=0.5, anchor="center")

        WelcomeHeader(outer, ui)

        row = tk.Frame(outer, bg=BG_COLOUR2)
        row.pack(pady=10)
        login_frame_btn = tk.Button(row, text="Login", bg=ACCENT, fg="white", font=FONT_BUTTON, relief="flat",
                                    borderwidth=1, width=20, command=ui.show_login)
        login_frame_btn.grid(row=0, column=0)

        register_frame_btn = tk.Button(row, text="Register", bg=BG_COLOUR, fg="white", font=FONT_BUTTON, relief="flat",
                                       borderwidth=1, width=20, command=ui.show_register)
        register_frame_btn.grid(row=0, column=1)

        row2 = tk.Frame(outer, bg=BG_COLOUR2)
        row2.pack(pady=5)

        styled_label(row2, "Student ID (10 digits)", bg=BG_COLOUR2, font=FONT_BODY,
                     fg=FG_COLOUR2).grid(row=0, column=0, sticky="w", padx=8, pady=8)

        self.login_id = tk.Entry(row2, bg=BG_COLOUR3,fg="white", relief="flat", font=FONT_BODY, width=40, highlightcolor=ACCENT, highlightthickness=1, insertbackground='white')
        self.login_id.grid(row=1, column=0, sticky="w", padx=8)

        styled_label(row2, "Password", bg=BG_COLOUR2, fg=FG_COLOUR2,
                     font=FONT_BODY).grid(row=2, column=0, sticky="w", padx=8, pady=8)
        self.login_pwd = tk.Entry(row2, bg=BG_COLOUR3, fg="white", relief="flat", font=FONT_BODY, width=40, show="*",
                                  highlightcolor=ACCENT, highlightthickness=1, insertbackground='white')
        self.login_pwd.grid(row=3, column=0, sticky="w", padx=8)

        tk.Button(outer, text="Login >>", bg=BG_COLOUR2, fg="white", font=FONT_BUTTON, relief="flat",
                  borderwidth=1).pack(pady=15)

class RegisterFrame(tk.Frame):
    def __init__(self, parent, ui):
        super().__init__(parent, bg=BG_COLOUR)
        self.pack(fill="both", expand=True)
        self.ui = ui

        outer = tk.Frame(self, bg=BG_COLOUR2, padx=40, pady=20)
        outer.place(relx=0.5, rely=0.5, anchor="center")

        WelcomeHeader(outer, ui)

        row = tk.Frame(outer, bg=BG_COLOUR2)
        row.pack(pady=10)
        login_frame_btn = tk.Button(row, text="Login", bg=BG_COLOUR, fg="white", font=FONT_BUTTON, relief="flat",
                                    borderwidth=1, width=20, command=ui.show_login)
        login_frame_btn.grid(row=0, column=0)
        register_frame_btn = tk.Button(row, text="Register", bg=ACCENT, fg="white", font=FONT_BUTTON, relief="flat",
                                       borderwidth=1, width=20, command=ui.show_register)
        register_frame_btn.grid(row=0, column=1)

        fields = [
            ("Student ID (10 digits)", False),
            ("Full Name", False),
            ("Password", True),
            ("Confirm Password", True),
        ]
        self.entries = {}
        for label, show in fields:
            row2 = tk.Frame(outer, bg=BG_COLOUR2)
            row2.pack(fill="x")
            row2.grid_columnconfigure(0, minsize=180, uniform="reg_col")
            styled_label(row2, label, bg=BG_COLOUR2, font=FONT_BODY,
                         fg=FG_COLOUR2).grid(row=0, column=0, sticky="e", padx=8, pady=5)
            if show:
                entry = tk.Entry(row2, bg=BG_COLOUR3, fg="white", relief="flat", font=FONT_BODY, width=27, show="*",
                                 highlightcolor=ACCENT, highlightthickness=1)
            else:
                entry = tk.Entry(row2, bg=BG_COLOUR3, fg="white", relief="flat", font=FONT_BODY, width=27,
                                 highlightcolor=ACCENT, highlightthickness=1)

            self.entries[label] = entry
            entry.grid(row=0, column=1, sticky="w", padx=8)

        separator(outer).pack(fill="x", pady=10)
        row2 = tk.Frame(outer, bg=BG_COLOUR2)
        row2.pack(fill="x")
        row2.grid_columnconfigure(0, minsize=180, uniform="reg_col")

        styled_label(row2, "Year of Study:", bg=BG_COLOUR2, font=FONT_BODY,
                                 fg=FG_COLOUR2).grid(row=2, column=0, sticky="e", padx=6)
        self.yos = styled_combobox(row2, ["  1","  2","  3"], 3)
        self.yos.grid(row=2, column=1, sticky="w", padx=6, pady=5)

        prog_options = []
        for p in self.ui.app.programmes:
            prog_options.append(f"{p["programme_code"]} - {p["name"]}")
        styled_label(row2, "Programme:", bg=BG_COLOUR2, font=FONT_BODY,
                     fg=FG_COLOUR2).grid(row=0, column=0, sticky="e", padx=6)
        self.programme_drop = styled_combobox(row2, prog_options, 26)
        self.programme_drop.grid(row=0, column=1, sticky="w", padx=6, pady=5)

        camp_options = []
        for p in self.ui.app.campuses:
            camp_options.append(f"{p["name"]} - {p["campus_code"]}")
        styled_label(row2, "Campus:", bg=BG_COLOUR2, font=FONT_BODY,
                     fg=FG_COLOUR2).grid(row=1, column=0, sticky="e", padx=6)
        self.campus_drop = styled_combobox(row2, camp_options, 26)
        self.campus_drop.grid(row=1, column=1, sticky="w", padx=6, pady=5)

        register_frame_btn = tk.Button(row2, text="Register >>", bg=BG_COLOUR3, fg="white", font=FONT_BUTTON, relief="flat",
                                    borderwidth=1, width=15, command=ui.show_login)
        register_frame_btn.grid(row=3, column=1, sticky="e", pady=(40,5), padx = 10)

    def register(self):
        sid = self.entries["Student ID (10 digits)"].get()
        name = self.entries["Full Name"].get()
        password = self.entries["Password"].get()
        con_password = self.entries["Confirm Password"].get()
        pass

if __name__=="__main__":
    StudyBuddyUI()