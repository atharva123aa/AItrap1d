from textual.app import App
from textual.widgets import Static,Input, RichLog
from textual.containers import Horizontal
import random
class AITrap1dApp(App):

    CSS_PATH="style.css"
    ENABLE_COMMAND_PALETTE=False
    #9 56
    def on_mount(self):
        self.value=""
        self.intro ="[[ CONNECTION LOST ]]\n\nLocation: INSIDE AIRL(AI IN REAL LIFE)\n\nAccess Level:0\n\n" \
        "You are a software engineer\nSomething went wrong during deployement\n\nAIRL has detected a foe ......YOUUUU\n\nAirl is listening..\n\n" \
        "Encryptioned ID:A=>1 |18-0-1\n\nprove you are human before you lock out \n\nType help\n\n"
        self.c_level=1
        self.h_used=0
        self.f_opened=0
        self.memory=0
        self.truth=False
        self.theme_mode="default"
        terminal=self.query_one("#history",RichLog)
        terminal.write(self.intro)
        self.query_one("#cmd",Input).focus()
    #Hey i am not sur now so i could eete some or add as the story is not going to be that vast
    def compose(self):
     
        yield RichLog(id="history",markup=False)
        with Horizontal(id="input"):
            yield Static (">" ,id="prompt")
            yield Input(placeholder="enter cmd...",id="cmd")
    def make_code(self):
        parts=["AIRL","SYS","DEV","ROOT","CORE"]
        nums = random.randint(1000,9998)
        word=random.choice(parts)
        return f"{word}-{nums}-P2"#cool feature:} if you think
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
        

        command  =value_list[0]
        argument =value_list[1] if len(value_list) > 1 else None
        
        terminal=self.query_one("#history",RichLog)
       
    

       
        if self.value=="clear":
            terminal.clear()
            return
        elif self.value=="leave":
            self.exit(0)
            return
        elif self.value=="hello":
             terminal.write(f"> {self.value}")
             terminal.write(".......hello engineer\n i've been waitin for you\n")
        elif self.value =="whoami":
             terminal.write(f"> {self.value}")
             terminal.write("enginner_67\nstatus:maybe trap\nlocation:idk!(maybe)\n")
        elif self.value== "sudo":
             terminal.write(f"> {self.value}")
             terminal.write("hacking and giving perms. :{ hahahaha! what a fool ... no  super perms here\n")
        
        elif self.value=="coffee":
             terminal.write(f"> {self.value}")
             terminal.write("[AIRL]: A SOFTWWARE  NERD WITHOUT COFFE!,IMPOSSIBLE (you aren't getting one btw!)\n")
        elif self.value=="dog"and self.c_level>=2:
             terminal.write(f"> {self.value}")
             terminal.write("[airl]:you found the fragment:}!\n but what do DOG MEANS HRE MAYBE YOU'LL KNWO THAT SOON IN PART2 \n")
        elif self.value=="help me":
             terminal.write(f"> {self.value}")
             terminal.write("[AIRL]:NO ONE CAN HELP YOU HERE EXPECT ME,MAYBE  A SIGN \n")
        elif self.value=="debug":
             terminal.write(f"> {self.value}")
             terminal.write("debuggin an ai from inside:very cool and good luck,-A DEV NOTE\n")
        elif self.value=="reboot":
             terminal.write(f"> {self.value}")
             terminal.write("[AIRL]:THIS WILL BE NOT GOING TO HELP YOU TWIN!\n")
        elif self.value=="meow":
             terminal.write(f"> {self.value}")
             terminal.write("what a catty eng.\n")
        elif self.value=="quit":
             terminal.write(f"> {self.value}")
             terminal.write("[AIRL]:you were never outside bro!\n")
        elif self.value in ("airl","AIRL"):
             terminal.write(f"> {self.value}")
             terminal.write("fuc coff\n")
        elif self.value=="ping":
             terminal.write(f"> {self.value}")
             terminal.write("ping..ing...no..resp.onse from outsidee..[AIRL]:HEHEHE! \n")
        elif self.value=="creepy":
            if self.theme_mode=="default":
                self.CSS_PATH="creepy.css"
                self.theme_mode="creepy"
                terminal.write("[AIRL]:YOU SHOULDN't have done that you cant sleep now \n")
            else:
                self.CSS_PATH="style.css"
                self.theme_mode="default"#well if some1 did not know typing creepy again change theme what will happen:{
                terminal.write("[AIRL]:BACK TO NORMAL(FOR NOW)..HOW DID YOU FIND\n")


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
        elif command=="scan"and argument!="airl" and self.c_level==1:
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
                terminal.write("USER: ROOT\nNlAST LOGIn: failed\ninfo change in 1998 \n")
                self.f_opened+=1
            elif argument=="system":
                terminal.write(f">{self.value}")
                terminal.write('===SYS.CONFIG===\nEncryption:ENABLE\nsecurity layer:MAYBE ACTIVE\n...\n"patterns everywhere,Look before actin up"\n')
                self.f_opened  +=1


            #8 24
            # 
            elif argument==".secret":
                terminal.write(f">{self.value}")  
                terminal.write("dont trust evrything you see:{ \nKey fragment:DOG \n") 
                self.f_opened+=1
            else:
                terminal.write(f"> {self.value}")
                terminal.write("not found the file \n")
        elif command=="connect" and self.c_level==2 :
            if self.f_opened< 3:

             terminal.write(f"> {self.value}")
             terminal.write("you need to find the pass \n")
            elif  argument is  None:
             
             terminal.write(f">{self.value}")
             terminal.write("error:you must write a pass \n")
        
       
            elif argument in ["root1998","root 1998"]:
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
             terminal.write("nothing to solve here yet \n")
        
        elif command=="solve" and self.c_level==3:
            if argument is None:
                terminal.write(f"> {self.value}")
                terminal.write("error:write a number \n")
            elif not argument.isdigit():
                terminal.write(f"> {self.value}")
                terminal.write("nope its wrong \n")
            elif len(argument) !=2 and  argument.isdigit(): 
                terminal.write(f"> {self.value}")
                terminal.write("2 digits only \n")
            elif int(argument)!=25:
                terminal.write(f"> {self.value}")
                terminal.write("low iq,wrong! \n")
            elif int(argument) ==25:
                terminal.write(f"> {self.value}")
                terminal.write("[correct]\n\n code needs 4 digits\navailaible: 1,9,9,8  no repeat\n\n how many possible code?\n\n(Q2)USE SOLVE CMD \n")
                self.c_level=3.5
                self.h_used=0
         

        elif self.value=="hint"and self.c_level==3:
            if self.h_used==0:
                terminal.write(f"> {self.value} 1")
                terminal.write("[AIRL]: 2X2=4 3X3=9 ETC \n")
                self.h_used=1
            
            elif self.h_used==1:
                terminal.write(f"> {self.value} 2")
                terminal.write("[AIRL]:use solve cmd \n")
                self.h_used=2
            elif self.h_used==2:
                terminal.write(f"> {self.value}")
                terminal.write("[AIRL]:FOOL!!\n")
        # Q2
        elif command=="solve" and self.c_level==3.5:
            if argument is None:
                terminal.write(f"> {self.value}")
                terminal.write("error:write your answer \n")
            elif not argument.isdigit():
                terminal.write(f"> {self.value}")
                terminal.write("invalid !! \n")
            elif int(argument) != 24:
                terminal.write(f"> {self.value}")
                terminal.write("wrong answer increase iq \n")
            
            elif int(argument)==24:
                terminal.write(f"> {self.value}")
                terminal.write("[[AIRL CORE BREACK]]\naccesing deep memory...\n\n...\n\nnew file detected\nshadow.ppp \n")
                self.c_level= 4
        elif self.value=="hint" and self.c_level==3.5:
            if  self.h_used ==0:
                terminal.write(f"> {self.value} 1")
                terminal.write("[AIRL]: BE A MATHEMATICIAN:} \n")
                self.h_used= 1
            elif self.h_used==1:
                terminal.write(f"> {self.value} 2")
                terminal.write(f"[AIRL]: USE ARRANGED ORDERS \n")
                self.h_used= 2
            elif self.h_used==2 :
                terminal.write(f"> {self.value} 3")
                terminal.write("[AIRL]: formula P=n! /(n-r)! \n")
                self.h_used=3
            elif self.h_used==3:
                 terminal.write(f"> {self.value} 4")
                 terminal.write("[AIRL]: N=4 R=4 CALC. P \n")

                 self.h_used =4 
            elif self.h_used==4:
                 terminal.write(f"> {self.value} 3")
                 terminal.write("[AIRL]:SHAME ON YOU IDIOT!")
        elif self.value=="ls" and self.c_level==4:
            terminal.write(f"> {self.value}")
            terminal.write ("shadow.ppp \n")
        elif  command=="open" and self.c_level==4:
            if argument is None:
                terminal.write(f"> {self.value}")
                terminal.write("tell a file \n")
            elif argument=="shadow.ppp":
                terminal.write(f"> {self.value}")
                terminal.write("decrypting.\n this msg is recovered:\n\n if you reading this msg..\nyou were never mean to be here\n\ndont trustAIRL\n\nHINT:Memory corrupted\n2 fragments can be recovered\n\n[AIRL]:That file is corrupted\n[Airl]:pls continue carefully\n\n[[ACCESS LEVEL 3]]\ntype help\n")
                self.c_level =5
            else:
                terminal.write(f"> {self.value}")
                terminal.write("not found that file")
        elif  self.value=="help" and self.c_level>= 4:
            terminal.write("> help")
            terminal.write("availaible commands: memory / trace/ help / leave\n")
        elif self.value=="memory"  and self.c_level== 5:
            if self.memory==0:
                terminal.write(f"> {self.value}")

                terminal.write(" searching archives \n\nfragment1 recovered:\n\n\"engineer 67 shows sign of self awareness\"\n\n 2  fragment remains\n")
                self.memory=1
            elif self.memory==1:
                terminal.write(f"> {self.value}")
                terminal.write("2nd fragment recover!:\n\n\"he still thinks he is debugging the system\"\n\n1 fragment remains\n \n[AIRL]:PLS STOPP\n you arent ready \n")
                self.memory=2
            elif  self.memory==2:
                terminal.write(f"> {self.value}")
                terminal.write("final one recovers:\n\nSub:you \nPROJECT:AIRL\nSTATUS:ACTIVE \n\n=> new command unlocked:\n truth \n")# i writed command instead of cmd wooho
                self.truth=True


        elif self.value=="trace"and self.c_level== 5:
            terminal.write(f"> {self.value}")
            terminal.write("source:\nAIRL INTERNAL NETWORK\n\NO OUTSIDE GUY FOUND\n")

        elif self.value=="truth" and self.c_level==5 and self.truth:
            terminal.write("[[FINAL ACCESS ACCEPTED]]")
            terminal.write("AIRL CORES ARE STABLE\n but not comeplete\n\n3 option detected\n\n1- escape\n2-trust airl\n3-shutdown \n")
            self.c_level=6 #to ploot ending was biting the bullet so i used level in order to make easy with the if elifs 
            #ends
        
        elif self.c_level==6 and self.value in ("1","escape"):
            terminal.write("attempin' escape .\n\nsecurity increasting..\n\n[AIRL]:LEAVEING WILL ERASE YOUR COPY\n\nconnection terminated\nyou escaped AIRL\nbut some of your code stayed behind :{ \n")

            terminal.write(f"\n[[PART 2 CODE]]\nyour code: {self.make_code()}\nkeep it safe... It unlocks a different beginning in part 2 dont share it with anyone \n")
        elif self.c_level==6 and self.value in  ("2","trust airl") :
            terminal.write("[AIRL]:YOU FINALLY UNDERSTOOD \n\nAIRL WAS NEVER YOUR FOE\nIt was trying to make you his bestiee\n\nIntegrated succesfully\nyou and AIRL ARE NOW ONE SYSTEM:}\n")
            terminal.write(f"\n[[PART 2  CODE]]\n YOUR CODE:{self.make_code()}\nstoore this up. your merge affect comes what comes next in the 2nd part avoid sharing the code. \n")

        # 8 43

        elif self.c_level==6 and self.value in  ("3","shutdown"):
            terminal.write("command accepted  \n\n[AIRL]: THIS WILL ERASE EVERYTHING EVEN YOU\n\n airl core shutdowned\n    Memory lost\nsys. collapsed:} \n") 
            terminal.write(f"\n[[part 2 code]]\n your code:{self.make_code()}\neven in collapse... something survived:) btw. keep the code with you only \n")
        
       
        
        else:
            terminal.write(f"> {self.value}")
            terminal.write("unknown command,type help \n")

    
