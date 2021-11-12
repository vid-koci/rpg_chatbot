from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

import backend
 
# GUI class for the chat
class GUI:
    # constructor method
    def __init__(self, chatbot):
        self.chatbot = chatbot
       
        # chat window which is currently hidden
        self.Window = Tk()
        self.Window.withdraw()

         
        # login window
        self.login = Toplevel()
        # set the title
        self.login.title("Login")
        self.login.resizable(width = False,
                             height = False)
        self.login.configure(width = 800,
                             height = 600)
        # create a Label
        self.pls = Label(self.login,
                       text = "Add a player character",
                       justify = CENTER,
                       font = font.Font(root=self.login,family="Helvetica",size=14,weight="bold")) #"Helvetica 14 bold")
         
        self.pls.place(relheight = 0.05,
                       relx = 0.2,
                       rely = 0.07)
        # create a Label
        self.labelName = Label(self.login,
                               text = "Character: ",
                               font = font.Font(root=self.login,family="Helvetica",size=12,weight="bold"))
         
        self.labelName.place(relheight = 0.05,
                             relx = 0.03,
                             rely = 0.2)
         
        # create a entry box for
        # tying the message
        self.entryName = Entry(self.login,
                             font = font.Font(root=self.login,family="Helvetica",size=12,weight="bold"))
         
        self.entryName.place(relwidth = 0.3,
                             relheight = 0.05,
                             relx = 0.15, #0.35,
                             rely = 0.2)

        self.entryDesc = Entry(self.login,
                             font = font.Font(root=self.login,family="Helvetica",size=12,weight="bold"))

        self.entryDesc.place(relwidth = 0.5,
                             relheight = 0.05,
                             relx = 0.45, #0.35,
                             rely = 0.2)

        self.add_player = Button(self.login,
                         text = "Add player",
                         font = font.Font(root = self.login, family="Helvetica",size=14,weight="bold"),
                         command = lambda: self.addPlayer(self.entryName.get(),self.entryDesc.get()))
         
        self.add_player.place(relx = 0.4,
                      rely = 0.3)
         
        # set the focus of the cursor
        self.entryName.focus()
         
        #record of the entered info
        self.players = []
        self.player_labels = []

        # create a Continue Button
        # along with action
        self.go_armor = Button(self.login,
                         text = "Animated Armor",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.entryName.get(),dialogue = "armor"))
        self.go_glinidril = Button(self.login,
                         text = "Glinidril",
                         font = "Helvetica 14 bold",
                         command = lambda: self.goAhead(self.entryName.get(),dialogue = "Glinidril"))
         
        self.go_armor.place(relx = 0.25,
                      rely = 0.4)
        self.go_glinidril.place(relx = 0.5,
                      rely = 0.4)
        self.Window.mainloop()

    def addPlayer(self, name, desc):
        if len(self.players)>=5:
            messagebox.showerror(title="Max number of characters reached", message="Unfortunately, the program currently does not support using more than 5 characters.")
            return
        new_player_label = Label(self.login,
                            text = name+": "+desc,
                               font = "Helvetica 12")
         
        new_player_label.place(relheight = 0.05,
                             relx = 0.1,
                             rely = 0.35+len(self.players)*0.05)
        self.players.append((name,desc))
        self.player_labels.append(new_player_label)
        self.entryName.delete(0, 'end')
        self.entryDesc.delete(0, 'end')
         
        self.go_armor.place(relx = 0.25,
                      rely = 0.35+len(self.players)*0.05)
        self.go_glinidril.place(relx = 0.5,
                      rely = 0.35+len(self.players)*0.05)

    def goAhead(self, name, dialogue="armor"):
        if len(self.players)==0:
            messagebox.showerror(title="No characters added", message="Add at least one character to use the chatbot.")
            return
        self.login.destroy()
        self.layout(dialogue)
 
    # The main layout of the chat
    def layout(self,name):
       
        self.name = name
        # to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 600,
                              height = 800,
                              bg = "#17202A")
        self.labelHead = Label(self.Window,
                             bg = "#17202A",
                              fg = "#EAECEE",
                              text = self.name ,
                               font = "Helvetica 13 bold",
                               pady = 5)
         
        self.labelHead.place(relwidth = 1)
        self.line = Label(self.Window,
                          width = 600,
                          bg = "#ABB2B9")
         
        self.line.place(relwidth = 1,
                        rely = 0.04,
                        relheight = 0.006)
         
        self.textCons = Text(self.Window,
                             width = 20,
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 12",
                             padx = 5,
                             pady = 5)
         
        self.textCons.place(relheight = 0.745,
                            relwidth = 1,
                            rely = 0.05)
         
        self.labelBottom = Label(self.Window,
                                 bg = "#ABB2B9",
                                 height = 120)
         
        self.labelBottom.place(relwidth = 1,
                               rely = 0.8)

        self.labelCharacter = Label(self.labelBottom,
                               text = "Character: ",
                               font = font.Font(root = self.labelBottom,family="Helvetica",size=10,weight="bold"))
         
        self.labelCharacter.place(relheight = 0.03,
                             relx = 0.01,
                             rely = 0.008)
 
        self.labelSays = Label(self.labelBottom,
                               text = "Says: ",
                               font = font.Font(root = self.labelBottom,family="Helvetica",size=10,weight="bold"))
         
        self.labelSays.place(relheight = 0.03,
                             relx = 0.01,
                             rely = 0.038)
  
        self.labelAction = Label(self.labelBottom,
                               text = "Action: ",
                               font = font.Font(root = self.labelBottom,family="Helvetica",size=10,weight="bold"))
         
        self.labelAction.place(relheight = 0.03,
                             relx = 0.01,
                             rely = 0.068)
        
        
        #entries

        self.entryName = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
         
        self.entryName.place(relwidth = 0.6,
                            relheight = 0.03,
                            rely = 0.008,
                            relx = 0.151)

        self.entryName.focus()

        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
         
        self.entryMsg.place(relwidth = 0.6,
                            relheight = 0.03,
                            rely = 0.038,
                            relx = 0.151)
         
        self.entryAction = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")

        self.entryAction.place(relwidth = 0.6,
                               relheight = 0.03,
                               rely = 0.068,
                               relx = 0.151)
         
        # create Send Buttons
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryName.get(),self.entryMsg.get(),self.entryAction.get()))
         
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.045,
                             relwidth = 0.22)

        self.buttonAI = Button(self.labelBottom,
                                text = "AI response",
                                font = "Helvetica 10 bold",
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.AIButton())
         
        self.buttonAI.place(relx = 0.77,
                             rely = 0.053,
                             relheight = 0.045,
                             relwidth = 0.22)
         
        self.textCons.config(cursor = "arrow")
         
        # create a scroll bar
        scrollbar = Scrollbar(self.textCons)
         
        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight = 1,
                        relx = 0.974)
         
        scrollbar.config(command = self.textCons.yview)
         
        self.textCons.config(state = DISABLED)

        #initialize the chatbot and display the prompt
        prompt = self.chatbot.initialize(self.players,self.name)
        self.receive(prompt+self.chatbot.query(""))#AI talks first - hence the the empty query
        self.text_since_last_query = ""
 
    # function to basically start the thread for sending messages
    def sendButton(self, name, msg, action):
        self.textCons.config(state = DISABLED)
        self.entryName.delete(0, END)
        self.entryMsg.delete(0, END)
        self.entryAction.delete(0, END)
        if msg=="":
            user_input=f"{name} {action}"
        elif action=="":
            user_input=f"{name} says \"{msg}\""
        else: 
            user_input=f"{name} says \"{msg}\" and {action}"
        self.receive(user_input)
        self.text_since_last_query+=" "+user_input
 
    def AIButton(self):
        self.textCons.config(state = DISABLED)
        message = self.chatbot.query(self.text_since_last_query)
        self.text_since_last_query = ""
        self.receive(message)

    # function to receive messages
    def receive(self, message):
        self.textCons.config(state = NORMAL)
        self.textCons.insert(END,
                             message+"\n\n")
         
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)

# create a GUI class object
chatbot = backend.chatbot()
g = GUI(chatbot)
