from tkinter import *
import socket
import threading
import os
import ipaddress
import time
from tkinter import messagebox
import ctypes

class Application(threading.Thread):

    def __init__(self, form):
        global sock
        sock = socket.socket()
        p=True
        host=input()
        while True:
            try:
                ipaddress.ip_address(host)
                break
            except:
                print('Wrong IP address or unable to connect.\nMake sure the server is up and doing.')
                host=input()
    #        host = '10.51.4.44'
       # host = socket.gethostname()
        port = 7777
        sock.connect((host, port))
        print('connected')
        #self.protocol("WM_DELETE_WINDOW", self.on_exit)
        ########################
        # kernel32 = ctypes.WinDLL('kernel32')
        # user32 = ctypes.WinDLL('user32')
        #
        # SW_HIDE = 0
        #
        # hWnd = kernel32.GetConsoleWindow()
        # if hWnd:
        #     user32.ShowWindow(hWnd, SW_HIDE)


        threading.Thread.__init__(self)
        self.start()

        # while True:
        #        print('p')
        #        data = sock.recv(1024)
        #        if data is not '':
        #            string = data.decode()
        #            print(string)
        #            str1 = string + '\n'
        #            self.textarea1.config(state=NORMAL)
        #            self.textarea1.insert(INSERT, str1)
        #            self.textarea1.config(state=DISABLED)
        #        form.mainloop()


    def run(self):
      while True:
         try:
            Data = sock.recv(1024)
         except ConnectionResetError:
             os._exit(1)
         if Data is not '':
                string = Data.decode()
                #print(string)
                str=string+'\n'
                textarea1.config(state=NORMAL)
                textarea1.insert('1.0',str)
                textarea1.config(state=DISABLED)
         #   root.update()

        #self.textbox1.insert(END,string=string)
       # self.textbox1.pack()


    def data_send(self,event=None):
            mess = textbox1.get()
            if mess is '':
                return
            msg = str.encode((my_name+':'+mess))
            sock.sendall((msg))
            string = 'YOU:' + mess + '\n'
            textarea1.config(state=NORMAL)
            textarea1.insert('1.0', string)
            textarea1.config(state=DISABLED)
            textbox1.delete(0, END)
    #        print(data.decode())

###############################
def about():
    messagebox.showinfo('About...','Hello Everyone, My name is AkashDeep Shukla (aka \'AKKIEI\' ) \nand I created this application for all of you.!\nAkashdeep shukla\nakashdeepshukla007@gmail.com \n7844066445')


##############################
# global host
# host=''
root = Tk()
# textbox2=Entry(root)
# textbox2.grid(row=1, column=1, padx=5, pady=5, sticky=W)
# textbox2.update()
#
# try:
#     time.sleep(3)
#     ipaddress.ip_address(textbox2.get())
#
# except:
#     print('Error')
#
#     #textbox2.update()
# host=str(textbox2.get())
#print(host,'ddfsd')


global my_name
my_name=input('Enter Your name !\n')
while my_name is '':
    my_name = input("c'mon give me your real name this time !")

print('Enter IP address of server')



ob=Application(root)
root.config(background='green')
root.resizable(0,0)
root.minsize(200, 200)
root.title('Client')


        # Global Padding pady and padx
pad_x = 5
pad_y = 5
global textbox1,textarea1,scrollbar1,button1
textbox1 = Entry(root,fg='red',width=40)
textbox1.bind('<Return>', lambda _: ob.data_send())
############################
menu=Menu(root)
root.config(menu=menu)

sub_menu=Menu(root)
menu.add_cascade(label='ABOUT',menu=sub_menu)
sub_menu.add_separator()
sub_menu.add_command(label='About the cool guy who wrote this..' ,command=about)
sub_menu.add_separator()




        #command= parameter missing.
button1 = Button(root,command=ob.data_send,text='Send',fg='red')

scrollbar1 = Scrollbar(root)
textarea1 = Text(root, width=40, height=20,)

textarea1.config(state=DISABLED,yscrollcommand=scrollbar1.set) ####
scrollbar1.config(command=textarea1.yview)

textarea1.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky=W)
scrollbar1.grid(row=0, column=2, padx=pad_x, pady=pad_y, sticky=W)
textbox1.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky=W)

button1.grid(row=1, column=2, padx=pad_x, pady=pad_y, sticky=W)
textarea1.tag_config('red',foreground='red')

def on_closing():
        root.destroy()
        os._exit(1)
root.protocol("WM_DELETE_WINDOW", on_closing)
# protocol("WM_DELETE_WINDOW",on_exit)
root.mainloop()
#root.mainloop()
