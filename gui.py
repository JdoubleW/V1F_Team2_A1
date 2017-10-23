from tkinter import *

def showMainFrameNL():
    mainframeENG.pack_forget()
    mainframeNL.pack()

def showMainFrameENG():
    mainframeNL.pack_forget()
    mainframeENG.pack()

def clickedENG():
    showMainFrameENG()

def clickedNL():
    showMainFrameNL()


##################################################################################


root = Tk()
mainframeNL = Frame(master=root)          #Start mainframe
mainframeNL.pack(fill="both", expand=True)

label = Label(master=mainframeNL,
               text='Welkom bij NS',
               background='yellow',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)

button1 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button2 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button3 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button4 = Button(master=mainframeNL,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_ENG = Button(master=mainframeNL,
                command=clickedENG,
                background='#3333FF',
                width=10,
                height=4)
label.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
button_ENG.place(x=0, y=655)

##################################################################################

mainframeENG = Frame(master=root)
mainframeENG.pack(fill="both", expand=True)

label = Label(master=mainframeENG,
               text='Welcome to NS',
               background='yellow',
               foreground='#3333FF',
               font=('', 40, ''),
               width=40,
               height=12)

button1 = Button(master=mainframeENG,
                text='Show departure times \n from Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button2 = Button(master=mainframeENG,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button3 = Button(master=mainframeENG,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button4 = Button(master=mainframeENG,
                text='Weergeef vertrektijden \n van Utrecht Centraal',
                foreground='white',
                background='#3333FF',
                width=20,
                height=4)

button_NL = Button(master=mainframeENG,
                command=clickedNL,
                background='#3333FF',
                width=10,
                height=4)


label.pack()
button1.place(x=310, y=550)
button2.place(x=480, y=550)
button3.place(x=650, y=550)
button4.place(x=820, y=550)
button_ENG.place(x=0, y=655)
button_NL.place(x=0, y=655)
showMainFrameNL()
root.mainloop()