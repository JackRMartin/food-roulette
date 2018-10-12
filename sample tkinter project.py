import tkinter as tk
import random

comchoose = ("Paper", "Rock", "Scissor")
com=""
def enter():
     ans=str(dad10.get())
     if (ans=="go home"):
          topwindow11=tk.Toplevel()
          topwindow11.geometry("10000x100000")
          topwindow11.title("Lost")
          label101 = tk.Label(topwindow11, text=("GAME OVER!!! \n You lost chicken!"), font = ("Times New Roman", 200), fg="red")
          label101.grid()
          topwindow11.mainloop()
     if(ans=="go to the arena"):
          topwindow34=tk.Toplevel()
          topwindow34.geometry("10000x10000")
          topwindow34.title("ARENA")
          name=str(dad1.get())
          age=str(dad2.get())
          gender=str(dad3.get())
          weaponname=str(dad4.get())
          armour=str(dad5.get())
          label1234= tk.Label(topwindow34, text=name+(" was at the arena. ")+name+(" was about to battle the \n evil man, BIG HARRY!!! \n The King announced the names. \n First we have BIG HARRY!!! Everyone cheered. We \n also have ")+name+(", the Tough Warrior! \n Choose your weapon. The Big Harry took out a \n sword. ")+name+(" took out a ")+weaponname+(". Nice choice! Now tell us your ages! Big HARRY was 34 years old. ")+name+(" was ")+age+(" years old. If this is not obvious already, \n what are your genders? Big HARRY is a man. And ")+name+ (" is a ")+gender+(" . What kind of armour are you people wearing? \n Big Harry was wearing Fire Thunder Armour! ")+name+(" is wearing ")+armour+(" Armour. Now FIGHT!!! ")+name+(" and The Big HARRY were battling. After hours of fighting, \n The Big HARRY fell and ")+name+(" claimed victory! \n The End!"), font=("Times New Roman",20), bg="red", fg="white")
          label1234.grid()
          topwindow34.grid()
def Lose():
     topwindow12345=tk.Toplevel()
     topwindow12345.geometry("10000x10000")
     topwindow12345.title("Wonder")
     topwindow12345.grid()
     labelarmando=tk.Label(topwindow12345, text=("YOU LOST BECAUSE THE HORSE BEAT YOU!!! The horse is smarter than you! He chose ")+com+(". LOL"), font= ("Times New Roman", 20), bg="red", fg="white")
     labelarmando.grid()
     topwindow12345.mainloop()
def Tie():
     topwindow12345=tk.Toplevel()
     topwindow12345.geometry("10000x10000")
     topwindow12345.title("Dreams")
     topwindow12345.grid()
     labelarmando=tk.Label(topwindow12345, text=("YOU Tied with the horse which means you lost! Horse got ")+com+(". LOL"), font= ("Times New Roman", 20), bg="red", fg="white")
     labelarmando.grid()
     topwindow12345.mainloop()
def Win():
     topwindow123456=tk.Toplevel()
     topwindow123456.geometry("10000x10000")
     topwindow123456.title("GG")
     topwindow123456.grid()
     name=str(dad1.get())
     labelarmando1=tk.Label(topwindow123456, text=("YOU won against the horse which means you caught it! Horse got ")+com+(".\n After a long day of playing rock, paper, scissors,")+name+(" got tired and decided to go home. GAME OVER!"), font= ("Times New Roman", 20), bg="red", fg="white")
     labelarmando1.grid()
     topwindow123456.mainloop()
     
def hoursebattle():
     user=str(dad1000.get())
     global com
     com = random.choice(comchoose)
     print (com)
     print (user)
     if(com == "Rock" and( user == "rock" or user == "Rock")):
          Tie()
     if(com == "Rock" and( user == "Paper" or user == "paper")):
          Win()
     if(com == "Rock" and( user == "Scissors" or user == "scissors")):
          Lose()
     if(com == "Paper" and (user == "paper" or user == "Paper")):
          Tie()
     if(com == "Paper" and (user == "rock" or user == "Rock")):
          Lose()
     if(com == "Paper" and (user == "Scissors" or user == "scissors")):
          Win()
     if(com == "Scissors" and (user == "Paper" or user == "paper")):
          Lose()
     if(com == "Scissors" and( user == "Rock" or user == "rock")):
          Win()
     if(com == "Scissors" and( user == "Scissors" or user == "scissors")):
          Tie()
