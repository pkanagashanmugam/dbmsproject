import tkinter as tk
from tkinter import font
from PIL import ImageTk,Image
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="")
mycursor = mydb.cursor()
mydb.autocommit=True

root=tk.Tk()
root.title("Student Corner")
root.configure(bg="blue")


global val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,cost
val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,cost=0,0,0,0,0,0,0,0,0,0,0
global canvapage4,logincanva,canvapage2,canvapage3

def register():
    global canvapage4,logincanva
    logincanva.destroy()
    exist=mycursor.rowcount
    def add_details():
        query="Insert into user_details values (%s,%s,%s,%s)"
        mycursor.execute(query,(int(roll.get()),name.get(),int(phno.get()),passw.get()))
        if mycursor.rowcount>exist:
            print("Successfully registered")
        mydb.commit()   

    canvapage4=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage4.pack()

    frame1_image = Image.open("D:\\DBMS PROJECT\\regbg.jpeg")
    img1=frame1_image.resize((1000,600))
    photo= ImageTk.PhotoImage(img1)
    canvapage4.create_image(500,300,image=photo)

    loginfont=font.Font(family="Times New Roman",size=14)
    canvapage4.create_rectangle(60,60,470,530,fill="black")
    canvapage4.create_text(265,100,text="REGISTER DETAILS",font=font.Font(family="Arial",size=20),fill="red")
    canvapage4.create_text(150,180,text="Roll Number: ",font=loginfont,fill="white")
    canvapage4.create_text(125,240,text="Name: ",font=loginfont,fill="white")
    canvapage4.create_text(137,300,text="Password: ",font=loginfont,fill="white")
    canvapage4.create_text(155,360,text="Phone Number: ",font=loginfont,fill="white")

    roll=tk.Entry(root)
    canvapage4.create_window(300,180,window=roll)
    name=tk.Entry(root)
    canvapage4.create_window(300,240,window=name)       
    passw=tk.Entry(root,show="*")
    canvapage4.create_window(300,300,window=passw)
    phno=tk.Entry(root)
    canvapage4.create_window(300,360,window=phno)

    frame2_image = Image.open("D:\DBMS PROJECT\O6cVp.png")
    frame3_image=frame2_image.resize((300,50))
    photo1= ImageTk.PhotoImage(frame3_image)

    bt=tk.Button(canvapage4,image=photo1,borderwidth=0,command=lambda:add_details())
    bt.place(x=110,y=450)

    root.mainloop()



def login():
    global canvapage4,logincanva
    def check():
        val=(entry1.get())
        if val.lower() in ["hutcafe","printout","coffeeday","reccafe","hekka","maggispot","aircraft"]:
            if entry2.get()=="rec123":
                #print("yes",entry1.get())
                logincanva.destroy()
                shoplog(val.lower())
                #print("check")
            else:
                logincanva.create_text(180,400,text="Try again!",font=loginfont,fill="red")
        else:
            val=int(val)
            mycursor.execute("Select * from user_details")
            passcheck=mycursor.fetchall()
            mydb.commit()
            #print(passcheck)
            for i in passcheck:
                #print(i)
                if i[0]==val:
                    passwordpy=i[3]
                    #print(entry2.get(),passwordpy)
            if passwordpy==entry2.get():
                selection(val)
            else:
                logincanva.create_text(180,400,text="Try again!",font=loginfont,fill="red")
            
            
    logincanva=tk.Canvas(root,height=500,width=800)
    logincanva.pack()
    logincanva.create_rectangle(0,0,400,500,fill="blue")
    logincanva.create_rectangle(20,10,380,490,fill="black")
    logincanva.create_rectangle(800,0,400,500,fill="black")
    loginfont=font.Font(family="Times New Roman",size=24)
    logincanva.create_text(190,190,text="LOGIN",font=loginfont,fill="white")
    loginfont=font.Font(family="Times New Roman",size=16)
    logincanva.create_text(90,250,text="Roll Number: ",font=loginfont,fill="white")

    logincanva.create_text(100,300,text="Password: ",font=loginfont,fill="white")
    entry1=tk.Entry(root)
    logincanva.create_window(240,250,window=entry1)
    entry2=tk.Entry(root,show="*")
    logincanva.create_window(240,300,window=entry2)

    lgp=Image.open("D:\\DBMS PROJECT\log.jpg")
    loginpic=lgp.resize((150,30))
    lp=ImageTk.PhotoImage(loginpic)
    lgbt=tk.Button(root,image=lp,borderwidth=0,command=lambda:check())
    lgbt.place(x=120,y=350)


    logincanva.create_text(130,430,text="Don't have an account?",font=(font.Font(family="Times New Roman",size=12)),fill="white")
    lgbt=tk.Button(root,text="Sign Up",borderwidth=0,highlightthickness=0,bd=0,command=lambda:register())
    lgbt.place(x=220,y=420)


    frame1_image = Image.open("D:\DBMS PROJECT\project.jpg")
    photo = ImageTk.PhotoImage(frame1_image)
    logincanva.create_image(600,200,image=photo)

    frame1_image2 = Image.open("D:\DBMS PROJECT\pic2.jpeg")
    photo2 = ImageTk.PhotoImage(frame1_image2)
    logincanva.create_image(190,75,image=photo2)

    root.mainloop()

