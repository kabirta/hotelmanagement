from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking



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
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()

