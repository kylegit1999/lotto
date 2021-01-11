import random
from tkinter import *
from tkinter import messagebox as mb
from datetime import *
# Creating a Window


window = Tk()
window.title("Lotto App")
window.geometry("600x400")
window.configure(background="yellow")

date = datetime.now()
dtm = Label(window, bg='yellow',fg='black')
dtm.place(x=200, y=200)
dtm.config(text=date.strftime("%d %B"+"\n"+" %Y %H: %M: %p"))



def reward():
    try:
        lottery1 = int(first_numEnt.get())
        lottery2 = int(sec_numEnt.get())
        lottery3 = int(third_numEnt.get())
        lottery4 = int(fourth_numEnt.get())
        lottery5 = int(fifth_numEnt.get())
        lottery6 = int(sixth_numEnt.get())
        lottery_list = [lottery1, lottery2, lottery3, lottery4, lottery5, lottery6]

    except ValueError:
        mb.showerror("Error", "Only enter numbers")

    return lottery_list


# creating the Entry Boxes for the player's Numbers

first_numEnt = Entry(window, relief='flat', width=5, bd=4, fg='black', bg='white')
first_numEnt.grid(row=1, column=1, padx=5, pady=7)
sec_numEnt = Entry(window, relief='flat', width=5, bd=4, fg='black', bg='blue')
sec_numEnt.grid(row=1, column=2, padx=5, pady=7)
third_numEnt = Entry(window, relief='flat', width=5, bd=4, fg='black', bg='pink')
third_numEnt.grid(row=1, column=3, padx=5, pady=7)
fourth_numEnt = Entry(window, relief='flat', width=5, bd=4, fg='black', bg='cyan')
fourth_numEnt.grid(row=1, column=4, padx=5, pady=7)
fifth_numEnt = Entry(window, relief='flat', width=5, bd=4, fg='black', bg='powderblue')
fifth_numEnt.grid(row=1, column=5, padx=5, pady=7)
sixth_numEnt = Entry(window, relief='flat', width=5, bd=4, fg='black', bg='lawngreen')
sixth_numEnt.grid(row=1, column=6, padx=5, pady=7)


# Creating the Labels for the lottery numbers
first_num = Label(window, relief='groove', width=5, bd=4, text="0", fg='black', bg='cyan')
first_num.grid(row=2, column=1, padx=5, pady=7)
sec_num = Label(window, relief='groove', width=5, bd=4, text="0", fg='black', bg='cyan')
sec_num.grid(row=2, column=2, padx=5, pady=7)
third_num = Label(window, relief='groove', width=5, bd=4, text="0", fg='black', bg='cyan')
third_num.grid(row=2, column=3, padx=5, pady=7)
fourth_num = Label(window, relief='groove', width=5, bd=4, text="0", fg='black', bg='cyan')
fourth_num.grid(row=2, column=4, padx=5, pady=7)
fifth_num = Label(window, relief='groove', width=5, bd=4, text="0", fg='black', bg='cyan')
fifth_num.grid(row=2, column=5, padx=5, pady=7)
sixth_num = Label(window, relief='groove', width=5, bd=4, text="0", fg='black', bg='cyan')
sixth_num.grid(row=2, column=6, padx=5, pady=7)


def lottery_numbers():
    first_num.configure(text=str(random.sample(range(1, 49),1)))
    sec_num.configure(text=str(random.sample(range(1, 49),1)))
    third_num.configure(text=str(random.sample(range(1, 49),1)))
    fourth_num.configure(text=str(random.sample(range(1, 49),1)))
    fifth_num.configure(text=str(random.sample(range(1, 49),1)))
    sixth_num.configure(text=str(random.sample(range(1, 49),1)))

    lotto_list = [fifth_num['text'], sec_num['text'], third_num['text'], fourth_num['text'], fifth_num['text'], sixth_num['text']]
    print(lotto_list)
    mylist = []

    for i in lotto_list:
        try:
            i=i[1:-1]
            mylist.append(int(i))
        except ValueError:
            mb.showerror("Value Error","Only enter numbers")


    #counting correct numbers
    num = 0
    player = reward()
    for i in player:
        if i in mylist:
            num += 1

    #checking correct numbers for prize
    if num == 6 :
        mb.showinfo("result", "You Won R10 000 000")


    elif num == 5 :
        mb.showinfo("result", "You Won R8584")
    elif num == 4 :
        mb.showinfo("result", "You Win R2384")
    elif num == 3 :
        mb.showinfo("result", "You Win R100.50")
    elif num == 2 :
        mb.showinfo("result", "You Win R20")
    else:
        mb.showinfo("result", "You Lose")


# f = open("text_file.py", "w+")
# f.close()
    f = open("text_file.txt", "a")
    #results = third_numEnt.get()
    f.write(first_num.cget("text"))
    f.write(sec_num.cget("text"))
    f.write(third_num.cget("text"))
    f.write(fourth_num.cget("text"))
    f.write(fifth_num.cget("text"))
    f.write(sixth_num.cget("text"))

    f.close()

def reset(text):

    first_numEnt.delete(0, END)
    first_numEnt.insert(0, text)
    sec_numEnt.delete(0, END)
    sec_numEnt.insert(0, text)
    third_numEnt.delete(0, END)
    third_numEnt.insert(0, text)
    fourth_numEnt.delete(0, END)
    fourth_numEnt.insert(0, text)
    fifth_numEnt.delete(0, END)
    fifth_numEnt.insert(0, text)
    sixth_numEnt.delete(0, END)
    sixth_numEnt.insert(0, text)


    first_num.configure(text=str(0))
    sec_num.configure(text=str(0))
    third_num.configure(text=str(0))
    fourth_num.configure(text=str(0))
    fifth_num.configure(text=str(0))
    sixth_num.configure(text=str(0))
    return








# creating a generator button
generator = Button(window, width=20, text="Generate Numbers", command=lottery_numbers)
generator.configure(fg='white', bg='purple')
generator.grid(row=3, column=1, padx=5, pady=7)







# Creating a clear button
clear_btn = Button(window, width=10, text="Clear", command=lambda: reset(""))
clear_btn.configure(fg="white", bg="purple")
clear_btn.grid(row=3, column=2, padx=5, pady=7)


# Defining a Function to Close the App
def Exit():
    quit()


# Creating an exit button
exitButton = Button(window, command=Exit)
exitButton.configure(text="Exit", fg='white', bg='purple')
exitButton.grid(row=3, column=4, columnspan=6, pady=7)

exitButton.configure(command=Exit)


# Attaching the "close" Function to the "close" Button
exitButton.configure(command=Exit)

# This is the Line That Runs the Program Until You Exit
window.mainloop()
