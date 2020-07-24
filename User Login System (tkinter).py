import tkinter
from tkinter.messagebox import askquestion
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import pandas as pd
from pandas import Series, DataFrame


generatedPasswords=['1LgiyhcT','Vpk!#Os8','K2XTUvHt','kPYO2AI$','V(ebA06I','5?jbFKru','2ORrhPmk','9KxuU?Sn','GUB8wPzp','!5CUtV0j','K8kq%l3j','G!MiKFv$','M1eFp$S!','kQ(o4izt',
'S9nmQ0AG','(tWMc6nP','aOVIYU(D','sOrxQHk&','kfW7XK?G','#rsL0RCd','uNfCLI2F','rth8fL3q','FSOvf48a','L^d503zu','QL51wUbk','*Vm5nXHw','gd9c?6^T','Z&50834@',
'$(qW!ewY','!azfdi0w','zn@jRMi?','OXiqSPht','&QdVf0m9','$9SrQy@l','xIUMjzir','T*AhE(2d','gsSA4^h2',
'?zR9A#1$','jUNI5VAQ','SEOYw3au','R)d@EAM*','i5dQrN@l','oetDhM03','zc7dFagQ','rj2CL0qe','RmtyPVLB','8JxzSrph','g20uTFH@',
'u6wl$X)V','iDX3C#6s','aswEN3rg','t5B@&YeN','(G%?Wop0','f*2OkPKe','mja0^u54','eKF^(Y!@','zC&?%NMe','%gr124o(','fUpDms6B','YA4Xdf$H','3#lNV(5z','K^Il0*JA','&BoSqw%R','Tl&qxK0w','rceZuHWl','12Oqx0X7','QBPykima','JgF)5tUp','euyEl?W0','(%ap$hR8','kG?oR0j9',
'ltkP2?6q','oIt$xzQ@','RGcfC5Fu','v)0HogMq','^AqkWMYZ','$othXEkr','qsZyWOjv','cTV@SgBP','id%4sM!z','B)vatjx^','6rkR(Ddw','fOmVvZp%','Lm^VDBQn','gtSb#1I0',
'A(eg&HN$','2lW!^Pzr','$e^36(Y)','ftVs6*4?','wj7AH@Ot','3xdgQX0b','^6kpwMWa','d8ca(iln','I1rs!O7f','A90OJHn!','luh^S*R5','@bh*(MZI','e00tW)Ui','Tj!LM@y9','PJZpjqI3']



class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("OAU at night.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES),self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image = self.background_image)


root = Tk()

root.overrideredirect(False)


root.title(" Welcome to our portal ! , "
               " Login or Sign up to continue.")

e = Example(root)
e.pack()
e.focus_set()
root.configure(background='AntiqueWhite1')






def login():
    from tkinter import messagebox


    username1 = E1.get()
    password1 = E2.get()

    if (password1 in generatedPasswords):

        msg = messagebox.showinfo('Login successful !.', ' Thank you ' + username1 + ', for using this service!.')


        return


    if (username1=='admin') and (password1=='admin'):
        
        root= Tk()
        
        def open():
            textbox = ScrolledText()
            # textbox.grid()
            filename = askopenfilename(initialdir='c:\\python31\\',
                                       filetypes=[('Text files', '.txt'), ('All files', '*')])
            s = open('5-year-mean-1882-2014').read()
            textbox.insert(1.0, s)

        def donothing():
            filewin = Toplevel(root)
            button = Button(filewin, text="Do nothing button")
            button.pack()

        def nothing():
            from tkinter import messagebox
            msg = messagebox.showinfo("Warning", "No function assigned yet!.")

        def helpline():
            from tkinter import messagebox
            msg = messagebox.showinfo("Problems with operations?", "Call: +2348148918155.")

        def About():
            from tkinter import messagebox
            msg = messagebox.showinfo('A user login system tkinter program.')

        def quit():
            answer = askquestion(title='Quit?', message='Really quit?')
            if answer == 'yes':
                root.destroy()

        root.protocol('WM_DELETE_WINDOW', quit)

        root.geometry('300x300')
        root.title("Welcome here!")
        var = ("Hey!? How are you doing?")
        label = Label(root, textvariable=var, relief=RAISED, bg='yellow')

        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0, bd=2, bg='orange')
        filemenu.add_command(label="New", command=nothing)
        filemenu.add_command(label="Open", command=open)
        filemenu.add_command(label="Save", command=nothing)
        filemenu.add_command(label="Save as...", command=nothing)
        filemenu.add_command(label="Close", command=nothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0, bd=2, bg='brown')
        editmenu.add_command(label="Undo", command=nothing)

        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=nothing)
        editmenu.add_command(label="Copy", command=nothing)
        editmenu.add_command(label="Paste", command=nothing)
        editmenu.add_command(label="Delete", command=nothing)
        editmenu.add_command(label="Select All", command=nothing)
        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0, bd=2, bg='purple')
        helpmenu.add_command(label="Help Index", command=nothing)
        helpmenu.add_command(label="About...", command=About)
        helpmenu.add_command(label='Call Author?.', command=helpline)
        menubar.add_cascade(label="Help", menu=helpmenu)
        aboutmenu = Menu(menubar, tearoff=0)
        aboutmenu.add_command(label='About Project', command=About)

        root.config(menu=menubar)

        
        
        
        root.configure(bg='chocolate')
        root.mainloop()

    if (username1=='') and (password1==''):
        msg = messagebox.showinfo('Error!.', ' You left the boxes blank. Contact: +2348148918155 if you are confused on how to use this portal.')



    else:
        msg = messagebox.showinfo('Login failed!.', 'Check details again or contact: +2348148918155.'
                                  
                                                                  ' Thank you ' + username1 + ', for using this service!.')

    return


