from tkinter import *



root = Tk()
label0 = Label(master=root, text='Vul uw station in: ', background='yellow', height=2)
label0.pack()

entry = Entry(master=root)
entry.pack(padx=10, pady=5)



label1 = Label(master=root, height=2)
label1.pack()

label2 = Label(master=root, height=2)
label2.pack()

label3 = Label(master=root, height=2)
label3.pack()

label4 = Label(master=root, height=2)
label4.pack()

label5 = Label(master=root, height=2)
label5.pack()

root.mainloop()