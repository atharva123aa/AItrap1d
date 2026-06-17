from textual.app import App
from textual.widgets import Static,Input, Richlog
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
        self.memory=0
        self.truth=False
    #Hey i am not sur now so i could eete some or add as the story is not going to be that vast
    def compose(self):
        self.input=Input(placeholder="enter cmd...")
        yield Static ("[[ CONNECTION LOCKED]]\n\Location: INSIDE AIRL (AI IN REAL LIFE))\n\nAccess Level:0\n\n" \
                      "You are a software engineer \nSomething went wrong during deployement\n\n\AIRL has detected a foe ......YOUUUU\n\n" \
                      "Encryptioned ID:A=> 1 |18-9-1\n\bprove you are human before you lock out \n\n",id="history",markup=False)
        with Horizontal(id="input"):
            yield Richlog(">" ,id="prompt")
            yield self.input
#work on richlog appliance over static-:}
    def _on_key(self,event):
        if event.key== "up":

            self.input.value== self.value
            self.input.cursor_position=len(self.value)
    
    def on_input_submit(self,event):
        self.value=event.value.strip().lower()
        value_list=self.value.split("",1)
        command  =value_list[0]
        argument =value_list[1] if len(value_list) > 1 else None
        # i wanna to make it for the normal game but the terminal part is easy and so i did this but i will try to make other version of it not of terminal
        terminal=self.query_one("#history",Richlog)
        if self.value=="clear":
            terminal.clear()
        elif self.value=="leave":
            self.leave()
            return
        else:
            terminal.write(f"> {self.value}")
            terminal.write("Unknown text,type help\n")
        self.input.value=""


        if self.value=="help" and self.c_level< 4:
            terminal.write("> help")
            terminal.write("commands: scan /ls/ open/connect/solve/hint/exit \n")
        elif command=="scan" and len(value_list)!= 2 and self.c_level==1:
            terminal.write(f">{self.value}")   
            terminal.write("fistly write id \n")      
        elif command=="scan"and value_list[1]=="airl" and self.c_level==1:
            terminal.write(f">{self.value}")
            terminal.write("wrong id decrypt the msg first\n")
        elif  command=="scan" and value_list[1]=="airl" and self.c_level==1:
            terminal.write("[[ACCESS LEVEL 1 UUNLOCK]]")
            terminal.write("Level 2:\nexplore the system\n try to connect\n type ls\n")
            self.h_used=0
            self.c_level=2
        
        elif self.value== "hint" and self.c_level==1:
            if self.h_used==0:
                terminal.write(f">{self.value}  1")
                terminal.write("[AIRL]: TRY CONVERTING NUM TO LETTER \n")
            elif self.h_used==1:
                terminal.write(f"> {self.value} 2")
                terminal.write("[AIRL]: EXAMPLE:\n A=1\n B=2\n D=4")
                self.h_used=2


            elif   self.h_used==2:
                 terminal.write(f"> {self.value} 3")
                 terminal.write("[AIRL]:NO MORE HINTS\n")
        elif self.value=="ls" and self.c_level==2:
            terminal.write(f"> {self.value}")
            terminal.write("files:\nusers\nlogs\nsystem\n.secret \n")