def signup():
    from tkinter import messagebox
    

    
    root = Tk()
    
    
    root.title("Fill up your details to register with us !.")
    

    command1 = Label(root, text="Name :", font=('Hobo Std', 13, 'bold'), borderwidth='3', foreground='darkblue')
    command1.place(x=20, y=215)

    command2 = Label(root, text="Age :", font=('Hobo Std', 13, 'bold'), borderwidth='3',foreground='darkblue')
    command2.place(x=20, y=265)

    command3 = Label(root, text="Sex :", font=('Hobo Std', 13, 'bold'), borderwidth='3', foreground='darkblue')
    command3.place(x=20, y=315)

    command4 = Label(root, text="Email address:", font=('Adobe Caslon Pro Bold', 10, 'bold'), borderwidth='4',foreground='darkred')
    command4.place(x=50, y=635)

    command5 = Label(root, text="Phone Number:", font=('Adobe Caslon Pro Bold', 10, 'bold'), borderwidth='4',foreground='darkred')
    command5.place(x=450, y=635)

    
    command6 = Label(root, text="Username:", font=('batang', 9, 'bold'), borderwidth='4')
    command6.place(x=500, y=322)
    command7 = Label(root, text="Password:", font=('batang', 9, 'bold'), borderwidth='4')
    command7.place(x=500, y=422)



    Ent1 = StringVar()  # For Name
    Ent2 = StringVar()  # For Age
    Ent3 = StringVar()  # For Sex
    Ent4 = StringVar()  # For email
    Ent5 = StringVar()  # For phone number
    Ent6 = StringVar()  # For username
    Ent7 = StringVar()  # For password

    ent1 = Entry(root, textvariable=Ent1)  # For Name
    ent1.place(x=101, y=219)
    ent2 = Spinbox(root, textvariable=Ent2 ,from_=0, to_=100)  # For Age
    ent2.place(x=90, y=269)
    ent3 = ttk.Combobox(root, textvariable=Ent3, values=['Male', 'Female', 'Not specified'])  # For Sex
    ent3.place(x=90, y=321)
    ent4 = Entry(root, textvariable=Ent4, show='*')  # For email address
    ent4.place(x=160, y=640)
    ent5 = Entry(root, textvariable=Ent5)  # For phone number
    ent5.place(x=560, y=640)

    ent6 = Entry(root, bd=5,textvariable=Ent6)  # Entry for username
    ent6.place(x=653, y=322)
    ent7 = Entry(root, bd=5,textvariable=Ent7)
    ent7.place(x=653, y=422)  # Entry for password

    name = str(Ent1.get())
    age = str(Ent2.get())
    sex = Ent3.get()
    email = Ent4.get()
    phonenumber = Ent5.get()
    username2 = Ent6.get()
    password2 = Ent7.get()



    def submit():

        if (name.isalpha()) and (age.isdigit()) and (len(int(phonenumber.isdigit()))==11):
            msg = messagebox.showinfo('Login successful !.', ' Thank you ' + username + ', for using this service!.')


        elif name.isdigit():
            msg = messagebox.showinfo('Invalid input !.', ' Correct your entry in Name')

        elif age.isalpha():
            msg = messagebox.showinfo('Invalid input !.', ' Correct your entry in Age ( Age should be digit(s).')

        elif len(int(phonenumber.isdigit()))!=11 :
            msg = messagebox.showinfo('Invalid input !.', ' Correct your entry in Phone number.')


        return


    submitButton = Button(root, text="Submit Form", font=('batang', 10, 'bold'), borderwidth='4', foreground='black', command = submit)
    submitButton.place(x=1100, y=655)
    
    

    
    
    
    root.configure(bg='darkred')
    root.mainloop()
    
    return



E1 = StringVar()
E2 = StringVar()




L1 = Label(root, text="Username:",font=('batang', 9, 'bold'), borderwidth='4')
L1.place(x=500, y=322)
L2 = Label(root, text="Password:",font=('batang', 9, 'bold'), borderwidth='4')
L2.place(x=500, y=422)

E1 = Entry(root, bd=5)          # Entry for username
E1.place(x=653, y=322)
E2 = Entry(root, bd=5)
E2.place(x=653, y=422)              # Entry for password

B1 = Button(root, text="Login", font=('calibri', 11, 'bold'),foreground='darkblue', borderwidth=4, command=login)
B1.place(x=655, y=560)

B2 = Button(root, text="Sign up", font=('calibri', 11, 'bold'),foreground='darkblue', borderwidth=4, command=signup)
B2.place(x=1150, y=100)

























root.mainloop()

