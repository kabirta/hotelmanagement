from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

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


if __name__ == "__main__":

    root = Tk()
    app = Register(root)
    root.mainloop()



