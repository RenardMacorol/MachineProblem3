from tkinter import * #import tkinter
from Graph import Graph

#NOTE!! Plss for Development GUI Refer in this link 
# https://www.canva.com/design/DAGA173ym1c/d_z45DCcBHGC4QYWXCA_Fg/edit?utm_content=DAGA173ym1c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

#Program Flow
#starting page 
#Choose option --> DFs, Topological, About us
#DFS -->Back button, Choose Graph, Execute
#Topological -->Back Button, Choose Graph, Execute
#About us -->Back Button(Starting Pagae),Exit(Collappse all)
outputText= 30
outputWidth = 1800
#Output pos
outputX=100
outputY=200
graph1placeX = 50
graph1placeY = 300
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
        self.graph_message = Message(self.main_Window,
                                   text="Pls choose what graph will be the input",
                                   bg="#fffcb0", 
                                   font=('RobotoMono',30,'bold'),
                                   fg='#000000',
                                   width=800)
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
        self.graph1 = Button(self.main_Window,
                                  text="Graph 1",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  command=lambda:self.graph1_clicked(1),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph2 = Button(self.main_Window,
                                  text="Graph 2",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  command=lambda:self.graph2_clicked(1),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph3 = Button(self.main_Window,
                                  text="Graph 3",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  command=lambda:self.graph3_clicked(1),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph4 = Button(self.main_Window,
                                  text="Graph 4",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  command=lambda:self.graph4_clicked(1),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph5 = Button(self.main_Window,
                                  text="Graph 5",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',                       
                                  command=lambda: self.graph5_clicked(1),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph_message.place(x=30,y=50)
        self.back_button.place(x=500,y=500)
        self.graph1.place(x=graph1placeX,y=graph1placeY)
        self.graph2.place(x=graph1placeX*5.5,y=graph1placeY)
        self.graph3.place(x=graph1placeX*10,y=graph1placeY)
        self.graph4.place(x=graph1placeX*15,y=graph1placeY)
        self.graph5.place(x=graph1placeX*20,y=graph1placeY)
    # remove welcome then --> dfs page 
    def dfs_clicked(self):
        self.remove_Welcome()
        self.graph_message = Message(self.main_Window,
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
                                  command=lambda:self.graph1_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph2 = Button(self.main_Window,
                                  text="Graph 2",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda:self.graph2_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph3 = Button(self.main_Window,
                                  text="Graph 3",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda:self.graph3_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph4 = Button(self.main_Window,
                                  text="Graph 4",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda:self.graph4_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph5 = Button(self.main_Window,
                                  text="Graph 5",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.graph5_clicked(0),
                                  anchor=CENTER,
                                  relief=FLAT)
        self.graph_message.place(x=30,y=50)
        self.back_button.place(x=500,y=500)
        self.graph1.place(x=graph1placeX,y=graph1placeY)
        self.graph2.place(x=graph1placeX*5.5,y=graph1placeY)
        self.graph3.place(x=graph1placeX*10,y=graph1placeY)
        self.graph4.place(x=graph1placeX*15,y=graph1placeY)
        self.graph5.place(x=graph1placeX*20,y=graph1placeY)
   
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
                        text="Macorol,Renard B. , \nCampos,Vince D.",
                        bg="#dadef4", 
                        font=('RobotoMono',40,'bold'),
                        fg='#000000',
                        borderwidth=10,
                        width=1000,
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
        self.back_button.place(x=500,y=600)                          
        self.group_members.place(x=415,y=30) 
        self.group_List.place(x=300,y=150)
   
    def remove_option(self):
        self.graph_message.place_forget()
        self.graph1.place_forget()
        self.graph2.place_forget()
        self.graph3.place_forget()
        self.graph4.place_forget()
        self.graph5.place_forget()
        self.back_button.place_forget()
    #back button many purpose will implemented after this
    def back_clicked(self,button_num):
        self.back_button.place_forget() 
        if(button_num==0):
           self.remove_option()
        #About us area
        if(button_num==1):                     
            self.group_members.place_forget()
            self.group_List.place_forget()
        if(button_num==2):
           self.remove_option()
        if(button_num==3):
            self.output_Message.place_forget()
        self.welcome_Message.place(x=280,y=50)
        self.dfs_Button.place(x=30,y=350)
        self.topological_Button.place(x=750,y=350)
        self.aboutUs_Button.place(x=500,y=600)
    
    
    #dfe ==0 topo ==1
    def graph1_clicked(self,type):
        self.remove_option()
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(3),
                                  anchor=CENTER,
                                  relief=FLAT)
             
        self.back_button.place(x=500,y=500)
        if(type==0):
             output= "DFS traversal starting from vertex 'A':", g1.dfs_traversal(0)
             self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
            
             self.output_Message.place(x=outputX,y=outputY)
        if(type==1):
            output = "Topolocial Sort", g1.topological_sort()
            self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
            self.output_Message.place(x=outputX,y=outputY)
    def graph2_clicked(self,type):
        self.remove_option()
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(3),
                                  anchor=CENTER,
                                  relief=FLAT)
             
        self.back_button.place(x=500,y=500)
        if(type==0):
             output= "DFS traversal starting from vertex 'A':", g2.dfs_traversal(0)
             self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
             self.output_Message.place(x=outputX,y=outputY)
        if(type==1):
            output = "Topolocial Sort", g2.topological_sort()
            self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
            self.output_Message.place(x=outputX,y=outputY)
    def graph3_clicked(self,type):
        self.remove_option()
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(3),
                                  anchor=CENTER,
                                  relief=FLAT)
             
        self.back_button.place(x=500,y=500)
        if(type==0):
             output= "DFS traversal starting from vertex 'A':", g3.dfs_traversal(0)
             self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
             self.output_Message.place(x=outputX,y=outputY)
        if(type==1):
            output = "Topolocial Sort", g3.topological_sort()
            self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
            self.output_Message.place(x=outputX,y=outputY)     
    def graph4_clicked(self,type):
        self.remove_option()
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(3),
                                  anchor=CENTER,
                                  relief=FLAT)
             
        self.back_button.place(x=500,y=500)
        if type == 0:
            output = "DFS traversal starting from vertex 'A': " + str(g4.dfs_traversal(0))
            outputText = len(output)
            outputWidth = outputText * 10  # Adjust the width as needed
            outputX = 30
            outputY = 50
        elif type == 1:
            output = "Topological Sort: " + str(g4.topological_sort())
            outputText = len(output)
            outputWidth = outputText * 15  # Adjust the width as needed
            outputX = 30
            outputY = 50

        self.output_Message = Message(self.main_Window,
                                  text=output,
                                  font=('RobotoMono', outputText, 'bold'),
                                  fg="#1f2335",
                                  bg="#7aa2f7",
                                  width=outputWidth)
        self.output_Message.place(x=outputX, y=outputY)
    def graph5_clicked(self,type):
        self.remove_option()
        self.back_button = Button(self.main_Window,
                                  text="Back",
                                  bg="#fffcb0", 
                                  font=('RobotoMono',30,'bold'),
                                  fg='#000000',
                                  borderwidth=10,
                                  command=lambda: self.back_clicked(3),
                                  anchor=CENTER,
                                  relief=FLAT)
             
        self.back_button.place(x=500,y=500)
        if(type==0):
             output= "DFS traversal starting from vertex 'A':", g5.dfs_traversal(0)
             self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
             self.output_Message.place(x=outputX,y=outputY)
        if(type==1):
            output = "Topolocial Sort", g5.topological_sort()
            self.output_Message = Message(self.main_Window,
                                            text=output,
                                            font=('RobotoMono',outputText,'bold'),
                                            fg="#1f2335",
                                            bg="#7aa2f7",
                                            width=outputWidth)
            self.output_Message.place(x=outputX,y=outputY)

  


#-----------------------Work in progress here-------------------------------------
#DFS MEssages and areas
   
#Intialize program
# Etong dalaw yung parang public static void main sa java
def main():
        window = Tk()#Create a window
        app = GUI(window)
        window.mainloop()
#Note! All of this are dag
print("Normal DAG")
g1 = Graph(7)
g1.addVertex("A")#0
g1.addVertex("B")#1
g1.addVertex("C")#2
g1.addVertex("D")#3
g1.addVertex("E")#4
g1.addVertex("F")#5
g1.addVertex("G")#6

g1.addEdge(0,1)
g1.addEdge(0,2)
g1.addEdge(1,3)
g1.addEdge(2,3)
g1.addEdge(3,4)
g1.addEdge(4,5)
g1.addEdge(4,6)
g1.addEdge(5,6)

print(g1.__str__())

print("Multiple Root DAG")
g2 = Graph(5)
g2.addVertex("A")#0
g2.addVertex("B")#1
g2.addVertex("C")#2
g2.addVertex("D")#3
g2.addVertex("E")#4

g2.addEdge(0,1)
g2.addEdge(1,2)
g2.addEdge(2,3)
g2.addEdge(3,4)
g2.addEdge(0,3)

print(g2.__str__())

print("DAG with Cycle")
g3 = Graph(5)
g3.addVertex("A")#0
g3.addVertex("B")#1
g3.addVertex("C")#2
g3.addVertex("D")#3
g3.addVertex("E")#4

g3.addEdge(0,1)
g3.addEdge(1,2)
g3.addEdge(2,3)
g3.addEdge(3,4)
g3.addEdge(4,0) # This edge creates a cycle

print(g3.__str__())

print("DAG with one Vertex")
g4 = Graph(1)
g4.addVertex("A")#0

print(g4.__str__())

print("DAG Disconnected")
g5 = Graph(7)
g5.addVertex("A")#0
g5.addVertex("B")#1
g5.addVertex("C")#2
g5.addVertex("D")#3
g5.addVertex("E")#4
g5.addVertex("F")#5
g5.addVertex("G")#6

g5.addEdge(0,1)
g5.addEdge(1,2)
g5.addEdge(2,3)
g5.addEdge(3,4)
g5.addEdge(4,5)
g5.addEdge(5,6)

# Disconnected component
g5.addEdge(0,6)

print(g5.__str__())

# Example usage of the dfs method



if __name__ == "__main__":
     main()

    

