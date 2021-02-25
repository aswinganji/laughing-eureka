from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Titleused419thtime")
root.geometry("1000x1000")


kepress = ""
canvas = Canvas(root,width = 590,height = 510,bg = "white",highlightbackground = "lightgray")
canvas.pack()

color_label = Label(root,text = "End y")
color_label.place(relx = 0.9,rely = 0.86,anchor = CENTER)

color_label2 = Label(root,text = "End x")
color_label2.place(relx = 0.8,rely = 0.86,anchor = CENTER)

color_label3 = Label(root,text = "Start y")
color_label3.place(relx = 0.7,rely = 0.86,anchor = CENTER)

color_label4 = Label(root,text = "Start x")
color_label4.place(relx = 0.6,rely = 0.86,anchor = CENTER)

color_label5 = Label(root,text = "Color")
color_label5.place(relx = 0.5,rely = 0.86,anchor = CENTER)

cl = ["red","blue"]
ey = ["10","20","30","40","50","100","200"]
sv = StringVar()
sv1= StringVar()
sv2= StringVar()
sv3= StringVar()
sv4= StringVar()

d1 = ttk.Combobox(root,state = "readonly",value = ey,width = 10)
d1.place(relx = 0.9,rely = 0.88,anchor = CENTER)

d2 = ttk.Combobox(root,state = "readonly",value = ey,width = 10)
d2.place(relx = 0.8,rely = 0.88,anchor = CENTER)

d3 = ttk.Combobox(root,state = "readonly",value = ey,width = 10)
d3.place(relx = 0.7,rely = 0.88,anchor = CENTER)

d4 = ttk.Combobox(root,state = "readonly",value = ey,width = 10)
d4.place(relx = 0.6,rely = 0.88,anchor = CENTER)

d5 = ttk.Combobox(root,state = "readonly",value = cl,width = 10)
d5.place(relx = 0.5,rely = 0.88,anchor = CENTER)

def circle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'c'
    draw(keypress,oldx,oldy,newx,newy)
    
def rectangle(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'r'
    draw(keypress,oldx,oldy,newx,newy)
    
def line(event):
    oldx = d1.get()
    oldy = d2.get()
    newx = d3.get()
    newy = d4.get()
    keypress = 'l'
    draw(keypress,oldx,oldy,newx,newy)
    
def draw(keypress,oldx,oldy,newx,newy):
    color = d5.get()

    
    if keypress == 'c':
        dr = canvas.create_oval(oldx,oldy,newx,newy,fill = color)
        
    if keypress == 'r':
        dr = canvas.create_rectangle(oldx,oldy,newx,newy,fill = color)
        
    if keypress == 'l':
        dl1 = canvas.create_rectangle(oldx,oldy,newx,newy,fill = color)






root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)


root.mainloop()