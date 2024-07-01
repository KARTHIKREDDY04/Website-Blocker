from tkinter import *

window = Tk()
window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 400)
window.title("Website Blocker")

heading = Label(window, text='Website Blocker', font='arial')
heading.pack()

host_path = 'C:/Windows/System32/drivers/etc/hosts'
ip_address = '127.0.0.1'

def get_website_list():
    return list(enter_website.get(1.0, END).split(","))

def block_website():
    websites = get_website_list()
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in websites:
            if web in file_content:
                display = Label(window, text='Already Blocked', font='arial')
                display.place(x=200, y=200)
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text="Blocked", font='arial').place(x=230, y=200)

def unblock_website():
    websites = get_website_list()
    with open(host_path, 'r') as host_file:
        file_content = host_file.readlines()
    with open(host_path, 'w') as f:
        for line in file_content:
            is_blocked = False
            for web in websites:
                if web in line:
                    is_blocked = True
                    break
            if not is_blocked:
                f.write(line)
    display = Label(window, text='Unblocked Successfully', font='arial')
    display.place(x=350, y=200)

label1 = Label(window, text='Enter Website :', font='arial 13 bold')
label1.place(x=5, y=60)

enter_website = Text(window, font='arial', height='2', width='40')
enter_website.place(x=140, y=60)

block_button = Button(window, text='Block', font='arial', pady=5, command=block_website, width=6, bg='royal blue1',
                      activebackground='grey')
block_button.place(x=230, y=150)

unblock_button = Button(window, text='UnBlock', font='arial', pady=5, command=unblock_website, width=6, bg='royal blue1',
                        activebackground='grey')
unblock_button.place(x=350, y=150)

window.mainloop()