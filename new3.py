import tkinter
from tkinter import *


window=Tk()
window.resizable(0, 0)

window.geometry('1100x696+90+25')
window.overrideredirect(1)
window.config(bg='#1e1e1e')


#(Start) To Make Window Dragable

lastClickX = 0
lastClickY = 0

def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
    window.geometry("+%s+%s" % (x , y))

window.attributes('-topmost', True)
window.bind('<Button-1>', SaveLastClickPos)
window.bind('<B1-Motion>', Dragging)

#(End) To Make Window DragAble


class window2:
    def __init__(self, master, *args, **kwargs):
        self.master= master

        #TitleBar Main
        self.titlebar = Frame(master, height=31, width=1100, bg="#3c3c3c")
        self.titlebar.pack()

        def restore():
            self.titlebar2.destroy()
            self.titlebar = Frame(master, height=31, width=1100, bg="#3c3c3c")
            self.titlebar.pack()
            window.geometry('1100x696+90+25')
            def maxl2(e):

                self.photo200 = PhotoImage(file=r'G:\Store Management Software Development\tkinter\new project\Untitled2.png')
                self.closebutton2 = Button(self.titlebar, image=self.photo200, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
                self.closebutton2.place(x=1054, y=1)
                self.closebutton2.bind("<Enter>", maxh2)

            def maxh2(e):

                self.photo90 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\button2.png')
                self.closebutton2 = Button(self.titlebar, image=self.photo90, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy, highlightcolor="#000000")
                self.closebutton2.place(x=1054, y=0)
                self.closebutton2.bind("<Leave>", maxl2)

        
         
            self.photo = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\Untitled2.png')
            self.closebutton2= Button(self.titlebar, image=self.photo, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
            self.closebutton2.place(x=1054, y=1)
            self.closebutton2.bind("<Enter>", maxh2)


            def maxl(e):

                self.photo20 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\smallrestore1.png')
                self.maximize= Button(self.titlebar, image=self.photo20, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=fullscreen)
                self.maximize.place(x=1008, y=0)
                self.maximize.bind("<Enter>", maxh)

            def maxh(e):

                self.photo9= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\smallrestore.png')
                self.maximize= Button(self.titlebar, image=self.photo9, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=fullscreen)
                self.maximize.place(x=1008, y=0)
                self.maximize.bind("<Leave>", maxl)

     
            self.photo2 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\smallrestore1.png')
            self.maximize= Button(self.titlebar, image=self.photo2, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=fullscreen)
            self.maximize.place(x=1008, y=0)
            self.maximize.bind("<Enter>", maxh)

            def show_screen(event):
                window.deiconify()
                window.overrideredirect(1)

            def hide_screen():
                window.overrideredirect(0)
                window.iconify()

            def screen_appear(event):
                window.overrideredirect(1)


            def maxl3(e):

                self.photo208 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize2.png')
                self.minimize= Button(self.titlebar, image=self.photo208, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=hide_screen)
                self.minimize.place(x=962, y=0)
                self.minimize.bind("<Enter>", maxh3)

            def maxh3(e):

                self.photo909= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize.png')
                self.minimize= Button(self.titlebar, image=self.photo909, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=hide_screen)
                self.minimize.place(x=962, y=0)
                self.minimize.bind("<Leave>", maxl3)


            self.photo540 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize2.png')
            self.minimize= Button(self.titlebar, image=self.photo540, bd=0, activebackground='#3c3c3c', bg='#3c3c3c')
            self.minimize.place(x=962, y=0)
            self.minimize.bind("<Enter>", maxh3)
            self.titlebar.bind("<Button-3>", show_screen)
            self.titlebar.bind("<Map>", screen_appear)
        
        
        
        
        #After Clicking Maximize Button
        def fullscreen():
                
            self.titlebar.destroy()
            window.geometry("1366x728+0+0")
            
            
            self.titlebar2 = Frame(master, height=29, width=1366, bg="#3c3c3c")
            self.titlebar2.pack()


            
            #START Close Button Full Screen
            def maxl6(e):

                self.photo411 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\Untitled2.png')
                self.closebutton5= Button(self.titlebar2, image=self.photo411, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
                self.closebutton5.place(x=1321, y=0)
                self.closebutton5.bind("<Enter>", maxh6)

            def maxh6(e):

                self.photo412= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\button2.png')
                self.closebutton5= Button(self.titlebar2, image=self.photo412, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
                self.closebutton5.place(x=1321, y=0)
                self.closebutton5.bind("<Leave>", maxl6)


            self.photo3 = PhotoImage(file= r'G:\Store Management Software Development\tkinter\new project\Untitled2.png')
            self.closebutton5 = Button(self.titlebar2, image=self.photo3, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
            self.closebutton5.place(x=1321, y=0)
            self.closebutton5.bind("<Enter>", maxh6)
            #END Close Button Full Screen


            #START Restore Down Button Full Screen
            def maxl5(e):

                self.photo297 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\Untitled.png')
                self.maximize6= Button(self.titlebar2, image=self.photo297, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=restore)
                self.maximize6.place(x=1275, y=0)
                self.maximize6.bind("<Enter>", maxh5)

            def maxh5(e):

                self.photo2970= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\restore3.png')
                self.maximize6= Button(self.titlebar2, image=self.photo2970, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=restore)
                self.maximize6.place(x=1275, y=0)
                self.maximize6.bind("<Leave>", maxl5)


            self.photo402 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\Untitled.png')
            self.maximize6 = Button(self.titlebar2, image=self.photo402, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=restore)
            self.maximize6.place(x=1275, y=0)
            self.maximize6.bind("<Enter>", maxh5)
            #END Restore Down Button Full Screen




            #START Minimize button Full Screen
            def show_screen(event):
                window.deiconify()
                window.overrideredirect(1)

            def hide_screen():
                window.overrideredirect(0)
                window.iconify()

            def screen_appear(event):
                window.overrideredirect(1)

            def maxl4(e):

                self.photo2087 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize2.png')
                self.minimize2= Button(self.titlebar2, image=self.photo2087, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=hide_screen)
                self.minimize2.place(x=1229, y=0)
                self.minimize2.bind("<Enter>", maxh4)

            def maxh4(e):

                self.photo909= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize.png')
                self.minimize2= Button(self.titlebar2, image=self.photo909, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=hide_screen)
                self.minimize2.place(x=1229, y=0)
                self.minimize2.bind("<Leave>", maxl4)


            self.photo540 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize2.png')
            self.minimize2= Button(self.titlebar2, image=self.photo540, bd=0, activebackground='#3c3c3c', bg='#3c3c3c')
            self.minimize2.place(x=1229, y=0)
            self.minimize2.bind("<Enter>", maxh4)
            self.titlebar2.bind("<Button-3>", show_screen)
            self.titlebar2.bind("<Map>", screen_appear)
            #END Minimize Button Full Screen







        # START Close Button Small Screen
        def maxl2(e):

            self.photo200 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\Untitled2.png')
            self.closebutton2= Button(self.titlebar, image=self.photo200, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
            self.closebutton2.place(x=1054, y=1)
            self.closebutton2.bind("<Enter>", maxh2)

        def maxh2(e):

            self.photo90= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\button2.png')
            self.closebutton2= Button(self.titlebar, image=self.photo90, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy, highlightcolor="#000000")
            self.closebutton2.place(x=1054, y=0)
            self.closebutton2.bind("<Leave>", maxl2)

        
         
        self.photo = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\Untitled2.png')
        self.closebutton2= Button(self.titlebar, image=self.photo, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=window.destroy)
        self.closebutton2.place(x=1054, y=1)
        self.closebutton2.bind("<Enter>", maxh2)
        #END Close Button Small Screen



        #START Maximize Button Small Screen 
        def maxl(e):

            self.photo20 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\smallrestore1.png')
            self.maximize= Button(self.titlebar, image=self.photo20, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=fullscreen)
            self.maximize.place(x=1008, y=0)
            self.maximize.bind("<Enter>", maxh)

        def maxh(e):

            self.photo9= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\smallrestore.png')
            self.maximize= Button(self.titlebar, image=self.photo9, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=fullscreen)
            self.maximize.place(x=1008, y=0)
            self.maximize.bind("<Leave>", maxl)

     
        self.photo2 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\smallrestore1.png')
        self.maximize= Button(self.titlebar, image=self.photo2, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=fullscreen)
        self.maximize.place(x=1008, y=0)
        self.maximize.bind("<Enter>", maxh)
        #END Maximize Button Small Screen 


        #START Minimize Buttton Small Screen 
        def show_screen(event):
            window.deiconify()
            window.overrideredirect(1)

        def hide_screen():
            window.overrideredirect(0)
            window.iconify()

        def screen_appear(event):
            window.overrideredirect(1)

            
        def maxl3(e):

            self.photo208 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize2.png')
            self.minimize= Button(self.titlebar, image=self.photo208, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=hide_screen)
            self.minimize.place(x=962, y=0)
            self.minimize.bind("<Enter>", maxh3)

        def maxh3(e):

            self.photo909= PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize.png')
            self.minimize= Button(self.titlebar, image=self.photo909, bd=0, activebackground='#3c3c3c', bg='#3c3c3c', command=hide_screen)
            self.minimize.place(x=962, y=0)
            self.minimize.bind("<Leave>", maxl3)


        self.photo540 = PhotoImage(file = r'G:\Store Management Software Development\tkinter\new project\minimize2.png')
        self.minimize= Button(self.titlebar, image=self.photo540, bd=0, activebackground='#3c3c3c', bg='#3c3c3c')
        self.minimize.place(x=962, y=0)
        self.minimize.bind("<Enter>", maxh3)
        self.titlebar.bind("<Button-3>", show_screen)
        self.titlebar.bind("<Map>", screen_appear)
        #END Minimize Button Small Screen


    
    

r= window2(window)

window.mainloop()
