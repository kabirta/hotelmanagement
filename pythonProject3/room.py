from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import time
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkinter import Tk


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1295x550+230+220")

        # ==========variables========≠=======

        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal = StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ===============title===================
        lbl_title = Label(self.root, text="Room Booking", font=("time new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ====================logo=================
        img2 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_logo.place(x=5, y=2, width=100, height=40)

        # =====================lebelFrame================
        lebelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details",
                                    font=("time new roman", 12, "bold"))
        lebelframeleft.place(x=5, y=50, width=425, height=490)

        # =====================lebelFrame================
        lebelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Details",
                                    font=("time new roman", 12, "bold"))
        lebelframeleft.place(x=5, y=50, width=425, height=490)

        # Customer contact
        lbl_cust_contact = Label(lebelframeleft, text="Customer Contact", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(lebelframeleft, textvariable=self.var_contact,font=("arial", 13, "bold"), width=20)
        entry_contact.grid(row=0, column=1, sticky=W)
        # Fetch data button
        btnFetchData = Button(lebelframeleft,command=self.Fetch_contact,text="Fetch Data", font=("arial", 8, "bold"), bg="black", fg="gold",width=8)
        btnFetchData.place(x=347, y=4)

        # Check-in Date
        lbl_check_in_date = Label(lebelframeleft, text="Check-in Date", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_check_in_date.grid(row=1, column=0, sticky=W)

        entry_check_in_date = ttk.Entry(lebelframeleft,textvariable=self.var_checkin, font=("arial", 13, "bold"), width=25)
        entry_check_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_check_out_date = Label(lebelframeleft, text="Check-out Date", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_check_out_date.grid(row=2, column=0, sticky=W)

        entry_check_out_date = ttk.Entry(lebelframeleft,textvariable=self.var_checkout,font=("arial", 13, "bold"), width=25)
        entry_check_out_date.grid(row=2, column=1)

        # Room Type
        lbl_room_type = Label(lebelframeleft, text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)

        entry_room_type = ttk.Combobox(lebelframeleft,textvariable=self.var_roomtype,font=("arial", 12, "bold"), width=23)
        entry_room_type["value"]=("Single","Double","Laxary")
        entry_room_type.grid(row=3, column=1)

        # Available Room
        lbl_available_room = Label(lebelframeleft, text="Available Room", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_available_room.grid(row=4, column=0, sticky=W)

        entry_available_room = ttk.Entry(lebelframeleft,textvariable=self.var_roomavailable,font=("arial", 13, "bold"), width=25)
        entry_available_room.grid(row=4, column=1)

        # Meal
        lbl_meal = Label(lebelframeleft, text="Meal", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)

        entry_meal = ttk.Entry(lebelframeleft,textvariable=self.var_meal, font=("arial", 13, "bold"), width=25)
        entry_meal.grid(row=5, column=1)

        # No Of Days
        lbl_no_of_days = Label(lebelframeleft, text="No Of Days", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)

        entry_no_of_days = ttk.Entry(lebelframeleft,textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=25)
        entry_no_of_days.grid(row=6, column=1)

        # Paid Tax
        lbl_paid_tax = Label(lebelframeleft, text="Paid Tax", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_paid_tax.grid(row=7, column=0, sticky=W)

        entry_paid_tax = ttk.Entry(lebelframeleft,textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=25)
        entry_paid_tax.grid(row=7, column=1)

        # Total Cost
        lbl_total_cost = Label(lebelframeleft, text="Total Cost", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_total_cost.grid(row=9, column=0, sticky=W)

        entry_total_cost = ttk.Entry(lebelframeleft,textvariable=self.var_total,font=("arial", 13, "bold"), width=25)
        entry_total_cost.grid(row=9, column=1)

        #==========================bill button==================
        btnBill = Button(lebelframeleft, text="BILL",command=self.total, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnBill.grid(row=10, column=0, padx=(3, 2),sticky=W)


        #==========================button======================

        # Buttons Frame
        btn_frame = Frame(lebelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        # Add Button
        btnAdd = Button(btn_frame, text="ADD",command=self.add_data,font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=(3, 2))

        # Update Button
        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update_data, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=(3, 2))

        # Delete Button
        btnDelete = Button(btn_frame, text="DELETE",command=self.mDelete ,font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=(3, 2))

        # Reset Button
        btnReset = Button(btn_frame, text="RESET", command=self.reset_data ,font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=(2, 5))

        #===============Right side image===============
        img3 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\bed.jpg")
        img3 = img3.resize((520, 230), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl_logo = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbl_logo.place(x=760, y=55, width=520, height=230)

        # =============table frame =================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Service System",
                                 font=("time new roman", 12, "bold"))
        table_frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(table_frame, font=("arial", 12, "bold"), text="Search By", bg="red", fg="white")
        lblSearchBy.grid(row=9, column=0, sticky=W)


        #=====================labal frame search system=================

        # Search ComboBox
        self.search_var = StringVar()
        self.txt_search = Entry()
        self.combo_search = ttk.Combobox(table_frame,textvariable=self.search_var ,font=("arial", 12), width=13, state="readonly")
        self.combo_search['values'] = ('Contact', 'Room')
        self.combo_search.current(0)
        self.combo_search.grid(row=9, column=1, padx=(5, 0), sticky=W)

        # Search Entry
        self.lbl_Search = ttk.Entry(table_frame,font=("arial", 12, "bold"), width=12)
        self.lbl_Search.grid(row=9, column=2, padx=2, pady=6, )

        # Search Button
        btnSearch = Button(table_frame, text="Search" ,command=self.search,font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=9, column=3, padx=2)

        # Show All Button
        btnShowAll = Button(table_frame, text="Show All",command=self.fetch_data, font=("arial", 11, "bold"),
                            bg="black",
                            fg="gold", width=10)
        btnShowAll.grid(row=9, column=4, padx=2)


      # ============= show data Table==========
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=595, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL, style='Horizontal.TScrollbar')
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL, style='Vertical.TScrollbar')

        self.room_Table = ttk.Treeview(details_table,
                                       columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal",
                                                "noOfdays"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side='bottom', fill='x')
        scroll_y.pack(side='right', fill='y')

        scroll_x.config(command=self.room_Table.xview)
        scroll_y.config(command=self.room_Table.yview)

        self.room_Table.heading("contact", text="Contact")
        self.room_Table.heading("checkin", text="Check-in")
        self.room_Table.heading("checkout", text="Check-out")
        self.room_Table.heading("roomtype", text="Room Type")
        self.room_Table.heading("roomavailable", text="Room No")
        self.room_Table.heading("meal", text="Meal")
        self.room_Table.heading("noOfdays", text="No Of Days")

        self.room_Table["show"] = "headings"

        self.room_Table.column("contact", width=100)
        self.room_Table.column("checkin", width=100)
        self.room_Table.column("checkout", width=100)
        self.room_Table.column("roomtype", width=100)
        self.room_Table.column("roomavailable", width=100)
        self.room_Table.column("meal", width=100)
        self.room_Table.column("noOfdays", width=100)

        self.room_Table.pack(fill=BOTH, expand=1)
        self.room_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678",
                                               database="customer")
                my_cursor = conn.cursor()

                # Print values for debugging
                print("Values to be inserted:", self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(),
                      self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(),
                      self.var_noofdays.get())

                my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                  (self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(),
                                   self.var_roomtype.get(), self.var_roomavailable.get(), self.var_meal.get(),
                                   self.var_noofdays.get()))

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success", "Room booked", parent=self.root)

            except mysql.connector.Error as err:
                print(f"MySQL Error: {err}")
                messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
            except Exception as es:
                print(f"An unexpected error occurred: {str(es)}")
                messagebox.showwarning("Unexpected Error", f"An error occurred: {str(es)}", parent=self.root)

    #fatch data
    def fetch_data(self):

        conn = mysql.connector.connect(host="localhost", username="root", password="12345678",database="customer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows)!= 0:
            self.room_Table.delete(*self.room_Table.get_children())
            for i in rows:
                self.room_Table.insert("",END,values=i)

            conn.commit()
        conn.close()
     #============get cursor============++++
    def get_cursor(self,event=""):
        selected_row = self.room_Table.focus()
        content = self.room_Table.item(selected_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
    #=============Update function===========

    def update_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        else:


            conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="customer")
            my_cursor = conn.cursor()

            update_query = "UPDATE room SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s WHERE contact=%s"
            print(update_query)  # Add this line to print the SQL statement
            my_cursor.execute(update_query, (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()
                                       ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Room details updated", parent=self.root)

            #==============delete button=================


    def mDelete(self):

        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer",
                                              parent=self.root)

        if mDelete:
            conn = mysql.connector.connect(host="localhost", user="root", password="12345678",
                                                   database="customer")
            my_cursor = conn.cursor()
            query = "DELETE FROM room WHERE Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Customer deleted", parent=self.root)
        else:
            return

            #============Reset===================

    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    #============Fetch contact================
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678",
                                               database="customer")
                my_cursor = conn.cursor()

                # Fetching all details using a single query
                query = "SELECT * FROM customer1 WHERE Mobile = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                conn.close()

                if row is None:
                    messagebox.showerror("Error", "Number not found", parent=self.root)
                else:
                    # Displaying details in a new frame
                    showDataframe = Frame(self.root, bg="lightblue", relief=RIDGE, padx=2)
                    showDataframe.place(x=455, y=55, width=300, height=180)

                    lblName = Label(showDataframe, text="Name", font=("arial", 12, "bold"))
                    lblName.place(x=0, y=0)
                    lbl = Label(showDataframe, text=row[1], font=("arial", 12, "bold"))
                    lbl.place(x=90, y=0)

                    lblGender = Label(showDataframe, text="Gender", font=("arial", 12, "bold"))
                    lblGender.place(x=0, y=30)
                    lbl2 = Label(showDataframe, text=row[3], font=("arial", 12, "bold"))
                    lbl2.place(x=90, y=30)

                    lblEmail = Label(showDataframe, text="Email", font=("arial", 12, "bold"))
                    lblEmail.place(x=0, y=60)
                    lbl_email_value = Label(showDataframe, text=row[6], font=("arial", 12, "bold"))
                    lbl_email_value.place(x=90, y=60)

                    lblNationality = Label(showDataframe, text="Nationality", font=("arial", 12, "bold"))
                    lblNationality.place(x=0, y=90)
                    lbl_nationality_value = Label(showDataframe, text=row[7], font=("arial", 12, "bold"))
                    lbl_nationality_value.place(x=90, y=90)

                    lblAddress = Label(showDataframe, text="Adress", font=("arial", 12, "bold"))
                    lblAddress.place(x=0, y=120)
                    lbl_address_value = Label(showDataframe, text=row[10], font=("arial", 12, "bold"))
                    lbl_address_value.place(x=90, y=120)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"MySQL Error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self.root)

        #search system

    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="customer")
            my_cursor = conn.cursor()

            column_to_search = "roomavailable"
            search_query = f"SELECT * FROM room WHERE {column_to_search} LIKE %s"

            search_string = f"%{self.txt_search.get()}%"
            my_cursor.execute(search_query, (search_string,))

            rows = my_cursor.fetchall()

            if len(rows) != 0:
                # Clear existing data in room_Table
                self.room_Table.delete(*self.room_Table.get_children())

                # Insert the fetched data into room_Table
                for row in rows:
                    self.room_Table.insert("", END, values=row)

                conn.commit()
            else:
                messagebox.showinfo("No Results", "No matching records found")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"MySQL Error: {err}")
        finally:
            if conn.is_connected():
                conn.close()

    def total(self):
        inDate = datetime.strptime(self.var_checkin.get(), "%d/%m/%Y")
        outDate = datetime.strptime(self.var_checkout.get(), "%d/%m/%Y")
        self.var_noofdays.set(abs((outDate - inDate).days))

        q1 = float(300)
        q2 = float(700)
        q3 = float(self.var_noofdays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)

        if self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury":
            # Assuming Luxury room type has a different price for breakfast
            q6 = float(100)
            q5 += q6

        tax = "Rs." + str("%.2f" % (q5 * 0.1))
        ST = "Rs." + str("%.2f" % q5)
        TT = "Rs." + str("%.2f" % (q5 + (q5 * 0.1)))

        self.var_paidtax.set(tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()