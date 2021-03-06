from tkinter import *
from PIL import ImageTk, Image

from kComponents import prettyButton


class LoginScreen(Frame):
    def __init__(self, master, startCommand, registerFunc, landingPage):
        Frame.__init__(self, master, bg="#FFFFFF")
        self.startCommand = startCommand
        self.registerFunc = registerFunc
        self.landingPage = landingPage

        self.logo = ImageTk.PhotoImage(Image.open("image.png").resize((250, 250), Image.ANTIALIAS))
        self.font = "Roboto"

        self.logoLabel = Label(self, image=self.logo, bg="#FFFFFF")
        self.logoLabel.pack()

        self.userText = Label(self, text="Username", font=(self.font, 16),bg="#FFFFFF")
        self.userText.pack()

        self.username = Entry(self)
        self.username.pack()

        self.passText = Label(self, text="Password", font=(self.font, 16),bg="#FFFFFF")
        self.passText.pack()

        self.password = Entry(self, show="*")
        self.password.pack()

        self.returnText = Label(self, text="", font=(self.font, 8), bg="#FFFFFF")
        self.returnText.pack()

        self.loginButton = prettyButton(self, text="Login", font=(self.font, 12), command=self.login)
        self.loginButton.pack()

        self.block = Label(self, text="", font=(self.font, 2), bg="#FFFFFF")
        self.block.pack()

        self.signupButton = prettyButton(self, text="Register", font=(self.font, 12), command=self.register)
        self.signupButton.pack()

        self.block2 = Label(self, text="", font=(self.font, 2), bg="#FFFFFF")
        self.block2.pack()

    def register(self):
        self.returnText.configure(text="Registering...", fg="blue")
        self.registerFunc(self.username.get(), self.password.get(), self.handleRegister)

    def login(self):
        self.returnText.configure(text="Authenticating...", fg="blue")
        self.startCommand(self.username.get(), self.password.get(), self.handleLogin)

    def handleLogin(self, r):
        code = r.status_code

        text = ""
        color = ""
        if(code == 200):
            text = "Login Sucessful!"
            color = "green"
            self.landingPage.tkraise()
        else:
            text = r.text
            color = "red"

        self.returnText.configure(text=text, fg=color)

    def handleRegister(self, r):
        code = r.status_code

        text = ""
        color = ""
        if (code == 200):
            text = "Register Sucessful!"
            color = "green"
        else:
            text = r.text
            color = "red"

        self.returnText.configure(text=text, fg=color)