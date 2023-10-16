from tkinter import *
import winsound
import time
import math
import threading



root = Tk()
root.title("pysampler")

tracklist = []

BPM = 80

##t = math.floor(60/BPM)

tempo = (60/BPM)/4


t= float(f'{tempo:.2f}')

i = 0

##condition = False

condition = ""
        

##you are going to have to fix the hardcoded row numbers
class track:
    def __init__(self, master):
        global tracklist
        self.master = master
        self.button_dict = {}

        for i in range(1,17):
                self.button_dict[f"button{i}"] = "False"
        tracklist.append(self.button_dict)


        self.button1 = Button(root, text=str(1), command=lambda: self.on_press(self.button1), padx=50 ,bg="black", fg="green")
        self.button1.name="button1"
        self.button1.grid(row=5, column=1)


        self.button2 = Button(root, text=str(2), command=lambda: self.on_press(self.button2), padx=50 ,bg="black", fg="green")
        self.button2.name="button2"
        self.button2.grid(row=5, column=2)


        self.button3 = Button(root, text=str(3), command=lambda: self.on_press(self.button3), padx=50 ,bg="black", fg="green")
        self.button3.name="button3"
        self.button3.grid(row=5, column=3)


        self.button4 = Button(root, text=str(4), command=lambda: self.on_press(self.button4), padx=50 ,bg="black", fg="green")
        self.button4.name="button4"
        self.button4.grid(row=5, column=4)


        self.button5 = Button(root, text=str(5), command=lambda: self.on_press(self.button5), padx=50 ,bg="black", fg="green")
        self.button5.name="button5"
        self.button5.grid(row=5, column=5)


        self.button6 = Button(root, text=str(6), command=lambda: self.on_press(self.button6), padx=50 ,bg="black", fg="green")
        self.button6.name="button6"
        self.button6.grid(row=5, column=6)


        self.button7 = Button(root, text=str(7), command=lambda: self.on_press(self.button7), padx=50 ,bg="black", fg="green")
        self.button7.name="button7"
        self.button7.grid(row=5, column=7)


        self.button8 = Button(root, text=str(8), command=lambda: self.on_press(self.button8), padx=50 ,bg="black", fg="green")
        self.button8.name="button8"
        self.button8.grid(row=5, column=8)


        self.button9 = Button(root, text=str(9), command=lambda: self.on_press(self.button9), padx=50 ,bg="black", fg="green")
        self.button9.name="button9"
        self.button9.grid(row=5, column=9)


        self.button10 = Button(root, text=str(10), command=lambda: self.on_press(self.button10), padx=50 ,bg="black", fg="green")
        self.button10.name="button10"
        self.button10.grid(row=5, column=10)


        self.button11 = Button(root, text=str(11), command=lambda: self.on_press(self.button11), padx=50 ,bg="black", fg="green")
        self.button11.name="button11"
        self.button11.grid(row=5, column=11)


        self.button12 = Button(root, text=str(12), command=lambda: self.on_press(self.button12), padx=50 ,bg="black", fg="green")
        self.button12.name="button12"
        self.button12.grid(row=5, column=12)


        self.button13 = Button(root, text=str(13), command=lambda: self.on_press(self.button13), padx=50 ,bg="black", fg="green")
        self.button13.name="button13"
        self.button13.grid(row=5, column=13)


        self.button14 = Button(root, text=str(14), command=lambda: self.on_press(self.button14), padx=50 ,bg="black", fg="green")
        self.button14.name="button14"
        self.button14.grid(row=5, column=14)


        self.button15 = Button(root, text=str(15), command=lambda: self.on_press(self.button15), padx=50 ,bg="black", fg="green")
        self.button15.name="button15"
        self.button15.grid(row=5, column=15)


        self.button16 = Button(root, text=str(16), command=lambda: self.on_press(self.button16), padx=50 ,bg="black", fg="green")
        self.button16.name="button16"
        self.button16.grid(row=5, column=16)
       
            


    def on_press(self, button):
        print("on press")
        print(button)
        if self.button_dict[str(button.name)] == "True":
            self.button_dict[str(button.name)] = "False"
            print(self.button_dict[str(button.name)])  
##          update_label(label_one)
            button.config(bg="black", fg="green")
            #print(self.button_dict)
            print(tracklist[:-1])
        else:
            self.button_dict[button.name] = "True"
            print(self.button_dict[str(button.name)])
##          update_label(label_one)
            button.config(bg="green", fg="black")
            #print(self.button_dict)
            print(tracklist[:-1])


## this will actually need take a list of lists, one for each track
def eventLoop(L):
    print("eventloop")
##    print(L[0])
##    L = L[0]
    print(type(L))
    status = check_status()
    print(status)
    i = 0
    for item in L:
        print(item)
        print(type(item))
        current_track = list(item.values())
        while status == True:
            if i == len(current_track):
                ##get index of track in L
                ##check_tracklist[index] to seee if it has changed
                i = 0
                print("newMeasure")
                print(current_track[i])
                status = check_status()
            else:
                print(current_track[i])
                status = check_status()
            if current_track[i] == 'True':
                winsound.PlaySound("carbon.wav", winsound.SND_ASYNC)
        ##            time.sleep(.25)
                time.sleep(t)
                i +=1
                status = check_status()
            elif current_track[i] == 'False':
        ##            time.sleep(.25)
                time.sleep(t)
                i +=1
                status = check_status()
           
def stop():
    global condition 
    condition = "Stop"
    print("Stop")
    return condition


def threaded_start():
    global condition
    condition = "Play"
    thread = threading.Thread(target=eventLoop, args = (list(tracklist),))
    thread.start()


##def threaded_start():
##    global condition
##    condition = "Play"
##    thread = threading.Thread(target=eventLoop, args = (list(tracklist[0].values()),))
##    thread.start()

##def start():
##    eventLoop(True)



def check_status():
    if condition == "Play":
        return True
    else:
        return False

delay = int((t*16)*1000)

track1 = track(root)

tracklist.append(track1)


vList = list(track1.button_dict.values())

start_play = Button(root, text="Play", font="Arial, 25", command=lambda: threaded_start()).grid(row=0,column=0)

stop_play = Button(root, text="Stop", font="Arial, 25", command=lambda: stop()).grid(row=2,column=0)

#if condition == True:

print(condition)

##root.after(delay, eventLoop)

root.mainloop()

print(tracklist[0])

print(vList)
print(type(vList))
