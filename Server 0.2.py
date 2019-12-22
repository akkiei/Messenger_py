from tkinter import *
import socket
import tkinter
import threading
import os
from tkinter import messagebox


class Application(threading.Thread):

    def __init__(self, form):

        host = socket.gethostname()
        port = 7777
        global sock
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (host, port)
        sock.bind(address)
        sock.listen(10)
        print("Now listening.....")



        global client
        #client, addr = sock.accept()
        client, addr = sock.accept()
        print("Got a connection from ", str(addr[0]), str(addr[1]))
        root.update()
        threading.Thread.__init__(self)
        self.start()
        ##################
        # while True:
        #         print('SERver')
        #         data = client.recv(1024)
        #         if data is not '':
        #             print('inside true if')
        #             string = data.decode()
        #             print(string)
        #             str1 = string + '\n'
        #             self.textarea1.config(state=NORMAL)
        #             self.textarea1.insert(INSERT, str1)
        #             self.textarea1.config(state=DISABLED)
        #         print('after IF')
            #    root.update()


    def run(self):
      while True:
         try:
            Data = client.recv(1024)
         except ConnectionResetError:
                os._exit(1)
         if Data is not '':
                string=Data.decode()
               # print(string)
                str1=string+'\n'
               # textarea1.tag_configure("BOLD", font=self.bold_font)
               # textarea1.configure('right',justify="right")
                textarea1.config(state=NORMAL)
                textarea1.insert('1.0',str1)
                textarea1.config(state=DISABLED)

            #root.update()

    def data_send(mess):
            mess =textbox1.get()
            if mess is '':
                return
            msg=str.encode(my_name+':'+mess)
            client.sendall(msg)
            string = 'YOU:'+ mess +'\n'
            textarea1.config(state=NORMAL)
            textarea1.insert('1.0', string)
            textarea1.config(state=DISABLED )
            textbox1.delete(0, END)
#            print(data.decode())

#############################


###############################
def about():
    messagebox.showinfo('About...','Hello Everyone, My name is AkashDeep Shukla (aka \'AKKIEI\' ) \nand I created this application for all of you.!\nAKashdeep shukla\nakashdeepshukla007@gmail.com \n7844066445')



global my_name
my_name=input('Enter your name here !\n')
while my_name is '':
    my_name = input("c'mon give me your real name this time !")

root = Tk()
ob=Application(root)
root.config(background='brown')
root.resizable(0,0)
root.minsize(200, 200)
root.title('Server')

        # Global Padding pady and padx
pad_x = 5
pad_y = 5
global textbox1
textbox1 = Entry(root,fg='red',width=40)
textbox1.bind('<Return>', lambda _: ob.data_send())
        #command= parameter missing.
global button1
button1 = Button(root,command=ob.data_send,text='Send',fg='red')
global scrollbar1
scrollbar1 = Scrollbar(root)
global textarea1
textarea1 = Text(root, width=40, height=20,fg='red',wrap=WORD) ###


menu=Menu(root)
root.config(menu=menu)

sub_menu=Menu(root)
menu.add_cascade(label='ABOUT',menu=sub_menu)
sub_menu.add_separator()
sub_menu.add_command(label='About the cool guy who wrote this.' ,command=about)
sub_menu.add_separator()


textarea1.config(state=DISABLED,yscrollcommand=scrollbar1.set) ####
scrollbar1.config(command=textarea1.yview)

textarea1.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky=W)
scrollbar1.grid(row=0, column=2, padx=pad_x, pady=pad_y, sticky=W)
textbox1.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky=W)
button1.grid(row=1, column=2, padx=pad_x, pady=pad_y, sticky=W)
textarea1.tag_configure('red',foreground='red')
def on_closing():
      root.destroy()
      os._exit(1)

root.protocol("WM_DELETE_WINDOW", on_closing)
#protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()







