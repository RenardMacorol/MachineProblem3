from tkinter import * #import tkinter

window = Tk() #instace a window 
standardtext =40 ## standard text size
window.geometry("1280x750")  # set size of a window
window.title("Machine Problem #3")
window.config(background="#dadef4") #voilet tokyo  

group_members = Label(window,
              text="Group Members",
              font=('RobotoMono',40,'bold'),
              fg='#000000', #Foregroud Color
              bg='#8590c5') #Background Color
group_members.place(x=415,y=30) 



group_List = "Macorol, \nCampos, \nTamayo, \nBandong"
group_ListVar = Message(window, 
                        text=group_List)
group_ListVar.config(bg="#fffcb0", 
                     font=('RobotoMono',standardtext,'bold'),
                     fg='#000000')
group_ListVar.place(x=415,y=100)

def click():
    window.quit()
    

button = Button(window,
                text="Quit",
                command=click,
                bg="#fffcb0", 
                font=('RobotoMono',40,'bold'),
                fg='#000000')

button.place(x=500,y=500)


window.mainloop() # set visible 



