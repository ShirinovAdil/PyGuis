from tkinter import *
import tkinter.messagebox
#COMENTS BELOW,SCROLL DOWN


# **** FUNCTIONS ****
def nothing():
    print("Action is not supported yet")
    window = Toplevel(root,bg = "#b4dce8") #Creating a window on click
    window.iconbitmap('ico.ico')
    window.geometry("500x300")

    status = Label(window, text="Status: ", bd=1, relief=SUNKEN, anchor=W, height=2, bg="#4d5c6b", fg="#bd64e0")
    status.pack(side=BOTTOM, fill=X)
    status.config(font=("Courier", 12))
# ----------------------------------------------------------------------------------------




#  **** ROOT SETTINGS ****
root = Tk()
root.title("Calculator")
root.configure(background='#909ca8')
root.minsize(800, 400)
root.iconbitmap('ico.ico')
# ----------------------------------------------------------------------------------------


#   ****  MAIN MENU *****
my_menu = Menu(root)        # СОЗДАЕТ МЕНЮ НА ВЕРХНЕЙ ЧАСТИ ЭКРАНА
root.config(menu = my_menu) #  КОНФИГИРУЕТ МЕНЮ НА ВЕРХНЕЙ ЧАСТИ ЭКРАНА
# ----------------------------------------------------------------------------------------


#First dropdown
sub_menu = Menu(my_menu)   # создает элемент верхнего меню
my_menu.add_cascade(label = "File" , menu = sub_menu)     # ЗАГОЛОВОК У ДРОПДАУН МЕНЮ и его название


sub_menu.add_command(label = "New project.", command = nothing)   #СОЗДАЕТ ОДИН ИЗ ВАРИАНТОВ(ФУНКЦИЙ) В ДРОПДАУН МЕНЮ
sub_menu.add_command(label = "New file.", command = nothing)               #СОЗДАЕТ ОДИН ИЗ ВАРИАНТОВ(ФУНКЦИЙ) В ДРОПДАУН МЕНЮ
sub_menu.add_separator()        # линия между меню которые вываливаются
sub_menu.add_command(label = "EXIT", command = nothing)                #СОЗДАЕТ ОДИН ИЗ ВАРИАНТОВ(ФУНКЦИЙ) В ДРОПДАУН МЕНЮ
# ----------------------------------------------------------------------------------------


#Second dropdown
edit_menu = Menu(my_menu)    #Второе меню дропдаун наверху
my_menu.add_cascade(label = "Edit", menu = edit_menu)       #  2 ЗАГОЛОВОК У ДРОПДАУН МЕНЮ задаем его название
edit_menu.add_command(label = "About", command = nothing)         #СОЗДАЕТ ОДИН ИЗ ВАРИАНТОВ(ФУНКЦИЙ) В ДРОПДАУН МЕНЮ
# ----------------------------------------------------------------------------------------


#Third dropdown
last_menu = Menu(my_menu)
my_menu.add_cascade(label = "Help", menu = last_menu)        # ЗАГОЛОВОК 3-ГО МЕНЮ
last_menu.add_command(label = "Settings", command = nothing)  #Вариант
# ----------------------------------------------------------------------------------------


# *** TOOLBAR ***
toolbar = Label(root,bg = "#163049")
firsttool = Button(toolbar,text = "Cut", command = nothing)
firsttool.pack(side=LEFT,padx = 2,pady = 2 )
secondtool = Button(toolbar,text = "Crop", command = nothing)
secondtool.pack(side = LEFT,padx = 2,pady = 2 )
toolbar.pack(side = TOP,fill = X)        #fill = X чтобы растянуть на весь экран
# ----------------------------------------------------------------------------------------


# *** STATUS BAR ***
status = Label(root, text = "Status: ",bd = 1, relief = SUNKEN, anchor = W, height = 2,bg = "#4d5c6b",fg = "#bd64e0")
status.pack(side = BOTTOM, fill = X)
status.config(font = ("Courier", 12))
#  ----------------------------------------------------------------------------------------


"""
# **** MAIN INTERACRION MENU ****

user = Entry(root,bg = "#4d5c6b")
user.pack()
user.place(x = 250,y = 250,height = 100)
# ----------------------------------------------------------------------------------------
"""



#  **** MESSAGE BOX ****
#answer = tkinter.messagebox.askquestion("Question 1", "Do u like Barcelona?")
#if answer == "yes":
    #tkinter.messagebox.showinfo("STUPIIIIIIDD", "LOOOOOOOOOL YOU ARE STUPID ASS")
#else:
    #tkinter.messagebox.showinfo("GOOD BOY", "YOU ARE A SMART GUY")
#/////////////////////////////////////////////////////////

# **** PHOTO INSERTION ***
#photo = PhotoImage(file = "lol.png")
#label = Label(root, image = photo)
#label.pack(side = RIGHT, expand = TRUE)
#//////////////////////////////////////////////

root.mainloop()

























"""     MAKING A WINDOW WITH PRINT AND QUIT FUNCTIONING
class My_buttons:

    def __init__(self,master):
        frame = Frame(master, width = 400, height = 500)
        frame.pack()

        self.print_but = Button(frame, text = "Print the text", command = self.msg)
        self.print_but.pack(side = LEFT)


        self.quit = Button(frame, text = "Quit", command = frame.quit)
        self.quit.pack(side=LEFT)

    def msg(self):
        print("LOL, THIS WORKS")




root = Tk()

adil = My_buttons(root)
root.mainloop()
"""
















"""        WAYS TO BIND CLICKS OF MOUSE
def left(event):
    print("U just left clicked a button or whatever")

def right(event):
    print("U just right clicked lol")

def middle(event):
    print("WTF?!?! Scroll???")


frame = Frame(root,width = 300, height = 250)
frame.bind("<Button - 1>",left)
frame.bind("<Button - 2>",middle)
frame.bind("<Button - 3>",right)
frame.pack()"""









"""def say_my_name():
    print("My name is Adil!")                            One of the ways to bind widget

but_name = Button(root,text = "Show the name",bg = 'black',fg = 'red',command = say_my_name)
but_name.pack()"""


"""
def say_my_name(event):
    print("My name is Adil!")        ANOTHER WAY TO BIND A WIDGET

but_name = Button(root,text = "Show the name",bg = 'black',fg = 'red')
but_name.bind("<Button - 1>",say_my_name)
but_name.pack()"""

 #  topFrame = Frame(root)  AND botFrame = Frame(root)  botFrame.pack(side = BOTTOM)
#  #my_label = Label(root,text = "This is my first label")           # print text in window
#my_label.pack()        # pack object
#Entry(root, show ="$")

 #la.grid(row = 0 , sticky = E )   #place label at row one and sticked to right
 #button1 = Button(topFrame,text = "Button1",fg = "red",bg = "grey")
#checkbox = Checkbutton(root , text = "Keep me logged in")     # Making a checkbox
 #lab2 = Label(root,text = "LOsadadL",bg = "blue", fg = "yellow")
 #show = Button(root,text = "Show",command = login()).grid(row = 1 , column = 3)
# #lab2.pack(side = LEFT,expand=True) MAKING LABEL RESPONSIVE


#checkbox.grid(columnspan = 2) # make checkbox take 2 columns

# keeps window running