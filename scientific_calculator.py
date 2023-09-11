import customtkinter as ctk

def button_callback():
    print(f"button pressed")

app = ctk.CTk()
app.title("Scientific Calculator")
app.geometry("400x600") # width by height

# 0th row
button_sin = ctk.CTkButton(app, text="sin", height=40, width=80,
                          command=button_callback).grid(row=0, column=0)
button_cos = ctk.CTkButton(app, text="cos", height=40, width=80,
                          command=button_callback).grid(row=0,column=1)
button_tan = ctk.CTkButton(app, text="tan", height=40, width=80,
                          command=button_callback).grid(row=0, column=2)
button_ln = ctk.CTkButton(app, text="ln", height=40, width=80,
                          command=button_callback).grid(row=0, column=3)
button_log10 = ctk.CTkButton(app, text="log\u2081\u2080", height=40, width=80,
                          command=button_callback).grid(row=0, column=4)

# 1st row 
button_eulerexp = ctk.CTkButton(app, text="e\u02b8", height=40, width=80,
                          command=button_callback).grid(row=1, column=0)
button_square = ctk.CTkButton(app, text="x\u00B2", height=40, width=80,
                          command=button_callback).grid(row=1,column=1)
button_cube = ctk.CTkButton(app, text="x\u00B3", height=40, width=80,
                          command=button_callback).grid(row=1, column=2)
button_sqrroot = ctk.CTkButton(app, text="\u221A", height=40, width=80,
                          command=button_callback).grid(row=1, column=3)
button_cuberoot = ctk.CTkButton(app, text="\u221B", height=40, width=80,
                          command=button_callback).grid(row=1, column=4)

# 2nd row
button_inverse = ctk.CTkButton(app, text="1/x", height=40, width=80,
                          command=button_callback).grid(row=2, column=0)
button_xpowery = ctk.CTkButton(app, text="x\u02b8", height=40, width=80,
                          command=button_callback).grid(row=2,column=1)
button_permu = ctk.CTkButton(app, text="nPr", height=40, width=80,
                          command=button_callback).grid(row=2, column=2)
button_combi = ctk.CTkButton(app, text="nCr", height=40, width=80,
                          command=button_callback).grid(row=2, column=3)
button_nfact = ctk.CTkButton(app, text="n!", height=40, width=80,
                          command=button_callback).grid(row=2, column=4)


# 3rd row
button_eulernum = ctk.CTkButton(app, text="e", height=40, width=80,
                          command=button_callback).grid(row=3, column=0)
button_pinum = ctk.CTkButton(app, text="\u03C0", height=40, width=80,
                          command=button_callback).grid(row=3,column=1)
button_modulo = ctk.CTkButton(app, text="%", height=40, width=80,
                          command=button_callback).grid(row=3, column=2)
button_leftbrace = ctk.CTkButton(app, text="(", height=40, width=80,
                          command=button_callback).grid(row=3, column=3)
button_rightbrace = ctk.CTkButton(app, text=")", height=40, width=80,
                          command=button_callback).grid(row=3, column=4)

# 4th row
button_7 = ctk.CTkButton(app, text="7", height=60, width=80,
                          command=button_callback).grid(row=4, column=0)
button_8 = ctk.CTkButton(app, text="8", height=60, width=80,
                          command=button_callback).grid(row=4,column=1)
button_9 = ctk.CTkButton(app, text="9", height=60, width=80,
                          command=button_callback).grid(row=4, column=2)
button_del = ctk.CTkButton(app, text="DEL", height=60, width=80,
                          command=button_callback).grid(row=4, column=3)
button_ac = ctk.CTkButton(app, text="AC", height=60, width=80,
                          command=button_callback).grid(row=4, column=4)

# 5th row
button_4 = ctk.CTkButton(app, text="4", height=60, width=80,
                          command=button_callback).grid(row=5, column=0)
button_5 = ctk.CTkButton(app, text="5", height=60, width=80,
                          command=button_callback).grid(row=5,column=1)
button_6 = ctk.CTkButton(app, text="6", height=60, width=80,
                          command=button_callback).grid(row=5, column=2)
button_mul = ctk.CTkButton(app, text="\u00D7", height=60, width=80,
                          command=button_callback).grid(row=5, column=3)
button_div = ctk.CTkButton(app, text="\u00F7", height=60, width=80,
                          command=button_callback).grid(row=5, column=4)

# 6th row 
button_1 = ctk.CTkButton(app, text="1", height=60, width=80,
                          command=button_callback).grid(row=6, column=0)
button_2 = ctk.CTkButton(app, text="2", height=60, width=80,
                          command=button_callback).grid(row=6,column=1)
button_3 = ctk.CTkButton(app, text="3", height=60, width=80,
                          command=button_callback).grid(row=6, column=2)
button_add = ctk.CTkButton(app, text="+", height=60, width=80,
                          command=button_callback).grid(row=6, column=3)
button_sub = ctk.CTkButton(app, text="-", height=60, width=80,
                          command=button_callback).grid(row=6, column=4)

# 7th row
button_0 = ctk.CTkButton(app, text="0", height=60, width=80,
                          command=button_callback).grid(row=7, column=0)
button_plus_minus = ctk.CTkButton(app, text="+/-", height=60, width=80,
                          command=button_callback).grid(row=7,column=1)
button_point = ctk.CTkButton(app, text=".", height=60, width=80,
                          command=button_callback).grid(row=7, column=2)
button_exp = ctk.CTkButton(app, text="EXP", height=60, width=80,
                          command=button_callback).grid(row=7, column=3)
button_equals = ctk.CTkButton(app, text="=", height=60, width=80,
                          command=button_callback).grid(row=7, column=4)


# app.grid_columnconfigure(0, weight=1)

# TODO1 create the buttons


app.mainloop()