dad1000=None
def horse():
    global dad1000
    topwindow2=tk.Toplevel()
    topwindow2.title("Horsie")
    topwindow2.geometry("900x400")
    name=str(dad1.get())
    label8 = tk.Label(topwindow2,text=name+(" went into the forest and saw a horse but\n in order to gain the horse's trust,")+name+(" must defeat \n the horse in Rock Paper SCISSORS! \n Choose Rock Paper Scissors!"), font = ("Times New Roman",20),bg="brown", fg="white")
    label8.grid(column=1, row=4, sticky=tk.E)
    dad1000=tk.Entry(topwindow2, bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
    dad1000.grid(column=1)
    button56=tk.Button(topwindow2, text="Submit Answer",bg="purple",height=5,width=30, fg="white", font = ("Arcade"),command=hoursebattle)
    button56.grid(column=1)

dad10 = None
def robot():
     global dad10
     topwindow3=tk.Toplevel()
     topwindow3.title("Town")
     topwindow3.geometry("800x900")
     name=str(dad1.get())
     weaponname=str(dad4.get())
     label10 = tk.Label(topwindow3, text=name+(" walked through town and saw a \n bunch of robbers in town. ")+name+(" tried to get out of there but failed. \n But wait! ")+name+(" still has hope and that \n is to beat the robbers with a ")+weaponname+("! Now, ")+name+(" is really \n tired from fighting \n bad guys. \n Should ")+name+(" go home or \n go to the arena?"), font = ("Times New Roman", 20),bg="red", fg="white")
     label10.grid()
     dad10=tk.Entry(topwindow3, bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
     dad10.grid()
     button52=tk.Button(topwindow3, text="Submit Answer",bg="purple",height=5,width=30, fg="white", font = ("Arcade"),command=enter)
     button52.grid()
     
     topwindow3.grid()
     topwindow3.mainloop()

def Start_Story():
    grand1=len(dad1.get())
    if(grand1==0):
        print ("Fill entry one")
    grand2=len(dad2.get())
    if(grand2==0):
        print ("Fill entry two")
    grand3=len(dad3.get())
    if(grand3==0):
        print ("Fill entry three") 
    grand4=len(dad4.get())
    if (grand4==0):
        print ("Fill entry four")
    else:
         topwindow = tk.Toplevel()
         topwindow.geometry("900x400")

         topwindow.grid_columnconfigure(0, weight=1)
         topwindow.title("Story")
         name=str(dad1.get())
         we1 = tk.Label(topwindow,text=name+(" just woke up and realized that today was the biggest day. \n ")+name+(" was going to battle in the arena but first is going to decide if \n there was no time and walk straight to the arena or needed a horse. \n which can only be found in a forest. \n Press one of the buttons to continue"), font = ("Times New Roman",20),bg="brown", fg="white")
         we1.grid(column=3, row=4, sticky=tk.W+tk.E)
         
         button1=tk.Button(topwindow, text="Get Horse",bg="purple",height=5,width=30, fg="white", font = ("Arcade"), command= horse)
         button1.grid(column=3, row=7, sticky=tk.E)

         button2=tk.Button(topwindow, text="Go Straight to the Arena",bg="purple",height=5,width=30, fg="white", font = ("Arcade"), command= robot)
         button2.grid(column=3, row=9, sticky=tk.E)
         topwindow.mainloop()
window = tk.Tk()
window.title("Roman's Tab")
window.geometry("600x600")

window.grid_columnconfigure(0, weight=1)

label1 = tk.Label(text=" Welcome to the Roman Gladiator ", font = ("Times New Roman",20),bg="brown", fg="green")

label1.grid(column=0, row=0, columnspan=2, sticky=tk.W+tk.E)

label2 = tk.Label(text="Enter Your Name:", font = ("Times New Roman",20),bg="gray", fg="white")
label2.grid(column=0, row=1, sticky = tk.E)

label3 = tk.Label(text="Enter Your Age:", font = ("Times New Roman",20),bg="blue", fg="black")
label3.grid(column=0, row=3, sticky = tk.E)

label4 = tk.Label(text="Enter Your Gender:", font = ("Times New Roman",20),bg="gray", fg="white")
label4.grid(column=0, row=5, sticky = tk.E)

label5 = tk.Label(text="Enter Your Weapon:", font = ("Times New Roman",20),bg="blue", fg="black")
label5.grid(column=0, row=7, sticky = tk.E)

label6 = tk.Label(text="Enter Your Armour Name:", font = ("Times New Roman",20),bg="gray", fg="white")
label6.grid(column=0, row=9, sticky = tk.E)

dad2=tk.Entry(bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
dad2.grid(column=1, row=3, sticky = tk.W)

dad3=tk.Entry(bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
dad3.grid(column=1, row=5, sticky = tk.W)

dad4=tk.Entry(bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
dad4.grid(column=1, row=7, sticky = tk.W)

dad1=tk.Entry(bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
dad1.grid(column=1, row=1, sticky = tk.W)

dad5=tk.Entry(bg="yellow", fg="red", width=20, font = ("Times New Roman",20))
dad5.grid(column=1, row=9, sticky = tk.W)

button=tk.Button(text="Start Your Story",bg="purple",height=5,width=30, fg="white", font = ("Arcade"), command = Start_Story)
button.grid(column=1, row=12, sticky=tk.W)

window.mainloop()

