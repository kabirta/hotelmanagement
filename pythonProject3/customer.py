from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        self.root.geometry("1295x550+230+220")

        # ==================== veriables==============

        self.ver_ref = StringVar()
        x = random.randint(1000, 9999)
        self.ver_ref.set(str(x))

        # ===============title===================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("time new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ====================logo=================
        img2 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_logo.place(x=5, y=2, width=100, height=40)

        # =====================lebelFrame================
        lebelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("time new roman", 12, "bold"))
        lebelframeleft.place(x=5, y=50, width=425, height=490)

        # ================== Labels and Entries =====================
        # Customer Ref
        lbl_cust_ref = Label(lebelframeleft, text="Customer Ref", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        self.var_ref = StringVar()

        entry_random_ref = ttk.Entry(lebelframeleft, textvariable=self.ver_ref, font=("arial", 13, "bold"),
                                     state="readonly")
        entry_random_ref.grid(row=0, column=1)

        # Customer Name
        lbl_cust_name = Label(lebelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_name.grid(row=1, column=0, sticky=W)

        self.var_cust_name = StringVar()
        enty_name = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_cust_name, font=("arial", 13, "bold"))
        enty_name.grid(row=1, column=1)

        # Mother's Name
        lbl_mother_name = Label(lebelframeleft, text="Mother's Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mother_name.grid(row=2, column=0, sticky=W)

        self.var_mother = StringVar()
        enty_mother_name = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_mother, font=("arial", 13, "bold"))
        enty_mother_name.grid(row=2, column=1)

        # Gender ComboBox
        lbl_gender = Label(lebelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        self.var_gender = StringVar()
        combo_gender = ttk.Combobox(lebelframeleft, font=("arial", 13, "bold"), width=27, state="readonly",
                                    textvariable=self.var_gender)
        combo_gender['values'] = ('Male', 'Female', 'Other')
        combo_gender.grid(row=3, column=1)

        # Postcode
        lbl_postcode = Label(lebelframeleft, text="Postcode", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_postcode.grid(row=4, column=0, sticky=W)

        self.var_post = StringVar()
        enty_postcode = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_post, font=("arial", 13, "bold"))
        enty_postcode.grid(row=4, column=1)

        # Mobile Number
        lbl_mobile = Label(lebelframeleft, text="Mobile Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_mobile.grid(row=5, column=0, sticky=W)

        self.var_mobile = StringVar()
        enty_mobile = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_mobile, font=("arial", 13, "bold"))
        enty_mobile.grid(row=5, column=1)

        # Email
        lbl_email = Label(lebelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_email.grid(row=6, column=0, sticky=W)

        self.var_email = StringVar()
        enty_email = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_email, font=("arial", 13, "bold"))
        enty_email.grid(row=6, column=1)

        # Nationality
        lbl_nationality = Label(lebelframeleft, text="Nationality", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_nationality.grid(row=7, column=0, sticky=W)

        self.var_nationality = StringVar()
        enty_nationality = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_nationality,
                                     font=("arial", 13, "bold"))
        enty_nationality.grid(row=7, column=1)

        # ID Type ComboBox
        lbl_id_type = Label(lebelframeleft, text="ID Type", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id_type.grid(row=8, column=0, sticky=W)

        self.var_id_proof = StringVar()
        combo_id_proof = ttk.Combobox(lebelframeleft, font=("arial", 13, "bold"), width=27, state="readonly",
                                      textvariable=self.var_id_proof)
        combo_id_proof['values'] = ('Aadhar', 'Voter ID', 'Passport', 'Driving Licence')
        combo_id_proof.grid(row=8, column=1)

        # ID Number
        self.var_id_number = StringVar()

        lbl_id_number = Label(lebelframeleft, text="ID Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_id_number.grid(row=9, column=0, sticky=W)

        enty_id_number = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_id_number,
                                   font=("arial", 13, "bold"))
        enty_id_number.grid(row=9, column=1)

        # Address Label
        lbl_address = Label(lebelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_address.grid(row=10, column=0, sticky=W)

        self.var_address = StringVar()
        # Address Entry
        enty_address = ttk.Entry(lebelframeleft, width=29, textvariable=self.var_address, font=("arial", 13, "bold"))
        enty_address.grid(row=10, column=1)

        # Buttons Frame
        btn_frame = Frame(lebelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        # Add Button
        btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=(3, 2))

        # Update Button
        btnUpdate = Button(btn_frame, text="UPDATE", command=self.update_data, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=(3, 2))

        # Delete Button
        btnDelete = Button(btn_frame, text="DELETE", command=self.delete_data, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=(3, 2))

        # Reset Button
        btnReset = Button(btn_frame, text="RESET", command=self.reset_data, font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=(2, 5))

        # =============table frame =================
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Service System",
                                 font=("time new roman", 12, "bold"))
        table_frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(table_frame, font=("arial", 12, "bold"), text="Search By", bg="red", fg="white")
        lblSearchBy.grid(row=9, column=0, sticky=W)

        # Search ComboBox
        self.combo_search = ttk.Combobox(table_frame, font=("arial", 12), width=13, state="readonly")
        self.combo_search['values'] = ('Mobile Number', 'Customer Ref')
        self.combo_search.current(0)
        self.combo_search.grid(row=9, column=1, padx=(5, 0), sticky=W)

        # Search Entry
        self.lbl_Search = ttk.Entry(table_frame, font=("arial", 12, "bold"), width=12)
        self.lbl_Search.grid(row=9, column=2, padx=2, pady=6, )

        # Search Button
        btnSearch = Button(table_frame, text="Search", command=self.search_data, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=9, column=3, padx=2)

        # Show All Button
        btnShowAll = Button(table_frame, text="Show All", command=self.show_all_data, font=("arial", 11, "bold"),
                            bg="black",
                            fg="gold", width=10)
        btnShowAll.grid(row=9, column=4, padx=2)

        # ============= show data Table==========

        details_table = Frame(table_frame, bd=2, relief=RIDGE)

        details_table.place(x=0, y=50, width=595, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL, style='Horizontal.TScrollbar')
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL, style='Vertical.TScrollbar')

        self.Cust_Details_Table = ttk.Treeview(details_table,
                                               columns=("ref", "name", "mother", "gender", "post", "mobile",
                                                        "email", "nationality", "id_proof", "id_number", "address"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side='bottom', fill='x')
        scroll_y.pack(side='right', fill='y')

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("id_proof", text="Id Proof")
        self.Cust_Details_Table.heading("id_number", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("id_proof", width=100)
        self.Cust_Details_Table.column("id_number", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cuersor)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def add_data(self):
        required_fields = ["mobile", "mother"]
        for field in required_fields:
            if getattr(self, f"var_{field}").get() == "":
                messagebox.showerror("Error", f"{field.capitalize()} is a required field", parent=self.root)
                return

        try:
            with mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345678",
                    database="customer"
            ) as conn:
                my_cursor = conn.cursor()

                ref_value = self.var_ref.get()

                my_cursor.execute(
                    "INSERT INTO customer1 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.ver_ref.get(),
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_id_proof.get(),
                        self.var_id_number.get(),
                        self.var_address.get()
                    )
                )

                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Unexpected Error", f"An error occurred: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="12345678", database="customer")

        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer1")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
        conn.close()


    def get_cuersor(self,event=""):
        curses_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(curses_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update_data(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678",
                                               database="customer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "UPDATE customer1 SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Adress=%s WHERE Ref=%s",
                    (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(),
                     self.var_post.get(), self.var_mobile.get(), self.var_email.get(),
                     self.var_nationality.get(), self.var_id_proof.get(), self.var_id_number.get(),
                     self.var_address.get(), self.var_ref.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer details updated", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        selected_row = self.Cust_Details_Table.focus()

        if not selected_row:
            messagebox.showerror("Error", "Please select a record to delete", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345678",
                                               database="customer")
                my_cursor = conn.cursor()

                delete_confirmation = messagebox.askyesno("Confirmation", "Do you really want to delete this record?",
                                                          parent=self.root)

                if delete_confirmation:
                    selected_data = self.Cust_Details_Table.item(selected_row)
                    ref_value = selected_data['values'][0]

                    my_cursor.execute("DELETE FROM customer1 WHERE Ref=%s", (ref_value,))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Customer details deleted", parent=self.root)

                    # Refresh the table after deletion
                    self.fetch_data()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def reset_data(self):

        self.var_cust_name.set("")
        self.var_mother.set("")
        #self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        #self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")


        x = random.randint(1000, 9999)
        self.ver_ref.set(str(x))

    def search_data(self):
        selected_search = self.combo_search.get()
        search_value = self.lbl_Search.get()

        if selected_search == "Mobile Number":
            column_name = "Mobile"
        elif selected_search == "Customer Ref":
            column_name = "Ref"
        else:
            messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
            return

        try:
            with mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="12345678",
                    database="customer"
            ) as conn:
                my_cursor = conn.cursor()

                my_cursor.execute(f"SELECT * FROM customer1 WHERE {column_name}=%s", (search_value,))
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                    for i in rows:
                        self.Cust_Details_Table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Information", "No matching records found", parent=self.root)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Unexpected Error", f"An error occurred: {str(es)}", parent=self.root)

    def show_all_data(self):
        try:
            with mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="12345678",
                    database="customer"
            ) as conn:
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT * FROM customer1")
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                    for i in rows:
                        self.Cust_Details_Table.insert("", END, values=i)
                else:
                    messagebox.showinfo("Information", "No records found", parent=self.root)

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Unexpected Error", f"An error occurred: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()