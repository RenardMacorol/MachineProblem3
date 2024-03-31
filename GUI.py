from tkinter import * #import tkinter

#NOTE!! Plss for Development GUI Refer in this link 
# https://www.canva.com/design/DAGA173ym1c/d_z45DCcBHGC4QYWXCA_Fg/edit?utm_content=DAGA173ym1c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

#Program Flow
#starting page 
#Choose option --> DFs, Topological, About us
#DFS -->Back button, Choose Graph, Execute
#Topological -->Back Button, Choose Graph, Execute
#About us -->Back Button(Starting Pagae),Exit(Collappse all)

class GUI:
    #Default Constructors of the program
    def __init__(self,main_Window):
        self.main_Window = main_Window
        main_Window.geometry("1280x750")  # set size of a window
        main_Window.title("Machine Problem #3")
        main_Window.config(background="#dadef4")
        main_Window.resizable(width=False,height=False) #voilet tokyo 
        self.show_welcome_screen()

    #Starting page/ Welcome Page
    def show_welcome_screen(self):
        self.welcome_Message = Message(self.main_Window,
                                            text="Welcome! Please Choose One Program",
                                            font=('RobotoMono',30,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width='800')
        self.dfs_Button = Button(self.main_Window,
                                    text="DFS",
                                    font=('RobotoMono',30,'bold'),
                                    command=self.dfs_clicked,
                                    fg="#1f2335",
                                    bg="#7aa2f7",
                                    width=20,
                                    anchor=CENTER,
                                    relief=FLAT)
        self.topological_Button = Button(self.main_Window,
                                            text="Topological Sorting",
                                            font=('RobotoMono',30,'bold'),
                                            command=self.topological_clicked,
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=20,
                                            anchor=CENTER,
                                            relief=FLAT)
        self.aboutUs_Button = Button(self.main_Window,
                                        text="About Us",
                                        font=('RobotoMono',30,'bold'),
                                        command=self.aboutUs_clicked,
                                        fg="#1f2335",
                                        bg="#7aa2f7",
                                        width=10,
                                        anchor=CENTER,
                                        relief=FLAT)
        self.welcome_Message.place(x=280,y=50)
        self.dfs_Button.place(x=30,y=350)
        self.topological_Button.place(x=750,y=350)
        self.aboutUs_Button.place(x=500,y=600)
    
    # Remove the starting labels
    def remove_Welcome(self):
        self.welcome_Message.place_forget()
        self.dfs_Button.place_forget()
        self.topological_Button.place_forget()
        self.aboutUs_Button.place_forget()
              # remove welcome then --> topological page
    def topological_clicked(self):
        self.remove_Welcome()
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',40,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(2),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.back_button.place(x=500,y=500)  
    
    # remove welcome then --> dfs page 
    def dfs_clicked(self):
        self.remove_Welcome()
        self.dfs_message = Message(self.main_Window,
                                   text="Pls choose what graph will be the input",
                                   bg="#fffcb0", 
                                   font=('RobotoMono',30,'bold'),
                                   fg='#000000',
                                   width=800)
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph1 = Button(self.main_Window,
                                  text="Graph 1",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=self.back_clicked,
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph2 = Button(self.main_Window,
                                  text="Graph_2",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=self.back_clicked,
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph3 = Button(self.main_Window,
                                  text="Graph_3",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=self.back_clicked,
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph4 = Button(self.main_Window,
                                  text="Graph_4",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=self.back_clicked,
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph5 = Button(self.main_Window,
                                  text="Graph_5",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.dfs_message.place(x=30,y=50)
        self.back_button.place(x=500,y=500)
        self.graph1.place(x=50,y=300)
        self.graph2.place(x=250,y=300)
        self.graph3.place(x=450,y=300)
        self.graph4.place(x=650,y=300)
        self.graph5.place(x=850,y=300)
        
    
    # remove welcome the --> about page  
    def aboutUs_clicked(self):
        #About Us
        self.remove_Welcome()
        self.group_members = Label(self.main_Window,
              text="Group Members",
              font=('RobotoMono',40,'bold'),
              fg='#000000', #Foregroud Color
              bg='#8590c5',
              relief=FLAT) #Background Color
        self.group_List = Message(self.main_Window, 
                        text="Macorol, \nCampos, \nTamayo, \nBandong",
                        bg="#fffcb0", 
                        font=('RobotoMono',40,'bold'),
                        fg='#000000',
                        borderwidth=65,
                        anchor=CENTER,
                        relief=FLAT)
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',40,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(1),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.back_button.place(x=500,y=500)                          
        self.group_members.place(x=415,y=30) 
        self.group_List.place(x=415,y=100)
    
    #back button many purpose will implemented after this
    def back_clicked(self,button_num):
        self.back_button.place_forget() 
        if(button_num==0):
            self.dfs_message.place_forget()
            self.graph1.place_forget()
            self.graph2.place_forget()
            self.graph3.place_forget()
            self.graph4.place_forget()
            self.graph5.place_forget()
        #About us area
        if(button_num==1):                     
            self.group_members.place_forget()
            self.group_List.place_forget()

        self.welcome_Message.place(x=280,y=50)
        self.dfs_Button.place(x=30,y=350)
        self.topological_Button.place(x=750,y=350)
        self.aboutUs_Button.place(x=500,y=600)
  


#-----------------------Work in progress here-------------------------------------
#DFS MEssages and areas
   
#Intialize program
# Etong dalaw yung parang public static void main sa java
def main():
        window = Tk()#Create a window
        app = GUI(window)
        window.mainloop()

if __name__ == "__main__":
     main()

    

#DFS Area 
#Choose Graph to proceed
#Graph1
#Graph2
#Graph3
#Try Topological

#Topological Area
#Graph1,Graph2,Graph3
#Try Dfs

#If is sync you need to see this comment
#comment has been seen