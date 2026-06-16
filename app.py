from textual.app import App
from textual.widgets import Static,Input
from textual.containers import Horizontal
class AITrap1dApp(App):

    CSS_PATH="style.css"
    #9 56
    def on_mount(self):
        self.value=""
        self.log  ="[[ CONNECTION LOST ]]\n\nLocation: INSIDE AIRL(AI IN REAL LIFE)\n\nAccess Level:0\n\n" \
        "You are a software enginer/nSomething went wrong during deployement\n\n\AIRL has detected a foe ......YOUUUU\n\n" \
        "Encryptioned ID:A=>1 |18-0-1\n\nprove you are human before you lock out \n\nType help\n\n"
        self.c_level=1
        self.h_used=0
        self.f_opened=0
        self.memry=0
        self.truth=False
    #Hey i am not sur now so i could eete some or add as the story is not going to be that vast
    def compose(self):
        self.input=Input(placeholder="enter cmd...")
        
        
