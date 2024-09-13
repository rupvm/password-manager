
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '*']



    pass_letters=[choice(letters) for _ in range(randint(4,8))]
    pass_numbers=[choice(numbers) for _ in range(randint(2,4))]
    pass_symbols=[choice(symbols) for _ in range(randint(2,4))]

    password_list=pass_letters+pass_numbers+pass_symbols
    print(password_list)
    shuffle(password_list)

    password="".join(password_list)
    e3.delete(0,'end')
    e3.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website=e1.get()
    email_name=e2.get()
    password=e3.get()

    new_entry={
        website:{
            "email":email_name,
            "password":password
        }
    }

    if website=="" or password=="":
        messagebox.showinfo(title="empty fields",message="you have left some of the fields empty")
    else:
        try:
            with open("password_manager.json",mode='r') as file:  #try to open the file if exists
                                                                    #if exists then else part is executed
                # reading old data
                data = json.load(file)

        except FileNotFoundError: # if not found then create the file and dump the initial value
            with open("password_manager.json",mode="w") as file:
                json.dump(new_entry,file,indent=4)

        else:
            # updating existing data,  update the data and dump the updated file
            data.update(new_entry)
            #saving the data
            with open("password_manager.json",mode="w") as file:
                json.dump(data,file,indent=4)
        finally:
            #saving the data back to the file
            e1.delete(0,'end')
            e3.delete(0,'end')


# ---------------------------- SEARCH ------------------------------- #

def search():
    website = e1.get()
    if website=="":
        messagebox.showinfo(title="empty fields",message="you have left some of the fields empty")
    else:
        try:
             with open("password_manager.json","r") as file:
                data=json.load(file)

        except FileNotFoundError:
            messagebox.showinfo(title="file",message="no such data file found")
        else:
            if website in data:
                messagebox.showinfo(title=website,message=f"This website already exists email {data[website]["email"]} and password {data[website]["password"]}")
                print(data[website]["email"])
                print(data[website]["password"])
            else:
                messagebox.showinfo(title=website,message=f"No such details found for {website}")







# ---------------------------- UI SETUP ------------------------------- #

root=Tk()
root.title("Password Manager")
root.config(padx=20,pady=20)


pic=PhotoImage(file="logo.png")
canvas=Canvas()
canvas.config(height=200,width=200)
canvas.create_image(110,110,image=pic)
canvas.grid(column=1,row=1)

website_label=Label(text="website:")
website_label.grid(column=0,row=2)

e1=Entry(width=31)
e1.grid(column=1,row=2,columnspan=1)
e1.focus()

l2=Label(text="Email/Username:")
l2.grid(column=0,row=3)
e2=Entry(width=31)
e2.grid(column=1,row=3,columnspan=1)
e2.insert(0,"halder.rupam2003@gmail.com")

l3=Label(text="Password:")
l3.grid(column=0,row=4)

e3=Entry(width=31)
e3.grid(column=1,row=4)


b1=Button(text="Generate Password",command=generate_password)
b1.grid(column=2,row=4)


b2=Button(text="Add",width=36,command=add)
b2.grid(column=1,row=5,columnspan=2)




b3=Button(text="Search",command=search)
b3.grid(column=2,row=2)



















root.mainloop()