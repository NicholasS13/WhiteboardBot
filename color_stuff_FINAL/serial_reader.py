import serial.tools.list_ports
from tkinter import *

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()

#initialize Tkinter
root = Tk()
root.title("Arduino Serial Filter Program")
root.geometry("600x500")

my_frame = Frame(root)
my_frame.pack(pady=20)
livergb = Text(my_frame, width=20, height=25)
livergb.pack(side=RIGHT, padx=5)
livecolor = Text(my_frame, width=20, height=25)
livecolor.pack(side=LEFT)
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        serial_stream = packet.decode('utf').rstrip('\n')
        if "LIVERGB: " in serial_stream: #Raw RGB Value being Read
            pass;
        elif "LIVECOLOR: " in serial_stream: # live color detected
            pass
        elif "LIVELASTCOLOR: " in serial_stream:
            pass
        elif "COLOR LIST: " in serial_stream: #Last color, current Color
            pass
        else:
            pass
        
        print(serial_stream)
