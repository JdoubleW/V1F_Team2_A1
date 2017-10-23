from tkinter import *

root = Tk()

mainmenu = Frame(master=root)
mainmenu.pack(fill="both", expand=True)
label = Label(master=root,
               text='Welkom bij NS',
               background='yellow',
               foreground='blue',
               font=('', 40, ''),
               width=40,
               height=12)

button1 = Button(master=root,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='blue',
                width=20,
                height=4)

button2 = Button(master=root,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='blue',
                width=20,
                height=4)

button3 = Button(master=root,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='blue',
                width=20,
                height=4)

button4 = Button(master=root,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='blue',
                width=20,
                height=4)

button_dutch = Button(master=root,
                foreground='white',
                background='blue',
                width=20,
                height=4)
label.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
button_dutch.place(y=655)
root.mainloop()