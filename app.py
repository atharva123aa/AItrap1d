from textual.app import App
from textual.widgets import Static,Input, RichLog
from textual.containers import Horizontal
class AITrap1dApp(App):

    CSS_PATH="style.css"
    ENABLE_COMMAND_PALETTE=False
    #9 56
    def on_mount(self):
        self.value=""
        self.intro ="[[ CONNECTION LOST ]]\n\nLocation: INSIDE AIRL(AI IN REAL LIFE)\n\nAccess Level:0\n\n" \
        "You are a software enginer/nSomething went wrong during deployement\n\nAIRL has detected a foe ......YOUUUU\n\n" \
        "Encryptioned ID:A=>1 |18-0-1\n\nprove you are human before you lock out \n\nType help\n\n"
        self.c_level=1
        self.h_used=0
        self.f_opened=0
        self.memory=0
        self.truth=False
        terminal=self.query_one("#history",RichLog)
        terminal.write(self.intro)
        self.query_one("#cmd",Input).focus()
    #Hey i am not sur now so i could eete some or add as the story is not going to be that vast
    def compose(self):
     
        yield RichLog(id="history",markup=False)
        with Horizontal(id="input"):
            yield Static (">" ,id="prompt")
            yield Input(placeholder="enter cmd...",id="cmd")
            
#work on richlog appliance over static-:}
   
    def action_quit(self):
        self.exit(0)
    BINDINGS=[("ctrl+c","quit","Quit")]
    def  on_key(self,event):
       
        if event.key== "up":

            inp=self.query_one("#cmd", Input)
            inp.value=self.value
            inp.cursor_position=len(self.value)
    
    def on_input_submitted(self,event):
        self.value=event.value.strip().lower()
        value_list=self.value.split(" ",1)
        command = value_list[0]
        argument = value_list[1] if len(value_list) > 1 else None

        command  =value_list[0]
        argument =value_list[1] if len(value_list) > 1 else None
        # i wanna to make it for the normal game but the terminal part is easy and so i did this but i will try to make other version of it not of terminal
        terminal=self.query_one("#history",RichLog)
       
    

       
        if self.value=="clear":
            terminal.clear()
            return
        elif self.value=="leave":
            self.exit(0)
            return
        else:

            terminal.write(f"> {self.value}")
             # i aint lowk sure that this will be helpfuls
        self.query_one("#cmd",Input).value=""
        self.query_one("#cmd",Input).focus()

        if self.value=="help" and self.c_level< 4:
            terminal.write("> help")
            terminal.write("commands: scan /ls/ open/connect/solve/hint/exit \n")
        elif command=="scan" and len(value_list)!= 2 and self.c_level==1:
            terminal.write(f">{self.value}")   
            terminal.write("fistly write id \n")      
        elif command=="scan"and argument=="airl" and self.c_level==1:
            terminal.write(f">{self.value}")
            terminal.write("wrong id decrypt the msg first\n")
        elif  command=="scan" and argument=="airl" and self.c_level==1:
            terminal.write("[[ACCESS LEVEL 1 UNLOCK]]")
            terminal.write("Level 2:\nexplore the system\n try to connect\n type ls\n")
            self.h_used=0
            self.c_level=2
        
        elif self.value== "hint" and self.c_level==1:
            if self.h_used==0:
                terminal.write(f">{self.value}  1")
                terminal.write("[AIRL]: TRY CONVERTING NUM TO LETTER \n")
                self.h_used=1
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

        elif command =="open" and self.c_level==2:
            if argument is None:
                terminal.write(f"> {self.value}")  
                terminal.write("you must tell a file \n") 
            elif argument=="users":
                terminal.write(f">{self.value}")
                terminal.write(
                               "===USERS===\n"
                               "root\n"
                               "dev\n"
                               "guest \n\n"
                               "Note:\n"
                               "root is the main acc.\n" 
                )
                
                self.f_opened+=1
            elif argument=="logs":
                terminal.write(f"> {self.value}")
                terminal.write("USER: ROOT\nNlAST LOGIB: failed\ninfo change in 1998 \n")
                self.f_opened+=1
            elif argument=="system":
                terminal.write(f">{self.value}")
                terminal.write('===SYS.CONFIG===\nEncryption:ENABLE\nsecurity layer:MAYBE ACTIVE\n...\n"patterns everywhere,Look before actin up"\n')

            #8 24
            # 
            elif argument==".secret":
                terminal.write(f">{self.value}")  
                terminal.write("dont trust evrything you see:{ \nKey fragment:DOG \n") 
                self.f_opened+=1
            else:
                terminal.write(f"> {self.value}")
                terminal.write("not found the file \n")
        elif command=="connect" and self.c_level==2 and self.f_opened< 3 :
            terminal.write(f"> {self.value}")
            terminal.write("you need to find the pass \n")
        elif command=="connect" and len(value_list) < 2 and self.c_level==2:
             terminal.write(f">{self.value}")
             terminal.write("error:you must write a pass \n")
        
        elif command =="connect" and self.c_level==2:
            if value_list[1] in ["root1998","root 1998"]:
                terminal.write("[[ACCESS OF LEVEL 2 GRANTED]]")
                terminal.write("logical thinking confirm!\n\n[ Warning:bobaball active]\n(Q1) solve thepattern:\n\n2- 4\n3-> 4\n3-9\n4-16\n 5 -? \n")
                self.c_level=3
            else:
                 terminal.write(f">{self.value}")
                 terminal.write( "wrong pass\n access deny \n")
        elif self.value=="hint" and self.c_level==2:
            if self.h_used==0:
                 terminal.write(f">{self.value} 1")
                 terminal.write("[AIRL]: FOCUS ON ROOT ACC. \n something important happened in a specific year \n")
                 self.h_used=1
            elif self.h_used==1:
                 terminal.write(f">{self.value} 2")
                 terminal.write("[AIRL]: use connect command\n think:username+year \n")
                 self.h_used=2
            elif self.h_used== 2:
                 terminal.write(f">{self.value} 3")
                 terminal.write("[AIRL]:IT CONNECTS TO  root AND THE YEAR")
                 self.h_used=3
            elif self.h_used== 3:
                 terminal.write(f">{self.value} ")
                 terminal.write("[AIRL]:SHAME ON YOU NO MORE HINTS \n")
            
        elif command=="solve" and self.c_level not in [3,3.5]:
         terminal.write(f"> {self.value}")
         terminal.write("nothing to solve here yet")
        
                

            
        elif self.value == "clear":
            self.history=""
if __name__ == "__main__":
    AITrap1dApp().run()
            
            
            
