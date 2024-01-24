
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from customer import Cust_Win
from room import Roombooking
from hotel import HotelManagementSystem
import random

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.var_pass = StringVar()
        self.var_email = StringVar()









        # ===========background image==============

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\kabir\OneDrive\Desktop\hotel management system\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)



        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        # Icon image
        img1 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)
        #======Get started lable=========
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95,y=100)

        #label
        #username
        username=lbl=Label(frame,text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70,y=155)


        self.txtuser=ttk.Entry(frame,font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40,y=180,width=270)
        #password
        password = lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        #icon image
        img2 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\LoginIconAppl.png")
        img2 = img2.resize((25, 25), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(self.root, image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\lock-512.png")
        img3 = img3.resize((25, 25), Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(self.root, image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        #Login button


        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman", 15, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground='white',activebackground='red')
        loginbtn.place(x=110,y=300,width=120,height=35)

        #===========registerbutton======

        registerbtn = Button(frame, text="New User Register",command=self.register_window ,font=("times new roman", 10, "bold"),borderwidth=0, fg="white",bg="black", activeforeground='white', activebackground='black')
        registerbtn.place(x=15, y=350, width=160)

        #====== forgot button=========

        forgetpassbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"),borderwidth=0, fg="white", bg="black", activeforeground='white', activebackground='black')
        forgetpassbtn.place(x=10, y=370, width=160,)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field required")
        elif self.txtuser.get()=="kabir" and self.txtpass.get()=="tamu":
            messagebox.showinfo("Success", "Welcome to Hotelmanagement system")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="customer")
            my_cur = conn.cursor()
            my_cur.execute("SELECT * FROM register WHERE Email=%s AND Password=%s", ('kabir@gmail.com', '123'))

            row = my_cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:

                    self.new_window = Toplevel(self.root)  
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #===============veriable==========
        self.var_fname = StringVar()
        self.var_Iname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background image
        img = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        self.bg = ImageTk.PhotoImage(img)
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # Background image
        img1 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\thought-good-morning-messages-LoveSove.jpg")
        self.bg1 = ImageTk.PhotoImage(img1)
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(x=50, y=100, width=470, height=550)


        #   main frame===
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        regiser_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="dark green",bg="white")
        regiser_lbl.place(x=20,y=20)

        fname = Label(frame, text="First Name",font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(frame,textvariable=self.var_fname , font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=370, y=100)

        lname_entry = ttk.Entry(frame,textvariable=self.var_Iname ,font=("times new roman", 15, "bold"))
        lname_entry.place(x=370, y=130, width=250)
        # secound rows
        contact = Label(frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)

        contact_entry = ttk.Entry(frame,textvariable=self.var_contact ,font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        self.var_email = StringVar()
        email_entry = ttk.Entry(frame,textvariable=self.var_email ,font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=200, width=250)

        # Security Question
        sec_q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        sec_q.place(x=50, y=240)

        # List of questions for combobox
        questions = ["Best friend's name", "First pet's name", "Your birth place"]

        sec_q_combo = ttk.Combobox(frame, values=questions,textvariable=self.var_securityQ ,font=("times new roman", 15, "bold"))
        sec_q_combo.place(x=50, y=270, width=250)

        # Security Answer
        sec_a = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        sec_a.place(x=370, y=240)

        sec_a_entry = ttk.Entry(frame,textvariable=self.var_securityA ,font=("times new roman", 15, "bold"))
        sec_a_entry.place(x=370, y=270, width=250)

        # Password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=310)
        self.var_pass = StringVar()
        password_entry = ttk.Entry(frame,textvariable=self.var_pass ,font=("times new roman", 15, "bold"))
        password_entry.place(x=50, y=340, width=250)

        # Confirm Password
        confirm_password = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_password.place(x=370, y=310)

        confirm_password_entry = ttk.Entry(frame,textvariable=self.var_confpass ,font=("times new roman", 15, "bold"))
        confirm_password_entry.place(x=370, y=340, width=250)

        # Terms and Conditions
        self.var_check = IntVar()
        check_button = Checkbutton(frame, text="", variable=self.var_check, onvalue=1, offvalue=0, bg="white")
        check_button.place(x=50, y=380)

        terms = Label(frame, text="I Agree The Terms and Conditions", font=("times new roman", 12, "bold"), bg="white")
        terms.place(x=90, y=380)

        # Load the image using PIL
        pil_img = Image.open("C:/Users/kabir/OneDrive/Desktop/hotel management system/register-now-button1.jpg")

        # Resize the image
        pil_img = pil_img.resize((200, 50),Image.LANCZOS)

        # Convert the PIL image object to Tkinter-compatible photo image object
        img5 = ImageTk.PhotoImage(pil_img)

        # Create the button
        register_button = Button(frame,command=self.register_data ,image=img5)
        register_button.place(x=50, y=430)

        # Keep a reference to the image to prevent it from being garbage collected
        register_button.image = img5

        # Load the image using PIL
        pil_img2 = Image.open("C:/Users/kabir/OneDrive/Desktop/hotel management system/loginpng.png")

        # Resize the image
        pil_img2 = pil_img2.resize((200, 50), Image.LANCZOS)

        # Convert the PIL image object to Tkinter-compatible photo image object
        img6 = ImageTk.PhotoImage(pil_img2)

        # Create the button
        login_button = Button(frame, image=img6)
        login_button.place(x=300, y=430)

        # Keep a reference to the image to prevent it from being garbage collected
        login_button.image = img6

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and condition")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="12345678", database="customer")
            cur = conn.cursor()
            query = "ALTER TABLE register MODIFY COLUMN Firstname VARCHAR(45);"
            cur.execute(query)  # execute without value

            query = "SELECT * FROM register WHERE Email=%s"
            value = (self.var_email.get(),)
            cur.execute(query, value)
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "user already exist ")
            else:
                cur.execute("INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_Iname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register successfully")




class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel management system")
        root.geometry("1550x800+0+0")  # Corrected the size format
        # =================1st img================
        img1 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\hotel1.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1550, height=140)

        # ====================logo=================
        img2 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\logohotel.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=230, height=140)
       #===============title===================

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("time new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #==================main frame=================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
        #===================manu==================++++++++

        lbl_manu = Label(main_frame, text="MANU", font=("time new roman", 20, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_manu.place(x=0, y=0, width=230)

        #===============button======================

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("time new roman", 14, "bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="ROOM", width=22,command=self.roombooking ,font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="logout", width=22, font=("time new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)


        #======================right side image=================

        img3 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=225, y=0, width=1310, height=590)

        #=====================down images ===================

        img4 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\myh.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(r"C:\Users\kabir\OneDrive\Desktop\hotel management system\khana.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app = Roombooking(self.new_window)


if __name__ == "__main__":
    main()


