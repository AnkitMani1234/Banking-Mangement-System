import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def check_acc_nmb(num):
    try:
        with open(num + ".txt", 'r') as fpin:
            pass
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return False
    return True

def home_return(master):
    master.destroy()
    Main_Menu()

def write(master, name, oc, pin):
    if is_number(name) or not is_number(oc) or not is_number(pin) or name == "":
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    
    with open("Accnt_Record.txt", 'r') as f1:
        accnt_no = int(f1.readline())
    accnt_no += 1
    with open("Accnt_Record.txt", 'w') as f1:
        f1.write(str(accnt_no))
    
    with open(f"{accnt_no}.txt", "w") as fdet:
        fdet.write(f"{pin}\n{oc}\n{accnt_no}\n{name}\n")
    
    with open(f"{accnt_no}-rec.txt", 'w') as frec:
        frec.write("Date Credit Debit Balance\n")
        frec.write(f"{strftime('[%Y-%m-%d] [%H:%M:%S] ', gmtime())} {oc} {oc}\n")
    
    messagebox.showinfo("Details", f"Your Account Number is: {accnt_no}")
    master.destroy()

def crdt_write(master, amt, accnt, name):
    if not is_number(amt):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    
    with open(f"{accnt}.txt", 'r') as fdet:
        pin = fdet.readline()
        camt = int(fdet.readline())
    
    amti = int(amt)
    cb = amti + camt
    
    with open(f"{accnt}.txt", 'w') as fdet:
        fdet.write(f"{pin}{cb}\n{accnt}\n{name}\n")
    
    with open(f"{accnt}-rec.txt", 'a+') as frec:
        frec.write(f"{strftime('[%Y-%m-%d] [%H:%M:%S] ', gmtime())} {amti} {cb}\n")
    
    messagebox.showinfo("Success", "Amount Credited Successfully!!")
    master.destroy()

def debit_write(master, amt, accnt, name):
    if not is_number(amt):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    
    with open(f"{accnt}.txt", 'r') as fdet:
        pin = fdet.readline()
        camt = int(fdet.readline())
    
    if int(amt) > camt:
        messagebox.showinfo("Error!!", "Insufficient Balance\nPlease try again.")
    else:
        amti = int(amt)
        cb = camt - amti
        
        with open(f"{accnt}.txt", 'w') as fdet:
            fdet.write(f"{pin}{cb}\n{accnt}\n{name}\n")
        
        with open(f"{accnt}-rec.txt", 'a+') as frec:
            frec.write(f"{strftime('[%Y-%m-%d] [%H:%M:%S] ', gmtime())} -{amti} {cb}\n")
        
        messagebox.showinfo("Success", "Amount Debited Successfully!!")
    master.destroy()

def disp_bal(accnt):
    with open(f"{accnt}.txt", 'r') as fdet:
        fdet.readline()
        bal = fdet.readline()
    messagebox.showinfo("Balance", bal)

def check_log_in(master, name, acc_num, pin):
    if not check_acc_nmb(acc_num):
        master.destroy()
        Main_Menu()
        return
    if is_number(name) or not is_number(pin):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()
    else:
        master.destroy()
        logged_in_menu(acc_num, name)

def log_in(master):
    master.destroy()
    loginwn = tk.Tk()
    loginwn.geometry("600x300")
    loginwn.title("Log in")
    loginwn.configure(bg="SteelBlue1")
    
    tk.Label(loginwn, text="Enter Name:").pack()
    e1 = tk.Entry(loginwn)
    e1.pack()
    tk.Label(loginwn, text="Enter Account Number:").pack()
    e2 = tk.Entry(loginwn)
    e2.pack()
    tk.Label(loginwn, text="Enter your PIN:").pack()
    e3 = tk.Entry(loginwn, show="*")
    e3.pack()
    
    tk.Button(loginwn, text="Submit", command=lambda: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip())).pack()
    loginwn.mainloop()

def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1600x500")
    rootwn.title("Bank Management System")
    rootwn.configure(bg='SteelBlue1')
    
    tk.Label(rootwn, text="BANK MANAGEMENT SYSTEM", font=("Verdana", 40, "bold"), bg="blue4", fg="white").pack()
    
    tk.Button(rootwn, text="Create Account", command=Create).pack()
    tk.Button(rootwn, text="Log In", command=lambda: log_in(rootwn)).pack()
    tk.Button(rootwn, text="Quit", command=rootwn.destroy).pack()
    
    rootwn.mainloop()

Main_Menu()