def shoplog(shopc):
    global logincanva
    global chec
    logincanva.destroy()
    pending=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    pending.pack()
    loginfont=font.Font(family="Times New Roman",size=16)
    pending.create_text(500,50,text="PENDING ORDERS",font=loginfont,fill="red")
    pending.create_text(350,150,text="Roll Number\t\tItems\t\tQuantity",font=loginfont,fill="Orange")
    def checked(shopc,rollno,food,quan):
        global chec
        if shopc=="reccafe":
            query="Update rec_cafe set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
        if shopc=="hekka":
            #query="Update (%s) set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            #mycursor.execute(query,(shopc,"True",rollno,food,quan))
            query="Update hekka set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
            #chec.config(state=tk.DISABLED)
        if shopc=="hutcafe":
            #query="Update (%s) set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            #mycursor.execute(query,(shopc,"True",rollno,food,quan))
            query="Update hut_cafe set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
            #chec.config(state=tk.DISABLED)
        if shopc=="aircraft":
            #query="Update (%s) set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            #mycursor.execute(query,(shopc,"True",rollno,food,quan))
            query="Update aircraft set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
            #chec.config(state=tk.DISABLED)
        if shopc=="maggispot":
            #query="Update (%s) set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            #mycursor.execute(query,(shopc,"True",rollno,food,quan))
            query="Update maggispot set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
            #chec.config(state=tk.DISABLED)
        if shopc=="coffeeday":
            #query="Update (%s) set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            #mycursor.execute(query,(shopc,"True",rollno,food,quan))
            query="Update coffeeday set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
            #chec.config(state=tk.DISABLED)
        if shopc=="printout":
            #query="Update (%s) set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            #mycursor.execute(query,(shopc,"True",rollno,food,quan))
            query="Update printout set checkout=(%s) where roll_number=(%s) and items=(%s) and quantity=(%s)"
            mycursor.execute(query,("True",rollno,food,quan))
            #chec.config(state=tk.DISABLED)
            
        mycursor.execute("Select * from log_table")
        log=mycursor.fetchall()
        pending.create_text(400,500,text=log[-1])
        ###mydb.commit()
    if shopc=="reccafe":
        query="Select * from rec_cafe where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        #print(orders)
        ###mydb.commit()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'rec_cafe'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_rec_cafe before UPDATE ON rec_cafe FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from REC CAFE')
            """)'''
        #mydb.commit()
        for i in range(q):

            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")

            #mycursor.execute("show triggers on rec_cafe")
            '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'rec_cafe'
            """)'''
            #print(mycursor.fetchone())
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        #chec.configure(command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
        #mydb.commit()
        
    elif shopc=="hutcafe":
        query="Select * from hut_cafe where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'hut_cafe'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_hut_cafe before UPDATE ON hut_cafe FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from HUT CAFE')
            """)'''
        for i in range(q):
            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        mydb.commit()
    elif shopc=="hekka":
        query="Select * from hekka where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'hekka'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_hekka before UPDATE ON hut_cafe FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from HEKKA')
            """)'''
        for i in range(q):
            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        mydb.commit()
    #print(shopc=="maggispot")
    elif shopc=="maggispot":
        query="Select * from maggispot where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'maggispot'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_maggispot before UPDATE ON maggispot FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from MAGGISPOT')
            """)'''
        for i in range(q):
            print(orders[i])
            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        mydb.commit()
    elif shopc=="aircraft":
        query="Select * from aircraft where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'aircraft'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_aircraft before UPDATE ON aircraft FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from AIRCRAFT')
            """)'''
        for i in range(q):
            print(orders[i])
            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        mydb.commit()
    elif shopc=="coffeeday":
        query="Select * from coffeeday where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'coffeeday'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_coffeeday before UPDATE ON aircraft FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from COFFEE DAY')
            """)'''
        for i in range(q):
            print(orders[i])
            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        mydb.commit()
    elif shopc=="printout":
        query="Select * from printout where checkout=(%s)"
        mycursor.execute(query,("False",))
        orders=mycursor.fetchall()
        q=5 if 5<=len(orders) else len(orders)
        '''mycursor.execute("""
                SELECT trigger_name
                FROM information_schema.triggers
                WHERE event_object_table = 'printout'
            """)'''
        '''mycursor.execute("""
                CREATE TRIGGER my_trigger_printout before UPDATE ON printout FOR EACH ROW INSERT INTO log_table values ('An order has been checked out from PRINTOUT')
            """)'''
        for i in range(q):
            print(orders[i])
            textor=str(orders[i][0])+"    \t\t"+str(orders[i][1])+"\t\t\t"+str(orders[i][2])
            pending.create_text(350,(150+((i+1)*50)),text=textor,font=loginfont,fill="Black")
            chec=tk.Button(root,text="Checkout",bg="red",command=lambda:checked(shopc,orders[i][0],orders[i][1],orders[i][2]))
            chec.place(x=750,y=(135+((i+1)*50)))
        mydb.commit()
    root.mainloop()


def rec_cafe(val):
    cost=0
    #roll=val
    def generate_bill(val):
        global cost
        #global roll
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")
        price=[10,20,20,20,30,20,50,20,10,45]
        items=["Tea","Dosai","Pongal","Idly","Masala Dosa","Coffee","Meals","Puffs","Kitkat","Cake"]
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text")),int(but9.cget("text")),int(but10.cget("text"))]
        for i in range(10):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        insert=[]
        for j in range(10):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into rec_cafe values (%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nREC CAFE",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()

    global canvapage4,logincanva,canvapage2,canvapage3
    global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
    canvapage2.destroy()

    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()

    head=canvapage3.create_rectangle(34,29,299,75,fill="#FB6E6E")
    canvapage3.create_text(150,50,text="REC CAFE",font=("Arial",18))

    canvapage3.create_text(75,100,text="Tea: Rs.10",font=("Arial",14))

    #global val1
    #val1=0
    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
        #print(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
            
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)

    '''
    # load and resize the image
    image = Image.open("D:\DBMS PROJECT\8022263649_19ae5e9638_n.jpg")
    image1 = image.resize((50,50),Image.LANCZOS)
    #image1=ImageTk.PhotoImage(image)
    canvapage3.create_image(225, 225, image=ImageTk.PhotoImage(image1), anchor="nw")'''

    frame1_image = Image.open("D:\DBMS PROJECT\8022263649_19ae5e9638_n.jpg")
    img1=frame1_image.resize((147,136))
    photo= ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="Dosai: Rs.20",font=("Arial",14))

    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\Crispy Masala Dosa.jpg")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)



    canvapage3.create_text(475,100,text="Pongal: Rs.20",font=("Arial",14))


    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\pongal.jpg")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="Idly: Rs.20",font=("Arial",14))

    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\idl.jpg")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="Masala Dosa: Rs.30",font=("Arial",14))

    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\Masala Dosa.webp")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Coffee: Rs.20",font=("Arial",14))

    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=20,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\A Brief History of South Indian Filter Coffee.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="Meals: Rs.50",font=("Arial",14))

    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=250,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\Meals.jpg")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="Puffs: Rs.20",font=("Arial",14))

    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=480,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\puffs.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    canvapage3.create_text(675,350,text="Kitkat: Rs.10",font=("Arial",14))

    def inc9():
        global val9
        val9+=1
        but9["text"]=str(val9)
    def dec9():
        global val9
        val9-=1
        if val9>=0:
            but9["text"]=str(val9)
    but9=tk.Button(root,text=str(val1),width=5,height=1)
    but9.place(x=700,y=500)

    inc9_but = tk.Button(root, text="+", command=inc9)
    inc9_but.place(x=750,y=500)

    dec9_but = tk.Button(root, text="-", command=dec9)
    dec9_but.place(x=680,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\OIP (19).jpg")
    img9=frame1_image.resize((147,136))
    photo9= ImageTk.PhotoImage(img9)
    canvapage3.create_image(690,430,image=photo9)


    canvapage3.create_text(875,350,text="Cake: Rs.45",font=("Arial",14))

    def inc10():
        global val10
        val10+=1
        but10["text"]=str(val10)
    def dec10():
        global val10
        val10-=1
        if val10>=0:
            but10["text"]=str(val10)
    but10=tk.Button(root,text=str(val1),width=5,height=1)
    but10.place(x=900,y=500)

    inc10_but = tk.Button(root, text="+", command=inc10)
    inc10_but.place(x=950,y=500)

    dec10_but = tk.Button(root, text="-", command=dec10)
    dec10_but.place(x=880,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\OIP (16).jpg")
    img10=frame1_image.resize((147,136))
    photo10= ImageTk.PhotoImage(img10)
    canvapage3.create_image(890,430,image=photo10)


    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)
    
    root.mainloop()

def hut_cafe(val):
    global cost
    global canvapage4,logincanva,canvapage2,canvapage3
    global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
    global val1,val2,val3,val4,val5,val6,val7,val8,val9,val10
    canvapage2.destroy()
    cost=0
    def generate_bill(val):
        global cost
        items=["Tea","Dosai","Pongal","Idly","Masala Dosa","Coffee","Cavins","Chicken Puffs","Juice","Onion Dosa"]
        price=[10,20,20,20,30,20,25,30,30,35]
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text")),int(but9.cget("text")),int(but10.cget("text"))]
        for i in range(10):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        insert=[]
        for j in range(10):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into hut_cafe values(%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nHUT CAFE",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()

    #price=[10,20,20,20,35,20,50,20,10,45]
    
    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()

    head=canvapage3.create_rectangle(34,29,299,75,fill="#FB6E6E")
    canvapage3.create_text(150,50,text="HUT CAFE",font=("Arial",18))

    canvapage3.create_text(75,100,text="Tea: Rs.10",font=("Arial",14))

    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)



    frame1_image = Image.open("D:\DBMS PROJECT\\tea.jpg")
    img1=frame1_image.resize((147,136))
    photo = ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="Dosai: Rs.20",font=("Arial",14))

    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\\Dosa.jpeg")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)



    canvapage3.create_text(475,100,text="Pongal: Rs.20",font=("Arial",14))

    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\venn-pongal.jpg")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="Idly: Rs.20",font=("Arial",14))

    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\idly.jpg")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="Masala Dosa: Rs.30",font=("Arial",14))

    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\\Masala_dosa.webp")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Coffee: Rs.20",font=("Arial",14))

    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=20,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\regular-coffee.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="Cavins: Rs.25",font=("Arial",14))

    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=250,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\kavinsmilkshake.jpg")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="Chicken_Puffs: Rs.30",font=("Arial",14))

    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=480,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\chicken-puffs.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    canvapage3.create_text(675,350,text="juice: Rs.30",font=("Arial",14))

    def inc9():
        global val9
        val9+=1
        but9["text"]=str(val9)
    def dec9():
        global val9
        val9-=1
        if val9>=0:
            but9["text"]=str(val9)
    but9=tk.Button(root,text=str(val1),width=5,height=1)
    but9.place(x=700,y=500)

    inc9_but = tk.Button(root, text="+", command=inc9)
    inc9_but.place(x=750,y=500)

    dec9_but = tk.Button(root, text="-", command=dec9)
    dec9_but.place(x=680,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\juice.jpg")
    img9=frame1_image.resize((147,136))
    photo9= ImageTk.PhotoImage(img9)
    canvapage3.create_image(690,430,image=photo9)


    canvapage3.create_text(875,350,text="Onion_Dosa: Rs.35",font=("Arial",14))

    def inc10():
        global val10
        val10+=1
        but10["text"]=str(val10)
    def dec10():
        global val10
        val10-=1
        if val10>=0:
            but10["text"]=str(val10)
    but10=tk.Button(root,text=str(val1),width=5,height=1)
    but10.place(x=900,y=500)

    inc10_but = tk.Button(root, text="+", command=inc10)
    inc10_but.place(x=950,y=500)

    dec10_but = tk.Button(root, text="-", command=dec10)
    dec10_but.place(x=880,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\oniondosa.jpg")
    img10=frame1_image.resize((147,136))
    photo10= ImageTk.PhotoImage(img10)
    canvapage3.create_image(890,430,image=photo10)

    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)

    root.mainloop()

def aircraft(val):
    global cost
    global canvapage4,logincanva,canvapage2,canvapage3
    global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
    canvapage2.destroy()
    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()
    cost=0
    def generate_bill(val):
        global cost
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")
        items=["Tea","Rose Water","Water Melon","Idly","Samosa","Coffee","Sandwich","Puffs","Kitkat","Lime Juice"]
        price=[10,20,30,20,20,20,40,20,10,20]
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text")),int(but9.cget("text")),int(but10.cget("text"))]
        for i in range(10):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        insert=[]
        for j in range(10):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into aircraft values  (%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nAIRCRAFT",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()

        
    canvapage3.create_text(75,100,text="Tea: Rs.10",font=("Arial",14))

    val1=0
    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)


    '''
    # load and resize the image
    image = Image.open("D:\DBMS PROJECT\8022263649_19ae5e9638_n.jpg")
    image1 = image.resize((50,50),Image.LANCZOS)
    #image1=ImageTk.PhotoImage(image)
    canvapage3.create_image(225, 225, image=ImageTk.PhotoImage(image1), anchor="nw")'''

    frame1_image = Image.open("D:\DBMS PROJECT\8022263649_19ae5e9638_n.jpg")
    img1=frame1_image.resize((147,136))
    photo = ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="Rose_water: Rs.20",font=("Arial",14))

    val2=0
    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\\rose-milk.jpg")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)



    canvapage3.create_text(475,100,text="Water_melon: Rs.30",font=("Arial",14))

    val3=0
    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\Watermelon-Juice.jpg")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="Idly: Rs.20",font=("Arial",14))

    val4=0
    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\idl.jpg")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="Samosa: Rs.20",font=("Arial",14))

    val5=0
    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\\samosa.jpg")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Coffee: Rs.20",font=("Arial",14))

    val6=0
    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=20,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\regular-coffee.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="sandwich: Rs.40",font=("Arial",14))

    val7=0
    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=250,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\Vegetable-Sandwich.jpg")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="Puffs: Rs.20",font=("Arial",14))
    val8=0
    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=480,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\puffs.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    canvapage3.create_text(675,350,text="Kitkat: Rs.10",font=("Arial",14))

    val9=0
    def inc9():
        global val9
        val9+=1
        but9["text"]=str(val9)
    def dec9():
        global val9
        val9-=1
        if val9>=0:
            but9["text"]=str(val9)
    but9=tk.Button(root,text=str(val1),width=5,height=1)
    but9.place(x=700,y=500)

    inc9_but = tk.Button(root, text="+", command=inc9)
    inc9_but.place(x=750,y=500)

    dec9_but = tk.Button(root, text="-", command=dec9)
    dec9_but.place(x=680,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\OIP (19).jpg")
    img9=frame1_image.resize((147,136))
    photo9= ImageTk.PhotoImage(img9)
    canvapage3.create_image(690,430,image=photo9)


    canvapage3.create_text(875,350,text="lime juice: Rs.20",font=("Arial",14))

    val10=0
    def inc10():
        global val10
        val10+=1
        but10["text"]=str(val10)
    def dec10():
        global val10
        val10-=1
        if val10>=0:
            but10["text"]=str(val10)
    but10=tk.Button(root,text=str(val1),width=5,height=1)
    but10.place(x=900,y=500)

    inc10_but = tk.Button(root, text="+", command=inc10)
    inc10_but.place(x=950,y=500)

    dec10_but = tk.Button(root, text="-", command=dec10)
    dec10_but.place(x=880,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\lime juice.jpg")
    img10=frame1_image.resize((147,136))
    photo10= ImageTk.PhotoImage(img10)
    canvapage3.create_image(890,430,image=photo10)

    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)
    root.mainloop()

def hekka(val):
    global cost
    global canvapage4,logincanva,canvapage2,canvapage3
    global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
    canvapage2.destroy()
    
    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()
    cost=0
    def generate_bill(val):
        global cost
        
        price=[25,40,30,45,20,20,40,30,50,20]
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")    
        items=["Badam milk","Brownie","Cup Cake","Donuts","Mini Samosa","Coffee","Hot Chocolate","Juice","Cake","Lime Juice"]
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text")),int(but9.cget("text")),int(but10.cget("text"))]
        for i in range(10):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        insert=[]
        for j in range(10):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into hekka values (%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nHEKKA",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()


    head=canvapage3.create_rectangle(34,29,299,75,fill="#FB6E6E")
    canvapage3.create_text(150,50,text="HEKKA",font=("Arial",18))

    canvapage3.create_text(75,100,text="badam milk: Rs.25",font=("Arial",14))

    val1=0
    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\badam milk.jfif")
    img1=frame1_image.resize((147,136))
    photo = ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="Brownie: Rs.40",font=("Arial",14))

    val2=0
    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\\brownie.jfif")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)

    canvapage3.create_text(475,100,text="Cup Cake: Rs.30",font=("Arial",14))

    val3=0
    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\cupcake.jfif")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="donuts: Rs.45",font=("Arial",14))

    val4=0
    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\donuts.jfif")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="mini samosa Rs.20",font=("Arial",14))

    val5=0
    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\\mini samosa.jfif")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Coffee: Rs.20",font=("Arial",14))

    val6=0
    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=20,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\regular-coffee.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="Hot chocolate : Rs.40",font=("Arial",14))

    val7=0
    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=250,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\hot chocolate.jfif")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="juice: Rs.30",font=("Arial",14))
    val8=0
    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=480,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\juice.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    canvapage3.create_text(675,350,text="cake: Rs.50",font=("Arial",14))

    val9=0
    def inc9():
        global val9
        val9+=1
        but9["text"]=str(val9)
    def dec9():
        global val9
        val9-=1
        if val9>=0:
            but9["text"]=str(val9)
    but9=tk.Button(root,text=str(val1),width=5,height=1)
    but9.place(x=700,y=500)

    inc9_but = tk.Button(root, text="+", command=inc9)
    inc9_but.place(x=750,y=500)

    dec9_but = tk.Button(root, text="-", command=dec9)
    dec9_but.place(x=680,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\cake.jpg")
    img9=frame1_image.resize((147,136))
    photo9= ImageTk.PhotoImage(img9)
    canvapage3.create_image(690,430,image=photo9)


    canvapage3.create_text(875,350,text="lime juice: Rs.20",font=("Arial",14))

    val10=0
    def inc10():
        global val10
        val10+=1
        but10["text"]=str(val10)
    def dec10():
        global val10
        val10-=1
        if val10>=0:
            but10["text"]=str(val10)
    but10=tk.Button(root,text=str(val1),width=5,height=1)
    but10.place(x=900,y=500)

    inc10_but = tk.Button(root, text="+", command=inc10)
    inc10_but.place(x=950,y=500)

    dec10_but = tk.Button(root, text="-", command=dec10)
    dec10_but.place(x=880,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\lime juice.jpg")
    img10=frame1_image.resize((147,136))
    photo10= ImageTk.PhotoImage(img10)
    canvapage3.create_image(890,430,image=photo10)

    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)

    root.mainloop()


def coffee(val):
    global cost
    global canvapage4,logincanva,canvapage2,canvapage3
    global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
    canvapage2.destroy()
    
    cost=0
    def generate_bill(val):
        global cost
        price=[20,25,45,65,40,50,60,50,60,70]
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")
        insert=[]
        items=["Black coffee","Coffee","Brownie","Chilli Cheese Toastizza","Cold Coffee","Mango Shots","Croissant","Sandwich","Brainfreeze","Cup Noodles"]
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text")),int(but9.cget("text")),int(but10.cget("text"))]
        for i in range(10):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        for j in range(10):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into coffeeday values (%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nCAFE COFFEE DAY",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()

    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()

    head=canvapage3.create_rectangle(34,29,299,75,fill="#FB6E6E")
    canvapage3.create_text(150,50,text="COFFEE DAY",font=("Arial",18))

    canvapage3.create_text(75,100,text="Black Coffee: Rs.20",font=("Arial",14))

    val1=0
    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\blackcoffee.jpg")
    img1=frame1_image.resize((147,136))
    photo = ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="Coffee: Rs.25",font=("Arial",14))

    val2=0
    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\\coffeeday.jpg")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)



    canvapage3.create_text(475,100,text="Brownie: Rs.45",font=("Arial",14))

    val3=0
    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\coffeeday brownie.jpg")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="Chilli Cheese Toastizza: Rs.65",font=("Arial",10))

    val4=0
    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\chillichessetoastizza.jpg")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="Cold Coffee;Rs.40",font=("Arial",12))

    val5=0
    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\\coldcoffee.jpg")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Mango Shots: Rs.50",font=("Arial",12))

    val6=0
    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=20,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\mango shots.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="Croissant: Rs.60",font=("Arial",12))

    val7=0
    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=250,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\croissant.jpg")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="Sandwich: Rs.50",font=("Arial",14))
    val8=0
    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=480,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\coffeedaysandwich.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    canvapage3.create_text(675,350,text="Brainfreeze: Rs.60",font=("Arial",14))

    val9=0
    def inc9():
        global val9
        val9+=1
        but9["text"]=str(val9)
    def dec9():
        global val9
        val9-=1
        if val9>=0:
            but9["text"]=str(val9)
    but9=tk.Button(root,text=str(val1),width=5,height=1)
    but9.place(x=700,y=500)

    inc9_but = tk.Button(root, text="+", command=inc9)
    inc9_but.place(x=750,y=500)

    dec9_but = tk.Button(root, text="-", command=dec9)
    dec9_but.place(x=680,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\brainfreeze.jpg")
    img9=frame1_image.resize((147,136))
    photo9= ImageTk.PhotoImage(img9)
    canvapage3.create_image(690,430,image=photo9)


    canvapage3.create_text(875,350,text="Cup Noodles: Rs.70",font=("Arial",14))

    val10=0
    def inc10():
        global val10
        val10+=1
        but10["text"]=str(val10)
    def dec10():
        global val10
        val10-=1
        if val10>=0:
            but10["text"]=str(val10)
    but10=tk.Button(root,text=str(val1),width=5,height=1)
    but10.place(x=900,y=500)

    inc10_but = tk.Button(root, text="+", command=inc10)
    inc10_but.place(x=950,y=500)

    dec10_but = tk.Button(root, text="-", command=dec10)
    dec10_but.place(x=880,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\Cup noodles.jpg")
    img10=frame1_image.resize((147,136))
    photo10= ImageTk.PhotoImage(img10)
    canvapage3.create_image(890,430,image=photo10)

    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)

    root.mainloop()
def printout(val):
    canvapage2.destroy()
    items=["Gel Pen","A4 sheet","Marker","Blue Pen","Black Pen","Cello Tape","Note Book","Pencil"]
    cost=0
    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()

    def generate_bill(val):
        global cost
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")
        insert=[]
        price=[10,1,15,5,5,10,40,10]
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text"))]
        for i in range(8):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        for j in range(8):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into printout values (%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nPRINTOUT",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()
    def printo(val):
        global cost
        canvapage3.destroy()
        prinpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        prinpage.pack()
        prinre=prinpage.create_rectangle(300,50,700,550,fill="black")
        prinpage.create_text(500,100,text="   PRINTOUT",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        prinpage.create_text(400,200,text="Drive Link:",font=(font.Font(family="Times",size=12)),fill="white")
        prinpage.create_text(400,300,text="No.of copies:",font=(font.Font(family="Times",size=12)),fill="white")
        drive=tk.Text(root,height=5,width=20)
        drive.place(x=500,y=185)
        cop=tk.Entry(root)
        prinpage.create_window(570,300,window=cop)
        prinpage.create_text(390,350,text="No.of pages:",font=(font.Font(family="Times",size=12)),fill="white")
        pag=tk.Entry(root)
        prinpage.create_window(570,350,window=pag)
        cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_printbill(val))
        cont.place(x=880,y=550)
        def generate_printbill(val):
            cost=int(cop.get())*int(pag.get())
            o=(val,drive.get("1.0", tk.END),int(cop.get()),cost,"False")
            mycursor.execute("Insert into printout values (%s,%s,%s,%s,%s)",o)
            mydb.commit()
            t="Grand Total=",cost
            prinpage.create_text(600,500,text=t,fill="white")
            root.mainloop()

    head=canvapage3.create_rectangle(34,29,299,75,fill="#FB6E6E")
    canvapage3.create_text(150,50,text="STATIONERY SHOP",font=("Arial",18))

    canvapage3.create_text(75,100,text="Gel Pen: Rs.10",font=("Arial",14))

    val1=0
    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\gel pen.jpg")
    img1=frame1_image.resize((147,136))
    photo = ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="A4 sheet: Rs.1",font=("Arial",14))

    val2=0
    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\\a4.jpg")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)



    canvapage3.create_text(475,100,text="Marker: Rs.15",font=("Arial",14))

    val3=0
    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\marker.jpg")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="Blue pen: Rs.5",font=("Arial",14))

    val4=0
    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\ball pen.jpg")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="Black pen: Rs.5",font=("Arial",14))

    val5=0
    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\\black pen.jpg")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Cello Cape: Rs.10",font=("Arial",14))

    val6=0
    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=15,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\cello tape.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="Note Book: Rs.40",font=("Arial",14))

    val7=0
    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=245,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\notebook.jpg")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="pencil: Rs.10",font=("Arial",14))
    val8=0
    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=475,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\pencil.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    printou=tk.Button(root,text="PRINTOUT",font=("Verdana",16),command=lambda:printo(val))
    printou.place(x=730,y=400)

    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)

    root.mainloop()
            
def maggi(val):
    global cost
    global canvapage4,logincanva,canvapage2,canvapage3
    global photo,photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8,photo9,photo10
    canvapage2.destroy()
    items=["Maggi","Cheese Maggi","Chilli Maggi","Garlic Maggi","Cold Coffee","Coffee","Hot Chocolate","Kitkat","Munch","Lime Juice"]
    cost=0
    def generate_bill(val):
        global cost
        canvapage3.destroy()
        billpage=tk.Canvas(root,height=600,width=1000,bg="#37358B")
        billpage.pack()
        bill=billpage.create_rectangle(300,50,700,550,fill="white")
        insert=[]
        price=[40,45,45,45,40,20,40,10,10,20]
        #print(but10.cget("text"))
        freq=[int(but1.cget("text")),int(but2.cget("text")),int(but3.cget("text")),int(but4.cget("text")),int(but5.cget("text")),int(but6.cget("text")),int(but7.cget("text")),int(but8.cget("text")),int(but9.cget("text")),int(but10.cget("text"))]
        for i in range(10):
            cost+=(freq[i]*price[i])
        string="Items\t\t\tQty\t\t\tAmount\n\n"
        for j in range(10):
            if freq[j]!=0:
                string+=items[j]+"\t\t\t"+str(freq[j])+"\t\t\t"+str(price[j])+"\n\n"
                insert.append((val,items[j],freq[j],price[j],"False"))
        for o in insert:
            mycursor.execute("Insert into maggispot values (%s,%s,%s,%s,%s)",o)
        mydb.commit()
        billpage.create_text(500,100,text="    BILL\nMAGGI HOTSPOT",font=(font.Font(family="Helvetica",size=16)),fill="Orange")
        billpage.create_text(500,150,text="==============================================")
        billpage.create_text(500,250,text=string)
        t="Grand Total=",cost
        billpage.create_text(600,500,text=t)
        root.mainloop()

    canvapage3=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage3.pack()

    head=canvapage3.create_rectangle(34,29,299,75,fill="#FB6E6E")
    canvapage3.create_text(150,50,text="MAGGI HOTSPOT",font=("Arial",18))

    canvapage3.create_text(75,100,text="Maggi: Rs.40",font=("Arial",14))

    val1=0
    def inc1():
        global val1
        val1+=1
        but1["text"]=str(val1)
    def dec1():
        global val1
        val1-=1
        if val1>=0:
            but1["text"]=str(val1)
    but1=tk.Button(root,text=str(val1),width=5,height=1)
    but1.place(x=50,y=260)

    inc1_but = tk.Button(root, text="+", command=inc1)
    inc1_but.place(x=100,y=260)

    dec1_but = tk.Button(root, text="-", command=dec1)
    dec1_but.place(x=30,y=260)


    '''
    # load and resize the image
    image = Image.open("D:\DBMS PROJECT\8022263649_19ae5e9638_n.jpg")
    image1 = image.resize((50,50),Image.LANCZOS)
    #image1=ImageTk.PhotoImage(image)
    canvapage3.create_image(225, 225, image=ImageTk.PhotoImage(image1), anchor="nw")'''

    frame1_image = Image.open("D:\DBMS PROJECT\\gingergarlic.jpg")
    img1=frame1_image.resize((147,136))
    photo = ImageTk.PhotoImage(img1)
    canvapage3.create_image(90,180,image=photo)



    canvapage3.create_text(275,100,text="Cheese maggie: Rs.45",font=("Arial",14))

    val2=0
    def inc2():
        global val2
        val2+=1
        but2["text"]=str(val2)
    def dec2():
        global val2
        val2-=1
        if val2>=0:
            but2["text"]=str(val2)
    but2=tk.Button(root,text=str(val2),width=5,height=1)
    but2.place(x=270,y=260)

    inc2_but = tk.Button(root, text="+", command=inc2)
    inc2_but.place(x=320,y=260)

    dec2_but = tk.Button(root, text="-", command=dec2)
    dec2_but.place(x=250,y=260)

    frame2_image = Image.open("D:\DBMS PROJECT\\cheese maggie.jpg")
    img2=frame2_image.resize((147,136))
    photo2= ImageTk.PhotoImage(img2)
    canvapage3.create_image(290,180,image=photo2)



    canvapage3.create_text(475,100,text="Chilli maggie: Rs.45",font=("Arial",14))

    val3=0
    def inc3():
        global val3
        val3+=1
        but3["text"]=str(val3)
    def dec3():
        global val3
        val3-=1
        if val3>=0:
            but3["text"]=str(val3)
    but3=tk.Button(root,text=str(val1),width=5,height=1)
    but3.place(x=480,y=260)

    inc3_but = tk.Button(root, text="+", command=inc3)
    inc3_but.place(x=530,y=260)

    dec3_but = tk.Button(root, text="-", command=dec3)
    dec3_but.place(x=460,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\chilli maggie.jpg")
    img3=frame1_image.resize((147,136))
    photo3= ImageTk.PhotoImage(img3)
    canvapage3.create_image(490,180,image=photo3)


    canvapage3.create_text(675,100,text="Garlic maggie: Rs.45",font=("Arial",14))

    val4=0
    def inc4():
        global val4
        val4+=1
        but4["text"]=str(val4)
    def dec4():
        global val4
        val4-=1
        if val4>=0:
            but4["text"]=str(val4)
    but4=tk.Button(root,text=str(val1),width=5,height=1)
    but4.place(x=650,y=260)

    inc4_but = tk.Button(root, text="+", command=inc4)
    inc4_but.place(x=700,y=260)

    dec4_but = tk.Button(root, text="-", command=dec4)
    dec4_but.place(x=630,y=260)

    frame1_image = Image.open("D:\DBMS PROJECT\\maggie.jpg")
    img4=frame1_image.resize((147,136))
    photo4= ImageTk.PhotoImage(img4)
    canvapage3.create_image(690,180,image=photo4)


    canvapage3.create_text(875,100,text="Cold Coffee;Rs.40",font=("Arial",14))

    val5=0
    def inc5():
        global val5
        val5+=1
        but5["text"]=str(val5)
    def dec5():
        global val5
        val5-=1
        if val5>=0:
            but5["text"]=str(val5)
    but5=tk.Button(root,text=str(val1),width=5,height=1)
    but5.place(x=900,y=250)

    inc5_but = tk.Button(root, text="+", command=inc5)
    inc5_but.place(x=950,y=250)

    dec5_but = tk.Button(root, text="-", command=dec5)
    dec5_but.place(x=880,y=250)

    frame1_image = Image.open("D:\DBMS PROJECT\\coldcoffee.jpg")
    img5=frame1_image.resize((147,136))
    photo5= ImageTk.PhotoImage(img5)
    canvapage3.create_image(890,180,image=photo5)

    canvapage3.create_text(75,350,text="Coffee: Rs.20",font=("Arial",14))

    val6=0
    def inc6():
        global val6
        val6+=1
        but6["text"]=str(val6)
    def dec6():
        global val6
        val6-=1
        if val6>=0:
            but6["text"]=str(val6)
    but6=tk.Button(root,text=str(val1),width=5,height=1)
    but6.place(x=40,y=500)

    inc6_but = tk.Button(root, text="+", command=inc6)
    inc6_but.place(x=90,y=500)

    dec6_but = tk.Button(root, text="-", command=dec6)
    dec6_but.place(x=20,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\regular-coffee.jpg")
    img6=frame1_image.resize((147,136))
    photo6= ImageTk.PhotoImage(img6)
    canvapage3.create_image(90,430,image=photo6)

    canvapage3.create_text(275,350,text="Hot chocolate : Rs.40",font=("Arial",14))

    val7=0
    def inc7():
        global val7
        val7+=1
        but7["text"]=str(val7)
    def dec7():
        global val7
        val7-=1
        if val7>=0:
            but7["text"]=str(val7)
    but7=tk.Button(root,text=str(val1),width=5,height=1)
    but7.place(x=270,y=500)

    inc7_but = tk.Button(root, text="+", command=inc7)
    inc7_but.place(x=320,y=500)

    dec7_but = tk.Button(root, text="-", command=dec7)
    dec7_but.place(x=250,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\hot chocolate.jfif")
    img7=frame1_image.resize((147,136))
    photo7= ImageTk.PhotoImage(img7)
    canvapage3.create_image(290,430,image=photo7)

    canvapage3.create_text(475,350,text="Kitkat: Rs.10",font=("Arial",14))
    val8=0
    def inc8():
        global val8
        val8+=1
        but8["text"]=str(val8)
    def dec8():
        global val8
        val8-=1
        if val8>=0:
            but8["text"]=str(val8)
    but8=tk.Button(root,text=str(val1),width=5,height=1)
    but8.place(x=500,y=500)

    inc8_but = tk.Button(root, text="+", command=inc8)
    inc8_but.place(x=550,y=500)

    dec8_but = tk.Button(root, text="-", command=dec8)
    dec8_but.place(x=480,y=500)


    frame1_image = Image.open("D:\DBMS PROJECT\\kitkat1.jpg")
    img8=frame1_image.resize((147,136))
    photo8= ImageTk.PhotoImage(img8)
    canvapage3.create_image(490,430,image=photo8)

    canvapage3.create_text(675,350,text="munch: Rs.10",font=("Arial",14))

    val9=0
    def inc9():
        global val9
        val9+=1
        but9["text"]=str(val9)
    def dec9():
        global val9
        val9-=1
        if val9>=0:
            but9["text"]=str(val9)
    but9=tk.Button(root,text=str(val1),width=5,height=1)
    but9.place(x=700,y=500)

    inc9_but = tk.Button(root, text="+", command=inc9)
    inc9_but.place(x=750,y=500)

    dec9_but = tk.Button(root, text="-", command=dec9)
    dec9_but.place(x=680,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\munch.jpg")
    img9=frame1_image.resize((147,136))
    photo9= ImageTk.PhotoImage(img9)
    canvapage3.create_image(690,430,image=photo9)


    canvapage3.create_text(875,350,text="lime juice: Rs.20",font=("Arial",14))

    val10=0
    def inc10():
        global val10
        val10+=1
        but10["text"]=str(val10)
    def dec10():
        global val10
        val10-=1
        if val10>=0:
            but10["text"]=str(val10)
    but10=tk.Button(root,text=str(val1),width=5,height=1)
    but10.place(x=900,y=500)

    inc10_but = tk.Button(root, text="+", command=inc10)
    inc10_but.place(x=950,y=500)

    dec10_but = tk.Button(root, text="-", command=dec10)
    dec10_but.place(x=880,y=500)

    frame1_image = Image.open("D:\DBMS PROJECT\\lime juice.jpg")
    img10=frame1_image.resize((147,136))
    photo10= ImageTk.PhotoImage(img10)
    canvapage3.create_image(890,430,image=photo10)

    cont=tk.Button(root,text="Continue",font=("Arial",16),borderwidth=0,bg="orange",command=lambda:generate_bill(val))
    cont.place(x=880,y=550)

    root.mainloop()



def selection(val):
    global canvapage4,logincanva,canvapage2,canvapage3
    logincanva.destroy()
    canvapage2=tk.Canvas(root,height=600,width=1000,bg="#37358B")
    canvapage2.pack()

    bgimg=ImageTk.PhotoImage(file="D:\DBMS PROJECT\choosebg.jpg")
    canvapage2.create_image(100,100,anchor=tk.NW,image=bgimg)
    canvapage2.lower(bgimg)

    canvapage2.create_oval(191,178,46,57,fill="#FBED6E",outline="black")
    bt1=tk.Button(canvapage2,text="REC CAFE",font=("Arial",12),command=lambda:rec_cafe(val))
    bt1.place(x=70,y=105)

    canvapage2.create_oval(177,284,23,440,fill="#FBED6E",outline="black")
    bt2=tk.Button(canvapage2,text="MAGGI\nHOTSPOT",font=("Arial",12),command=lambda:maggi(val))
    bt2.place(x=50,y=335)

    canvapage2.create_oval(201,171,324,79,fill="#FBED6E",outline="black")
    bt3=tk.Button(canvapage2,text="HEKKA",font=("Arial",12),command=lambda:hekka(val))
    bt3.place(x=230,y=110)

    canvapage2.create_oval(180,200,405,418,fill="#FBED6E",outline="black")
    bt4=tk.Button(canvapage2,text="HUT CAFE",font=("Arial",16),command=lambda:hut_cafe(val))
    bt4.place(x=220,y=280)

    '''canvapage2.create_oval(359,76,532,244,fill="#FBED6E",outline="black")
    bt5=tk.Button(canvapage2,text="HUT CAFE 1",font=("Arial",14))
    bt5.place(x=380,y=130)

    canvapage2.create_oval(396,324,592,532,fill="#FBED6E",outline="black")
    bt6=tk.Button(canvapage2,text="HUT CAFE 4",font=("Arial",12))
    bt6.place(x=437,y=405)

    canvapage2.create_oval(552,46,713,200,fill="#FBED6E",outline="black")
    bt7=tk.Button(canvapage2,text="HUT CAFE 2",font=("Arial",12))
    bt7.place(x=575,y=100)'''

    canvapage2.create_oval(602,209,782,388,fill="#FBED6E",outline="black")
    bt8=tk.Button(canvapage2,text="PRINTOUT",font=("Arial",12),command=lambda:printout(val))
    bt8.place(x=643,y=280)

    canvapage2.create_oval(652,397,809,561,fill="#FBED6E",outline="black")
    bt9=tk.Button(canvapage2,text="AIRCRAFT",font=("Arial",12),command=lambda:aircraft(val))
    bt9.place(x=688,y=470)

    canvapage2.create_oval(732,12,974,252,fill="#FBED6E",outline="black")
    bt10=tk.Button(canvapage2,text="CAFE\nCOFFEE\nDAY",font=("Arial",20),command=lambda:coffee(val))
    bt10.place(x=784,y=69)

    '''canvapage2.create_oval(774,267,974,455,fill="#FBED6E",outline="black")
    bt11=tk.Button(canvapage2,text="HUT CAFE 5",font=("Arial",16))
    bt11.place(x=810,y=340)'''

    root.mainloop()

login()
