# GUI-Chat.py

from tkinter import *
from tkinter import ttk, messagebox
import tkinter.scrolledtext as st
from tkinter import simpledialog

#################network###################
import socket  
import threading
import sys

PORT = 7500
BUFSIZE = 4096
SERVERIP = '192.168.1.6' # SERVER IP

global client

def server_handler(client):

	while True:
		try:
			data = client.recv(BUFSIZE) # Data from server
		except:
			print('ERROR')
			break
		if(not data) or (data.decode('utf-8') == 'q'):
			print('OUT!')
			break

		allmsg.set(allmsg.get() + data.decode('utf-8') + '\n')
		chatbox.delete(1.0,END) # clear old msg
		chatbox.insert(INSERT,allmsg.get()) # insert new msg
		chatbox.yview(END)
		# print('USER: ', data.decode('utf-8'))

	client.close()
	messagebox.showerror('Connection Failed','ตัดการเชื่อมต่อ')

####################################
GUI = Tk()
# GUI.geometry('650x750+700+20')

w = 650
h = 750

ws = GUI.winfo_screenwidth() # screen width
hs = GUI.winfo_screenheight() # screen hight
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')

GUI.title('Basic chat room')
###########font##########################
FONT1 = ('Angsana New',35)
FONT2 = ('Angsana New',20)
################chatbox##################
F1 = Frame(GUI)
F1.place(x=5,y=5)

allmsg = StringVar()

chatbox = st.ScrolledText(F1,width=38,heigh=10,font=FONT1)
chatbox.pack(expand=True, fill='x')
###############message form###################
v_msg = StringVar()

F2 = Frame(GUI)
F2.place(x=20,y=650)

E1 = ttk.Entry(F2,textvariable=v_msg,font=FONT2,width=50)
E1.pack(ipady=20)

##############button###############
def SendMessage(event=None):
	msg = v_msg.get()
	#allmsg.set(allmsg.get() + msg + '\n---\n')
	client.sendall(msg.encode('utf-8')) # sent message to server
	chatbox.delete(1.0,END) # clear old msg
	chatbox.insert(INSERT,allmsg.get()) # insert new msg
	chatbox.yview(END)
	v_msg.set('') # clear msg
	E1.focus()

F3 = Frame(GUI)
F3.place(x=500,y=650)
B1 = ttk.Button(F3,text='Send',command=SendMessage)
B1.pack(ipadx=25,ipady=30)

E1.bind('<Return>',SendMessage)

username = StringVar()

getname = simpledialog.askstring('NAME','คุณชื่ออะไร?')
import random

if getname == '' or getname == None:
	num = random.randint(10000,99999)
	getname = str(num)

username.set(getname)
chatbox.insert(INSERT,'สวัสดี ' + getname)

################run server###################
global client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

try:
	client.connect((SERVERIP,PORT))
	firsttext = 'NAME|' + username.get()
	client.send(firsttext.encode('utf-8'))
	task = threading.Thread(target=server_handler, args=(client,))
	task.start()
except:
	print('ERROR!')
	messagebox.showerror('Connection Failed','ไม่สามารถเชื่อมต่อกับ server ได้')

GUI.mainloop()