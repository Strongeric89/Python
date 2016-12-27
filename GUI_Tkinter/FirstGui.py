from Tkinter import *
root = Tk()
label_1 = Label(root,text='username:',fg='red',bg='black')
label_2 = Label(root,text='password:',fg='blue',bg='black')
entry_1 = Entry(root,bg='black',fg='white')
entry_2 = Entry(root)

#map the labels
label_1.grid(row=0)
label_2.grid(row=1)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

root.mainloop()


