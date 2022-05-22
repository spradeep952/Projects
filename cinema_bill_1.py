from tkinter import *
import random
import os
import sys
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1020x500")
        self.root.configure(bg="#fff")
        self.root.title("Cinema Bill System")
        self.font = ("Arial Black",20)
        title = Label(self.root, text="Cinema Bill System", font=self.font, bg="#A569BD", fg="white").pack(fill=X)
        
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
        self.bill_no = StringVar()
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()
        
        #  customer details label frame
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black",12), bg="#A569BD", fg="white")
        details.place(x=0, y=80)
        
        cust_name = Label(details, text="Customer Name", font=("Arial Black",14), bg="#A569BD", fg="white")
        cust_name.grid(row=0, column=0, padx=5)
        
        cust_entry = Entry(details, width=30, textvariable=self.c_name)
        cust_entry.grid(row=0, column=1, padx=5)
        
        contact_name = Label(details, text="Contact No.", font=("Arial Black",14), bg="#A569BD", fg="white")
        contact_name.grid(row=0, column=2, padx=5)
        
        contact_entry = Entry(details, width=30, textvariable=self.phone)
        contact_entry.grid(row=0, column=3, padx=5)

        bill_name = Label(details, text="Bill.No.", font=("Arial Black",14), bg="#A569BD", fg="white")
        bill_name.grid(row=0, column=4, padx=5)
        
        bill_entry = Entry(details, width=30, textvariable=self.bill_no)
        bill_entry.grid(row=0, column=5, padx=5)
        
        # snacks label frame
        snacks = LabelFrame(self.root, text="Cinema Menu", font=("Arial Black",12), bg="#E5B4F3", fg="#6C3483")
        snacks.place(x=5, y=180, height=300, width=280)
        
        item1 = Label(snacks, text="Pop Corn : ", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item1.grid(row=0, column=0, pady=5)
        item1_entry = Entry(snacks, width=10, textvariable=self.popcorn)
        item1_entry.grid(row=0, column=1, padx=10)
 
        item2 = Label(snacks, text="Coke : ", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item2.grid(row=1, column=0, pady=5)
        item2_entry = Entry(snacks, width=10, textvariable=self.coke)
        item2_entry.grid(row=1, column=1, padx=10)
 
        item3 = Label(snacks, text="Lays Chips : ", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item3.grid(row=2, column=0, pady=5)
        item3_entry = Entry(snacks, width=10, textvariable=self.layschips)
        item3_entry.grid(row=2, column=1, padx=10)
 
        item4 = Label(snacks, text="Oreo : ", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item4.grid(row=3, column=0, pady=5)
        item4_entry = Entry(snacks, width=10, textvariable=self.oreo)
        item4_entry.grid(row=3, column=1, padx=10)
 
        item5 = Label(snacks, text="Chocolate Muffin", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item5.grid(row=4, column=0, pady=5)
        item5_entry = Entry(snacks, width=10, textvariable=self.muffin)
        item5_entry.grid(row=4, column=1, padx=10)
 
        item6 = Label(snacks, text="Dairy Milk Silk : ", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item6.grid(row=5, column=0, pady=5)
        item6_entry = Entry(snacks, width=10, textvariable=self.silk)
        item6_entry.grid(row=5, column=1, padx=10)
 
        item7 = Label(snacks, text="Pop Corn (Large) : ", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        item7.grid(row=6, column=0, pady=5)
        item7_entry = Entry(snacks, width=10, textvariable=self.popcorn_large)
        item7_entry.grid(row=6, column=1, padx=10)
 
        #======== billarea ===============
        billarea = Frame(self.root,bd=5, bg="#E5B4F3")
        billarea.place(x=320, y=180, height=300, width=300)
        
        bill_title = Label(billarea,text="Bill Area",font=("Arial Black",17),bd=7,bg="#E5B4F3",fg="#6C3483")
        bill_title.pack(fill=X)
        
        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
        #=========== billing Summary =================
        billing_menu = LabelFrame(self.root, text="Bill Summary", font=("Arial Black",12), bg="#E5B4F3", fg="#6C3483")
        billing_menu.place(x=655, y=180, height=300, width=320)
        
        total_snacks = Label(billing_menu, text="Total Bill", font=("Arial Black",11), bg="#E5B4F3", fg="#6C3483")
        total_snacks.grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, textvariable=self.total_sna)
        total_snacks_entry.grid(row=0, column=1, padx=10, pady=7)
        
        
        #======= All Buttons Frame ======
        button_frame = Frame(billing_menu, bd=7, bg="#6C3483")
        button_frame.place(x=10, y=80, width=180, height=180)
        
        button_total = Button(button_frame, text="Total Bill", font=("Arial Black",15),width=10, bg="#E5B4F3", fg="#6C3483", command=lambda:self.total())
        button_total.grid(row=0, column=0, padx=5)
        button_clear = Button(button_frame, text="Clear Field", font=("Arial Black",15),width=10, bg="#E5B4F3", fg="#6C3483", command=lambda:self.clear())
        button_clear.grid(row=1, column=0, padx=5, pady=6)
        button_exit = Button(button_frame, text="Exit", font=("Arial Black",15),width=10, bg="#E5B4F3", fg="#6C3483", command=lambda:self.exit1())
        button_exit.grid(row=2, column=0, padx=5, pady=6)
        self.intro()
 

    def total(self):
        if (self.c_name.get=="" or self.phone.get()==""):
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
        self.popcorn_total=self.popcorn.get()*120
        self.coke_total=self.coke.get()*40
        self.layschips_total=self.layschips.get()*10
        self.oreo_total=self.oreo.get()*20
        self.muffin_total=self.muffin.get()*30
        self.silk_total=self.silk.get()*60
        self.popcorn_large_total=self.popcorn_large.get()*15
        self.total_snacks_price=(
                    self.popcorn_total+
                    self.coke_total+
                    self.layschips_total+
                    self.oreo_total+
                    self.muffin_total+
                    self.silk_total+
                    self.popcorn_large_total)          

        self.tax = round(self.total_snacks_price*0.05,3)
        self.a.set(str(self.tax)+" Rs")
        self.total_all_bill=self.total_snacks_price+self.tax
        self.total_all_bil=str(self.total_all_bill)+" Rs"
        self.total_sna.set(self.total_all_bil)
        self.billarea()

    #method for printing basic bill details
    def intro(self):
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(END,"\tWELCOME TO PVR Cinema\n\tPhone-No.9992223337")
        self.txtarea.insert(END,f"\n\nBill no. : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone No. : {self.phone.get()}")
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
        if self.muffin.get()!=0:
            self.txtarea.insert(END,f"Muffins\t\t {self.muffin.get()}\t{self.muffin_total}\n")
        if self.silk.get()!=0:
            self.txtarea.insert(END,f"Silk\t\t {self.silk.get()}\t{self.silk_total}\n")
        if self.popcorn_large.get()!=0:
            self.txtarea.insert(END,f"Namkeen\t\t {self.popcorn_large.get()}\t{self.popcorn_large_total}\n")

        self.txtarea.insert(END,f"---------------------------------\n")
        if self.a.get()!="0.0 Rs":
            self.txtarea.insert(END,f"Total Snacks Tax : {self.a.get()}\n")

        self.txtarea.insert(END,f"Total Snacks Amount : {self.total_snacks_price}\n")
        self.txtarea.insert(END,f"---------------------------------\n")

    def clear(self):
            self.txtarea.delete(10.0,END)
            self.popcorn.set(0)
            self.coke.set(0)
            self.layschips.set(0)
            self.oreo.set(0)
            self.muffin.set(0)
            self.silk.set(0)
            self.popcorn_large.set(0)
            self.total_sna.set(0)
            self.a.set(0)
            self.c_name.set('')
            self.bill_no.set(random.randint(1000,9999))
            self.phone.set(0)

    def exit1(self):
        self.root.destroy()
            
root=Tk()
obj=Bill_App(root)
root.mainloop()
