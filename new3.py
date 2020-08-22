# region Imports

from tkinter import *
from tkinter import ttk

# endregion



# region Color Used

color1 = '#252526'
color2 = '#3c3c3c'
color3 = '#1e1e1e'
color4 = '#cccccc'
color5 = '#333333'
color6 = '#2A2D2E'

# endregion



# region Main Window Settings

win = Tk()
win.overrideredirect(1)
win.config(bg=color3)
win.config(highlightbackground=color2)
win.geometry("1366x728+0+0")
win.title("Calculator")
win.iconbitmap("wd.ico")

# endregion




# region Title Bar Frame

title_bar = Frame(win, width=1366, height=29, bg=color2)
title_bar.place(x=0, y=0)

# endregion F



# region Drag Window

lastClickX = 0
lastClickY = 0


def savelastclickpos(event):

    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def dragging(event):

    x, y = event.x - lastClickX + win.winfo_x(), event.y - lastClickY + win.winfo_y()
    win.geometry("+%s+%s" % (x, y))


win.attributes('-topmost', True)
title_bar.bind('<Button-1>', savelastclickpos)
title_bar.bind('<B1-Motion>', dragging)

# endregion


# region Buttons Images Imports

photo1 = PhotoImage(file='close.png')
photo2 = PhotoImage(file='close_mouse.png')
photo3 = PhotoImage(file='minimize.png')
photo4 = PhotoImage(file='minimize_mouse.png')
photo5 = PhotoImage(file='restore.png')
photo6 = PhotoImage(file='restore_mouse.png')
photo7 = PhotoImage(file='maximize.png')
photo8 = PhotoImage(file='maximize_mouse.png')
photo10 = PhotoImage(file='all.png')
photo11 = PhotoImage(file='all_mouse.png')
photo12 = PhotoImage(file='search.png')
photo13 = PhotoImage(file='search_mouse.png')
photo14 = PhotoImage(file='setting.png')
photo15 = PhotoImage(file='setting_mouse.png')

# endregion



# region Close Button


def close_h(e):
    close_button.config(image=photo2)


def close_l(e):
    close_button.config(image=photo1)


close_button = Button(title_bar, image=photo1, bd=0, bg=color2, activebackground=color2, command=win.destroy)
close_button.place(x=1320, y=0)
close_button.bind("<Enter>", close_h)
close_button.bind("<Leave>", close_l)

# endregion



# region Maximize Button


def maximize():
    win.geometry("1366x728+0+0")
    title_bar.config(width=1366)
    maximize_button.place_forget()
    close_button.place(x=1320, y=0)
    minimize_button.place(x=1228, y=0)
    # title.place(x=614, y=4)



def maximize_h(e):

    maximize_button.config(image=photo8)


def maximize_l(e):
    maximize_button.config(image=photo7)


maximize_button = Button(title_bar, image=photo7, bd=0, bg=color2, activebackground=color2, command=maximize)
maximize_button.bind("<Enter>", maximize_h)
maximize_button.bind("<Leave>", maximize_l)
# endregion




# region Restore Down Button


def restore():

    win.geometry("1100x696+90+25")
    title_bar.config(width=1100)
    close_button.place(x=1054, y=0)
    maximize_button.place(x=1008, y=0)
    minimize_button.place(x=962, y=0)
    # title.place(x=500, y=4)


def restore_h(e):

    restore_button.config(image=photo6)


def restore_l(e):
    restore_button.config(image=photo5)


restore_button = Button(title_bar, image=photo5, bd=0, bg=color2, activebackground=color2, command=restore)
restore_button.place(x=1274, y=0)
restore_button.bind("<Enter>", restore_h)
restore_button.bind("<Leave>", restore_l)
# endregion



# region Minimize Button


def show_screen(event):
    win.deiconify()
    win.overrideredirect(1)


def hide_screen():
    win.overrideredirect(0)
    win.iconify()


def screen_appear(event):
    win.overrideredirect(1)


def minimize_h(e):
    minimize_button.config(image=photo4)


def minimize_l(e):
    minimize_button.config(image=photo3)


minimize_button = Button(title_bar, image=photo3, bd=0, bg=color2, activebackground=color2, command=hide_screen)
minimize_button.place(x=1230, y=0)
minimize_button.bind("<Enter>", minimize_h)
minimize_button.bind("<Leave>", minimize_l)
title_bar.bind("<Button-3>", show_screen)
title_bar.bind("<Map>", screen_appear)

# endregion

win.mainloop()
