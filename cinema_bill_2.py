from tkinter import *
import random
import os
import sys
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("650x450")
        self.root.title("Cinema Bill System")
        self.font = ("Arial",20)
        title = Label(self.root, text="Cinema Bill System", font=self.font).pack(fill=X)
        
        # Product variables
        self.popcorn = IntVar()
        self.coke = IntVar()
        self.layschips = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.popcorn_large = IntVar()
        self.total_sna = StringVar()
        self.a = StringVar()
        self.c_name = StringVar()
        
        #  customer details label frame
        details = LabelFrame(self.root, font=("Arial",12), relief="flat")
        details.place(x=20, y=50)
        
        cust_name = Label(details, text="Customer Name", font=("Arial",14))
        cust_name.grid(row=0, column=0, padx=5)
        
        cust_entry = Entry(details, width=30, textvariable=self.c_name)
        cust_entry.grid(row=0, column=1, padx=5)
        
        
        # snacks label frame
        snacks = LabelFrame(self.root, font=("Arial",12), relief="flat")
        snacks.place(x=50, y=120, height=180, width=230)
        
        cinema_label = Label(snacks, text="Cinema Menu", font=("Arial", 15)).grid(row=0, column=0)
        
        item1 = Label(snacks, text="Pop Corn : ", font=("Arial",11))
        item1.grid(row=1, column=0, pady=5)
        item1_entry = Entry(snacks, width=10, textvariable=self.popcorn)
        item1_entry.grid(row=1, column=1, padx=10)
 
        item2 = Label(snacks, text="Coke : ", font=("Arial",11))
        item2.grid(row=2, column=0, pady=5)
        item2_entry = Entry(snacks, width=10, textvariable=self.coke)
        item2_entry.grid(row=2, column=1, padx=10)
 
        item3 = Label(snacks, text="Lays Chips : ", font=("Arial",11))
        item3.grid(row=3, column=0, pady=5)
        item3_entry = Entry(snacks, width=10, textvariable=self.layschips)
        item3_entry.grid(row=3, column=1, padx=10)
 
        item4 = Label(snacks, text="Oreo : ", font=("Arial",11))
        item4.grid(row=4, column=0, pady=5)
        item4_entry = Entry(snacks, width=10, textvariable=self.oreo)
        item4_entry.grid(row=4, column=1, padx=10)
 
        #======== billarea ===============
        billarea = Frame(self.root, relief="flat")
        billarea.place(x=320, y=100, height=300, width=300)
        
        bill_title = Label(billarea,text="Bill Area",font=("Arial",15))
        bill_title.pack(fill=X)
        self.txtarea = Text(billarea) 
        self.txtarea.pack(fill=BOTH, expand=1)
        
        #=========== billing Summary =================
        billing_menu = LabelFrame(self.root, font=("Arial",12), relief="flat")
        billing_menu.place(x=10, y=310, height=100, width=290)
        
        total_snacks = Label(billing_menu, text="Total Bill", font=("Arial",11))
        total_snacks.grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, textvariable=self.total_sna)
        total_snacks_entry.grid(row=0, column=1, padx=10, pady=7)
        
        
        #======= All Buttons Frame ======
        button_frame = Frame(billing_menu, relief="flat")
        button_frame.place(x=20, y=50, width=265, height=60)
        
        button_total = Button(button_frame, text="Total", font=("Arial",15), command=lambda:self.total())
        button_total.grid(row=0, column=1, padx=5)
        button_clear = Button(button_frame, text="Clear", font=("Arial",15), command=lambda:self.clear())
        button_clear.grid(row=0, column=2, padx=5)
        button_exit = Button(button_frame, text="Exit", font=("Arial",15), command=lambda:self.exit1())
        button_exit.grid(row=0, column=3, padx=5)
        self.intro()
 

    def total(self):
        if (self.c_name.get==""):
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
        self.popcorn_total=self.popcorn.get()*120
        self.coke_total=self.coke.get()*40
        self.layschips_total=self.layschips.get()*10
        self.oreo_total=self.oreo.get()*20
        self.total_snacks_price=(
                    self.popcorn_total+
                    self.coke_total+
                    self.layschips_total+
                    self.oreo_total)          
        self.tax = round(self.total_snacks_price*0.05,3)
        self.a.set(str(self.tax)+" AED")
        self.total_all_bil=str(self.total_snacks_price+self.tax)+" AED"
        self.total_sna.set(self.total_all_bil)
        self.billarea()

    #method for printing basic bill details
    def intro(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\tWELCOME TO PVR Cinema\n\tPhone-No.9992223337")
        self.txtarea.insert(END,f"\n\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,"\n================================")
        self.txtarea.insert(END,"\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END,"================================\n")

    # method for handling billing
    def billarea(self):
        self.intro()
        if self.popcorn.get()!=0:
            self.txtarea.insert(END,f"Nutella\t\t {self.popcorn.get()}\t{self.popcorn_total}\n")
        if self.coke.get()!=0:
            self.txtarea.insert(END,f"Noodles\t\t {self.coke.get()}\t{self.coke_total}\n")
        if self.layschips.get()!=0:
            self.txtarea.insert(END,f"Lays\t\t {self.layschips.get()}\t{self.layschips_total}\n")
        if self.oreo.get()!=0:
            self.txtarea.insert(END,f"Oreo\t\t {self.oreo.get()}\t{self.oreo_total}\n")
    
        self.txtarea.insert(END,f"---------------------------------\n")
        if self.a.get()!="0.0 AED":
            self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")

        self.txtarea.insert(END,f"Total Snacks Amount : {self.total_snacks_price}\n")
        self.txtarea.insert(END,f"---------------------------------")

    def clear(self):
            self.txtarea.delete(8.0,END)
            self.popcorn.set(0)
            self.coke.set(0)
            self.layschips.set(0)
            self.oreo.set(0)
            self.total_sna.set(0)
            self.a.set(0)
            self.c_name.set('')

    def exit1(self):
        self.root.destroy()
    
root=Tk()
obj=Bill_App(root)
root.mainloop()
