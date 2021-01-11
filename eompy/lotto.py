#importing
from tkinter import *
from tkinter import messagebox

#to create executable
#pyinstaller lotto.py --onefile

window=Tk()
window.geometry("300x300")
window.title("Lotto")
window.configure(background="yellow")

def check():

    age = int(age_entry.get())
    if age>=18:
        messagebox.showinfo("Qualify", "Adult accepted")
        window.withdraw()
        exec(open('mine.py').read())

    elif age<18:
        messagebox.showerror("Qualify", "No kids")
        age_lbl.delete(0,END)
        age_lbl.Entry.delete(0, END)

age_lbl = Label(window, text='What is your name?:')
age_lbl.grid(row=1, column=1, padx=5, pady=7)
age_lbl = Label(window, text='How old are you:')
age_lbl.grid(row=2, column=1, padx=5, pady=7)

window.configure(background="yellow")
age_entry = Entry(window, borderwidth=4)
age_entry.grid(row=3, column=1)
age_entry = Entry(window, borderwidth=4)
age_entry.grid(row=4, column=1)

age_btn=Button(window, text="Check", command=check, bg='yellow', fg='black')
age_btn.grid(row=6, column=3)


window.mainloop()
