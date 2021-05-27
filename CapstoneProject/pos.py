# This applications purpose is to replicate a POS (Point of Sale)
# System for a Coffee Shop.
# --------------------------------------------

from tkinter import *
from tkinter import ttk
import tkinter as tk
import tempfile
import os
from tkinter import messagebox

# --- The application ---

class pos:

    # ---- POS window information ----

    def __init__(self, root):
        self.root = root
        self.root.title("Jitter's Cafe - POS")
        self.root.geometry("1350x750")
        self.root.configure(background="#87a7b3")
        self.input_value = True

        # ---- Menu Items ----

        self.coffee1 = PhotoImage(file= "CapstoneProject/images/coffee1.gif")
        self.coffee2 = PhotoImage(file= "CapstoneProject/images/coffee2.gif")
        self.coffee3 = PhotoImage(file= "CapstoneProject/images/coffee3.gif")
        self.coffee4 = PhotoImage(file= "CapstoneProject/images/coffee4.gif")
        self.coffee5 = PhotoImage(file= "CapstoneProject/images/coffee5.gif")
        self.coffee6 = PhotoImage(file= "CapstoneProject/images/coffee6.gif")

        self.drink1 = PhotoImage(file= "CapstoneProject/images/drink1.gif")
        self.drink2 = PhotoImage(file= "CapstoneProject/images/drink2.gif")
        self.drink3 = PhotoImage(file= "CapstoneProject/images/drink3.gif")
        self.drink4 = PhotoImage(file= "CapstoneProject/images/drink4.gif")
        self.drink5 = PhotoImage(file= "CapstoneProject/images/drink5.gif")
        self.drink6 = PhotoImage(file= "CapstoneProject/images/drink6.gif")

        self.food1 = PhotoImage(file= "CapstoneProject/images/food1.gif")
        self.food2 = PhotoImage(file= "CapstoneProject/images/food2.gif")
        self.food3 = PhotoImage(file= "CapstoneProject/images/food3.gif")
        self.food4 = PhotoImage(file= "CapstoneProject/images/food4.gif")
        self.food5 = PhotoImage(file= "CapstoneProject/images/food5.gif")
        self.food6 = PhotoImage(file= "CapstoneProject/images/food6.gif")

        self.cake1 = PhotoImage(file= "CapstoneProject/images/cake1.gif")
        self.cake2 = PhotoImage(file= "CapstoneProject/images/cake2.gif")
        self.cake3 = PhotoImage(file= "CapstoneProject/images/cake3.gif")
        self.cake4 = PhotoImage(file= "CapstoneProject/images/cake4.gif")
        self.cake5 = PhotoImage(file= "CapstoneProject/images/cake5.gif")
        self.cake6 = PhotoImage(file= "CapstoneProject/images/cake6.gif")

        # ---- Global Constants ----

        global operator
        operator = ""
        Change_Input = StringVar()
        Cash_Input = StringVar()
        Tax_Input = StringVar()
        SubTotal_Input = StringVar()
        Total_Input = StringVar()
        Item = StringVar()
        Qty = StringVar()
        choice = StringVar()

        # ---- App Frames ----

        MainFrame = Frame(self.root, bg='#5b5b5b')
        MainFrame.grid(padx=8,pady=5)

        ButtonFrame = Frame(MainFrame, bd=5, width=1350, height=160, padx=4, pady=4, bg='#5b5b5b', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=5, width=1300, height=400, bg='#5b5b5b', relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFTCOVER = LabelFrame(DataFrame, bd=5, width=800, height=300, pady=2, relief=RIDGE
                            , bg='#5b5b5b', font=('Arial', 12,'bold'), text="Point of Sale",)
        DataFrameLEFTCOVER.pack(side=LEFT)

        KeypadFrame = Frame(DataFrameLEFTCOVER, bd=5, width=300, height=460, pady=5, relief=RIDGE)
        KeypadFrame.pack(side=LEFT, padx=4)

        ReceiptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, pady=5, padx=1, relief=RIDGE)
        ReceiptFrame.pack(side=RIGHT, padx=0)

        FoodItemFrame = LabelFrame(DataFrame, bd=5, width=450, height=300, padx=5, pady=2, relief=RIDGE
                        , bg='#5b5b5b', font=('Arial', 12, 'bold'), text="Menu",)
        FoodItemFrame.pack(side=RIGHT)

        CalFrame = Frame(ButtonFrame, bd=5, width=432, height=140, relief=RIDGE)
        CalFrame.grid(row = 0, column = 0, padx=5)

        ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140, pady=2, relief=RIDGE)
        ChangeFrame.grid(row = 0, column = 1, padx=5)

        RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        RemoveFrame.grid(row = 0, column = 2, padx=5)

        # ---- Keypad Function ----

        def btnClick(numbers):
            global operator
            operator = operator + str(numbers)
            Cash_Input.set(operator)

        # ---- Print Button Function ----

        def iPrint():
            q = self.txtReceipt.get("1.0", "end-1c")
            print(q)
            filename = tempfile.mktemp(".txt")
            open (filename, "w").write(q)
            os.startfile(filename, "print")

        # ---- Reset Button Function ----

        def btnClear():
            global operator
            operator=""
            Change_Input.set("")
            Cash_Input.set("0")
            Tax_Input.set("")
            SubTotal_Input.set("")
            Total_Input.set("")
            for i in self.POS_receipt.get_children():
                self.POS_receipt.delete(i)

        # ---- Clear Function ----

        def clear():
            Change_Input.set("")
            Cash_Input.set("0")

        # ---- Remove Item Function ----

        def delete():
            itemCost = 0.0
            Tax = 4.7
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
            SubTotal_Input.set(str('$%.2f'%(itemCost)))
            Tax_Input.set(str('$%.2f'%(((itemCost)* Tax)/100)))
            Total_Input.set(str('$%.2f'%((itemCost) + ((itemCost * Tax)/100))))
            selected_item = (self.POS_receipt.selection()[0])
            self.POS_receipt.delete(selected_item)
            giveChange()

        # ---- Change Function ----

        def giveChange():
            itemCost = 0.0
            Tax = 4.7
            CashInput = float(Cash_Input.get())
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
            Change_Input.set(str('$%.2f'%(CashInput-((itemCost) + ((itemCost * Tax)/100)))))
            if (Cash_Input.get() == "0"):
                Change_Input.set("")
                Payment_Method()

        # ---- Pay Button Function ----

        def Payment_Method():
            if (choice.get() == "Cash"):
                self.txtCost.focus()
                Cash_Input.set("")
            elif (choice.get() ==""):
                Cash_Input.set("0")
                Change_Input.set("")

        # ---- Menu Buttons - Cake Functions ----

        def cake1():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Chocolate Cake","1","3.00"))
            self.txtReceipt.insert(END, ("Chocolate Cake" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        def cake2():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Pink Cake","1","3.00"))
            self.txtReceipt.insert(END, ("Pink Cake" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        def cake3():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("White Cake","1","3.00"))
            self.txtReceipt.insert(END, ("White Cake" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        def cake4():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Red Velvet Cake","1","3.00"))
            self.txtReceipt.insert(END, ("Red Velvet Cake" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        def cake5():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Strawberry Cake","1","3.00"))
            self.txtReceipt.insert(END, ("Strawberry Cake" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        def cake6():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Carrot Cake","1","3.00"))
            self.txtReceipt.insert(END, ("Carrot Cake" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        # ---- Menu Buttons - Coffee Functions ----

        def coffee1():
            itemCost = 3.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Iced Coffee","1","3.50"))
            self.txtReceipt.insert(END, ("Iced Coffee" +"\t\t\t" + "1" + "\t\t\t" + "3.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.50) + ((itemCost-3.50)* Tax)/100)))

        def coffee2():
            itemCost = 2.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Black Coffee","1","2.00"))
            self.txtReceipt.insert(END, ("Black Coffee" +"\t\t\t" + "1" + "\t\t\t" + "2.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-2.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-2.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-2.00) + ((itemCost-2.00)* Tax)/100)))

        def coffee3():
            itemCost = 2.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Cappuccino","1","2.50"))
            self.txtReceipt.insert(END, ("Cappuccino" +"\t\t\t" + "1" + "\t\t\t" + "2.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-2.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-2.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-2.50) + ((itemCost-2.50)* Tax)/100)))

        def coffee4():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Vienna Coffee","1","3.00"))
            self.txtReceipt.insert(END, ("Vienna Coffee" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        def coffee5():
            itemCost = 3.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Coffee Shake","1","3.50"))
            self.txtReceipt.insert(END, ("Coffee Shake" +"\t\t\t" + "1" + "\t\t\t" + "3.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.50) + ((itemCost-3.50)* Tax)/100)))

        def coffee6():
            itemCost = 3.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Irish Coffee","1","3.00"))
            self.txtReceipt.insert(END, ("Irish Coffee" +"\t\t\t" + "1" + "\t\t\t" + "3.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.00) + ((itemCost-3.00)* Tax)/100)))

        # ---- Menu Buttons - Drink Functions ----

        def drink1():
            itemCost = 1.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Soda Can","1","1.50"))
            self.txtReceipt.insert(END, ("Soda Can" +"\t\t\t" + "1" + "\t\t\t" + "1.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-1.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-1.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-1.50) + ((itemCost-1.50)* Tax)/100)))

        def drink2():
            itemCost = 2.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Lemonade","1","2.00"))
            self.txtReceipt.insert(END, ("Lemonade" +"\t\t\t" + "1" + "\t\t\t" + "2.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-2.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-2.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-2.00) + ((itemCost-2.00)* Tax)/100)))

        def drink3():
            itemCost = 2.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Strwbry Lmnade","1","2.50"))
            self.txtReceipt.insert(END, ("Strwbry Lmnade" +"\t\t\t" + "1" + "\t\t\t" + "2.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-2.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-2.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-2.50) + ((itemCost-2.50)* Tax)/100)))

        def drink4():
            itemCost = 2.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Iced Tea","1","2.00"))
            self.txtReceipt.insert(END, ("Iced Tea" +"\t\t\t" + "1" + "\t\t\t" + "2.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-2.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-2.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-2.00) + ((itemCost-2.00)* Tax)/100)))

        def drink5():
            itemCost = 3.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Smoothie","1","3.50"))
            self.txtReceipt.insert(END, ("Smoothie" +"\t\t\t" + "1" + "\t\t\t" + "3.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.50) + ((itemCost-3.50)* Tax)/100)))

        def drink6():
            itemCost = 3.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Boba Tea","1","3.50"))
            self.txtReceipt.insert(END, ("Boba Tea" +"\t\t\t" + "1" + "\t\t\t" + "3.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.50) + ((itemCost-3.50)* Tax)/100)))

        # ---- Menu Buttons - Food Functions ----

        def food1():
            itemCost = 5.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Veg Sandwich","1","5.00"))
            self.txtReceipt.insert(END, ("Veg Sandwich" +"\t\t\t" + "1" + "\t\t\t" + "5.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-5.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-5.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-5.00) + ((itemCost-5.00)* Tax)/100)))

        def food2():
            itemCost = 5.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Ham Sandwich","1","5.00"))
            self.txtReceipt.insert(END, ("Ham Sandwich" +"\t\t\t" + "1" + "\t\t\t" + "5.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-5.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-5.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-5.00) + ((itemCost-5.00)* Tax)/100)))

        def food3():
            itemCost = 4.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Egg Sandwich","1","4.00"))
            self.txtReceipt.insert(END, ("Egg Sandwich" +"\t\t\t" + "1" + "\t\t\t" + "4.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-4.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-4.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-4.00) + ((itemCost-4.00)* Tax)/100)))

        def food4():
            itemCost = 3.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Grilled Cheese","1","3.50"))
            self.txtReceipt.insert(END, ("Grilled Cheese" +"\t\t\t" + "1" + "\t\t\t" + "3.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-3.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-3.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-3.50) + ((itemCost-3.50)* Tax)/100)))

        def food5():
            itemCost = 5.00
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Spinach Wrap","1","5.00"))
            self.txtReceipt.insert(END, ("Spinach Wrap" +"\t\t\t" + "1" + "\t\t\t" + "5.00" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-5.00)))
                Tax_Input.set(str('$%.2f'%(((itemCost-5.00)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-5.00) + ((itemCost-5.00)* Tax)/100)))

        def food6():
            itemCost = 4.50
            Tax = 4.7
            self.POS_receipt.insert("", tk.END, values=("Wheat Wrap","1","4.50"))
            self.txtReceipt.insert(END, ("Wheat Wrap" +"\t\t\t" + "1" + "\t\t\t" + "4.50" + "\n"))
            for child in self.POS_receipt.get_children():
                itemCost += float(self.POS_receipt.item(child, "values")[2])
                SubTotal_Input.set(str('$%.2f'%(itemCost-4.50)))
                Tax_Input.set(str('$%.2f'%(((itemCost-4.50)* Tax)/100)))
                Total_Input.set(str('$%.2f'%((itemCost-4.50) + ((itemCost-4.50)* Tax)/100)))

        # ---- CalFrame widget ----

        self.lblSubTotal = Label(CalFrame, font=('Arial', 14, 'bold'), text="Subtotal", bd=5)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txtSubTotal = Entry(CalFrame, font=('Arial', 14, 'bold'), bd=2, width=24, justify = 'left',
                                textvariable = SubTotal_Input )
        self.txtSubTotal.grid(row=0, column=1)

        self.lblTax = Label(CalFrame, font=('Arial', 14, 'bold'), text="Tax", bd=5)
        self.lblTax.grid(row=1, column=0, sticky=W, padx=5)
        self.txtTax = Entry(CalFrame, font=('Arial', 14, 'bold'), bd=2, width=24, justify = 'left',
                                textvariable = Tax_Input )
        self.txtTax.grid(row=1, column=1)

        self.lblTotal = Label(CalFrame, font=('Arial', 14, 'bold'), text="Total", bd=5)
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5)
        self.txtTotal = Entry(CalFrame, font=('Arial', 14, 'bold'), bd=2, width=24, justify = 'left',
                                textvariable = Total_Input )
        self.txtTotal.grid(row=2, column=1)

        # ---- ChangeFrame widget ----

        self.lblPayment = Label(ChangeFrame, font=('Arial', 14, 'bold'), text="Payment Method", bd=2)
        self.lblPayment.grid(row=0, column=0, sticky=W, padx=2)

        self.cboPayment = ttk.Combobox(ChangeFrame, width=36, font=('Arial', 14, 'bold'), state='readonly',
                                    textvariable=choice, justify=RIGHT)
        self.cboPayment['values'] = ('', 'Cash', 'Debit', 'Credit')
        self.cboPayment.current(0)
        self.cboPayment.grid(row=0, column=1)

        self.lblCost = Label(ChangeFrame, font=('Arial', 14, 'bold'), text="Total Cost", bd=5)
        self.lblCost.grid(row=1, column=0, sticky=W, padx=2)
        self.txtCost = Entry(ChangeFrame, font=('Arial', 14, 'bold'), bd=2, width=38, textvariable=Cash_Input, justify=RIGHT)
        self.txtCost.grid(row=1, column=1)
        self.txtCost.insert(0, "0")

        self.lblChange = Label(ChangeFrame, font=('Arial', 14, 'bold'), text="Change", bd=5)
        self.lblChange.grid(row=2, column=0, sticky=W, padx=2)
        self.txtChange = Entry(ChangeFrame, font=('Arial', 14, 'bold'), bd=2, textvariable=Change_Input, width=38, justify=RIGHT)
        self.txtChange.grid(row=2, column=1, sticky=W)

        # ---- Buttons, Pay, Print, Remove, Reset ----

        self.btnPay = Button(RemoveFrame, padx=2, font=('Arial', 15, 'bold'), text="Pay", width=10, height=1, bd=2,
                            command = giveChange)
        self.btnPay.grid(row=0, column=0, padx=4, pady=2)

        self.btnPrint = Button(RemoveFrame, padx=2, font=('Arial', 15, 'bold'), text="Print", width=10, height=1, bd=2,
                                command = iPrint)
        self.btnPrint.grid(row=1, column=1, padx=4, pady=2)

        self.btnReset = Button(RemoveFrame, padx=2, font=('Arial', 15, 'bold'), text="Reset", width=10, height=1, bd=2,
                                command = btnClear)
        self.btnReset.grid(row=1, column=0, padx=4, pady=2)

        self.btnRemoveItem = Button(RemoveFrame, padx=2, font=('Arial', 15, 'bold'), text="Remove Item", width=10, height=1, bd=2,
                                    command = delete)
        self.btnRemoveItem.grid(row=0, column=1, padx=4, pady=2)


        # ---- Buttons, Keypad 9, 8, 7 ----

        self.btn7 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="7", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(7))
        self.btn7.grid(row=0, column=0)

        self.btn8 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="8", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(8))
        self.btn8.grid(row=0, column=1)

        self.btn9 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="9", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(9))
        self.btn9.grid(row=0, column=2)

        # ---- Buttons, Keypad 6, 5, 4 ----

        self.btn4 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="4", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(4))
        self.btn4.grid(row=1, column=0)

        self.btn5 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="5", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(5))
        self.btn5.grid(row=1, column=1)

        self.btn6 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="6", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(6))
        self.btn6.grid(row=1, column=2)

        # ---- Buttons, Keypad 3, 2, 1 ----

        self.btn1 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="1", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(1))
        self.btn1.grid(row=2, column=0)

        self.btn2 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="2", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(2))
        self.btn2.grid(row=2, column=1)

        self.btn3 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="3", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(3))
        self.btn3.grid(row=2, column=2)

        # ---- Buttons, Keypad C, Dot, 0 ----

        self.btn0 = Button(KeypadFrame, padx=13, pady=22, font=('Arial', 20, 'bold'), text="0", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick(0))
        self.btn0.grid(row=3, column=0)

        self.btnDot = Button(KeypadFrame, padx=12, pady=22, font=('Arial', 20, 'bold'), text=" .", bd=8,
                            bg='#5b5b5b', command = lambda:btnClick('.'))
        self.btnDot.grid(row=3, column=1)

        self.btnC = Button(KeypadFrame, padx=11, pady=22, font=('Arial', 20, 'bold'), text="C", bd=8, bg='#5b5b5b',
                        command = clear)
        self.btnC.grid(row=3, column=2)

        # ---- Treeview, All Items Widget ----

        scroll_y = Scrollbar(ReceiptFrame, orient=VERTICAL)
        self.POS_receipt = ttk.Treeview(ReceiptFrame, height=20, columns=("Item", "Qty", "Total"),
                                        yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.POS_receipt.heading("Item", text="Item")
        self.POS_receipt.heading("Qty", text="Quantity")
        self.POS_receipt.heading("Total", text="Total")

        self.POS_receipt['show'] = 'headings'

        self.POS_receipt.column("Item", width=120)
        self.POS_receipt.column("Qty", width=60)
        self.POS_receipt.column("Total", width=70)

        self.POS_receipt.pack(fill=BOTH, expand=1)
        self.POS_receipt.bind("<ButtonRelease-1>")

        self.txtReceipt = Text(ReceiptFrame, width=79, height=1, font=('Arial', 6, 'bold'))
        self.txtReceipt.pack()

        self.txtReceipt.insert(END, "Item\t\t\t\t Qty\t\t\t Total\t\n")

        # ---- Menu Button Images - Cakes ----

        self.btnCake1 = Button(FoodItemFrame, padx=2, image = self.cake1, width=104, height=104, bd=2,
                                command = cake1)
        self.btnCake1.grid(row=0, column=0, padx=4, pady=2)

        self.btnCake2 = Button(FoodItemFrame, padx=2, image = self.cake2, width=104, height=104, bd=2,
                                command = cake2)
        self.btnCake2.grid(row=0, column=1, padx=4, pady=2)

        self.btnCake3 = Button(FoodItemFrame, padx=2, image = self.cake3, width=104, height=104, bd=2,
                                command = cake3)
        self.btnCake3.grid(row=0, column=2, padx=4, pady=2)

        self.btnCake4 = Button(FoodItemFrame, padx=2, image = self.cake4, width=104, height=104, bd=2,
                                command = cake4)
        self.btnCake4.grid(row=0, column=3, padx=4, pady=2)

        self.btnCake5 = Button(FoodItemFrame, padx=2, image = self.cake5, width=104, height=104, bd=2,
                                command = cake5)
        self.btnCake5.grid(row=0, column=4, padx=4, pady=2)

        self.btnCake6 = Button(FoodItemFrame, padx=2, image = self.cake6, width=104, height=104, bd=2,
                                command = cake6)
        self.btnCake6.grid(row=0, column=5, padx=4, pady=2)

        # ---- Menu Button Images - Coffee ----

        self.btnCoffee1 = Button(FoodItemFrame, padx=2, image = self.coffee1, width=104, height=104, bd=2,
                                command = coffee1)
        self.btnCoffee1.grid(row=1, column=0, padx=4, pady=2)

        self.btnCoffee2 = Button(FoodItemFrame, padx=2, image = self.coffee2, width=104, height=104, bd=2,
                                command = coffee2)
        self.btnCoffee2.grid(row=1, column=1, padx=4, pady=2)

        self.btnCoffee3 = Button(FoodItemFrame, padx=2, image = self.coffee3, width=104, height=104, bd=2,
                                command = coffee3)
        self.btnCoffee3.grid(row=1, column=2, padx=4, pady=2)

        self.btnCoffee4 = Button(FoodItemFrame, padx=2, image = self.coffee4, width=104, height=104, bd=2,
                                command = coffee4)
        self.btnCoffee4.grid(row=1, column=3, padx=4, pady=2)

        self.btnCoffee5 = Button(FoodItemFrame, padx=2, image = self.coffee5, width=104, height=104, bd=2,
                                command = coffee5)
        self.btnCoffee5.grid(row=1, column=4, padx=4, pady=2)

        self.btnCoffee6 = Button(FoodItemFrame, padx=2, image = self.coffee6, width=104, height=104, bd=2,
                                command = coffee6)
        self.btnCoffee6.grid(row=1, column=5, padx=4, pady=2)

        # ---- Menu Button Images - Drinks ----

        self.btnDrink1 = Button(FoodItemFrame, padx=2, image = self.drink1, width=104, height=104, bd=2,
                                command = drink1)
        self.btnDrink1.grid(row=2, column=0, padx=4, pady=2)

        self.btnDrink2 = Button(FoodItemFrame, padx=2, image = self.drink2, width=104, height=104, bd=2,
                                command = drink2)
        self.btnDrink2.grid(row=2, column=1, padx=4, pady=2)

        self.btnDrink3 = Button(FoodItemFrame, padx=2, image = self.drink3, width=104, height=104, bd=2,
                                command = drink3)
        self.btnDrink3.grid(row=2, column=2, padx=4, pady=2)

        self.btnDrink4 = Button(FoodItemFrame, padx=2, image = self.drink4, width=104, height=104, bd=2,
                                command = drink4)
        self.btnDrink4.grid(row=2, column=3, padx=4, pady=2)

        self.btnDrink5 = Button(FoodItemFrame, padx=2, image = self.drink5, width=104, height=104, bd=2,
                                command = drink5)
        self.btnDrink5.grid(row=2, column=4, padx=4, pady=2)

        self.btnDrink6 = Button(FoodItemFrame, padx=2, image = self.drink6, width=104, height=104, bd=2,
                                command = drink6)
        self.btnDrink6.grid(row=2, column=5, padx=4, pady=2)

        # ---- Menu Button Images - Food ----

        self.btnFood1 = Button(FoodItemFrame, padx=2, image = self.food1, width=104, height=104, bd=2,
                                command = food1)
        self.btnFood1.grid(row=3, column=0, padx=4, pady=2)

        self.btnFood2 = Button(FoodItemFrame, padx=2, image = self.food2, width=104, height=104, bd=2,
                                command = food2)
        self.btnFood2.grid(row=3, column=1, padx=4, pady=2)

        self.btnFood3 = Button(FoodItemFrame, padx=2, image = self.food3, width=104, height=104, bd=2,
                                command = food3)
        self.btnFood3.grid(row=3, column=2, padx=4, pady=2)

        self.btnFood4 = Button(FoodItemFrame, padx=2, image = self.food4, width=104, height=104, bd=2,
                                command = food4)
        self.btnFood4.grid(row=3, column=3, padx=4, pady=2)

        self.btnFood5 = Button(FoodItemFrame, padx=2, image = self.food5, width=104, height=104, bd=2,
                                command = food5)
        self.btnFood5.grid(row=3, column=4, padx=4, pady=2)

        self.btnFood6 = Button(FoodItemFrame, padx=2, image = self.food6, width=104, height=104, bd=2,
                                command = food6)
        self.btnFood6.grid(row=3, column=5, padx=4, pady=2)

# --- Calls the pos system to run and keeps it in a loop ---

if __name__=='__main__':
    root = Tk()
    application = pos(root)
    root.mainloop()
