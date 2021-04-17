from tkinter import *
import os
import time

image_quality = 1
speed = 1

def sel():
   selection = "Shutter speed: " + str(var.get()) + 's'
   label.config(text = selection)

def sel_shots():
   selection = "Number of subs: " + str(shots_var.get())
   label2.config(text = selection)

def sel_iso():
   selection = "ISO: " + str(iso_var.get())
   label3.config(text = selection)

def start_capture():
    os.system('gphoto2 --set-config shutterspeed=0')
    B.config(state = DISABLED)
    shutter_speed = var.get()
    num_shots = shots_var.get()
    iso = int(iso_var.get())
    iso_code = 24

    if iso == 400:
        iso_code = 3
    elif iso == 800:
        iso_code = 4
    elif iso == 1600:
        iso_code = 5
    elif iso == 3200:
        iso_code = 6
    elif iso == 6400:
        iso_code = 7

    os.system('gphoto2 --set-config iso=' + str(iso_code))

    for shot in range(0, num_shots):
        bulb_shoot(shutter_speed)
        time.sleep(5)
        text.insert(END, 'Done Shooting sub ' + str(shot + 1) + '\n')
        text.update()
#        B.config(text = 'Shooting sub ' + str(shot))
    B.config(state = NORMAL)

def set_image_qual():
    global image_quality
    if 1 - image_quality == 1:
        B1.config(text='Quality set to Basic')
        os.system('gphoto2 --set-config imagequality=0')
    else:
        B1.config(text='Quality set to RAW')
        os.system('gphoto2 --set-config imagequality=3')
    image_quality = 1 - image_quality

def bulb_shoot(t):
    os.system('gphoto2 --set-config eosremoterelease=Immediate --wait-event=' + str(t) + 's --set-config eosremoterelease="Release Full" --wait-event=5s')
#    os.system('gphoto2 --set-config bulb=1 --wait-event=' + str(t) + 's --set-config capturetarget=1')

def thirty_sec_test():
    os.system('gphoto2 --set-config shutterspeed=1')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    os.system('gphoto2 --capture-image-and-download --filename /home/astroberry/Pictures/Capture/' + timestr + '.jpg')

root = Tk()
var = IntVar()
shots_var = IntVar()
iso_var = IntVar()

label = Label(root, text='Select shutter speed')
label.pack()

R0 = Radiobutton(root, text="15s", variable=var, value=15,
                  command=sel)
R0.pack( anchor = W )

R1 = Radiobutton(root, text="30s", variable=var, value=30,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="45s", variable=var, value=45,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="60s", variable=var, value=60,
                  command=sel)
R3.pack( anchor = W)

R4 = Radiobutton(root, text="90s", variable=var, value=90,
                  command=sel)
R4.pack( anchor = W)

R5 = Radiobutton(root, text="120s", variable=var, value=120,
                  command=sel)
R5.pack( anchor = W)

label2 = Label(root, text='Select number of subs')
label2.pack()

R21 = Radiobutton(root, text="20", variable=shots_var, value=20,
                  command=sel_shots)
R21.pack( anchor = W )

R22 = Radiobutton(root, text="30", variable=shots_var, value=30,
                  command=sel_shots)
R22.pack( anchor = W )

R23 = Radiobutton(root, text="40", variable=shots_var, value=40,
                  command=sel_shots)
R23.pack( anchor = W)

R24 = Radiobutton(root, text="50", variable=shots_var, value=50,
                  command=sel_shots)
R24.pack( anchor = W)

R25 = Radiobutton(root, text="60", variable=shots_var, value=60,
                  command=sel_shots)
R25.pack( anchor = W)


label3 = Label(root, text='Select ISO')
label3.pack()

R31 = Radiobutton(root, text="400", variable=iso_var, value=400,
                  command=sel_iso)
R31.pack( anchor = W )

R32 = Radiobutton(root, text="800", variable=iso_var, value=2000,
                  command=sel_iso)
R32.pack( anchor = W )

R33 = Radiobutton(root, text="1600", variable=iso_var, value=5000,
                  command=sel_iso)
R33.pack( anchor = W)

R34 = Radiobutton(root, text="3200", variable=iso_var, value=8000,
                  command=sel_iso)
R34.pack( anchor = W)

R35 = Radiobutton(root, text="6400", variable=iso_var, value=12800,
                  command=sel_iso)
R35.pack( anchor = W)

B = Button(root, text ="Start Capturing", command = start_capture)
B.pack( anchor = W)

#B1 = Button(root, text ="Set Image Quality to RAW or Basic", command = set_image_qual)
#B1.pack( anchor = W)

B3 = Button(root, text ="Capture Sample", command = thirty_sec_test)
B3.pack( anchor = W)



textframe = Frame(root)
text = Text(textframe)
text.pack()
textframe.pack()

text.insert(END,"Intervalometer is up\n")

#text = StringVar()
#text.set("Intervalometer is up")
label = Label(root, textvariable=text)
label.pack()

#T = Text(root, height = 5, width = 52)
#T.pack()

#T.insert(END, "Intervalometer is up")

root.title("Hari's Intervalometer")
root.mainloop()
