### Import For GUI
from tkinter import *
# from PIL import Image,ImageTk
import tkinter.messagebox as tmsg
from tkinter import ttk
### Import Ends for GUI

### Import For Database

import sqlite3 as sql ## this I have just included sqlite3 for my database work as sql


connector = sql.connect("Sports_and_hostel_for_Student.db")
cur = connector.cursor()
"""
   The next line to it I have made try-except block if you are running it first time 
   it will generate all the tables in it otherwise it will through u an excepiton
   which is printed
   NOTE:If u want to add more tables to it create table at starting of try-except
"""
try:
    cur.execute(""" CREATE TABLE Student_login(
                        Roll_no INT UNIQUE,
                        Password varchar
                        );""")
    cur.execute("""CREATE TABLE Admin_login(
                        ID varchar UNIQUE,
                        Password varchar
                        );""")
    cur.execute(""" CREATE TABLE Coach_login(
                        ID varchar UNIQUE NOT NULL,
                        Name varchar NOT NULL,
                        Mobile INT UNIQUE NOT NULL ,
                        Email varchar,
                        gender varchar NOT NULL,
                        Password varchar
                        );""")
    cur.execute(""" CREATE TABLE Warden_login(
                        ID varchar UNIQUE NOT NULL,
                        Name varchar NOT NULL,
                        Mobile int UNIQUE NOT NULL,
                        Email varchar ,
                        Gender varchar NOT NULL,
                        Password varchar
                        );""")
    cur.execute(""" CREATE TABLE Student_details(
                        Name varchar NOT NULL,
                        Branch Varchar NOT NULL,
                        Sem Int NOT NULL,
                        Roll_no INt unique NOT NULL,
                        Phone_number Int NOT NULL 
                        );""")
    cur.execute(""" CREATE TABLE Sports(
                        Roll_no Int NOT NULL ,
                        Name varchar,
                        Branch varchar,
                        Sem int,
                        Participation_in varchar
                );""")
    cur.execute("""CREATE TABLE Sports_status_and_places(
                        Sports_name varchar,
                        Sports_status varchar,
                        Sports_places varchar
                );""")
    cur.execute("""CREATE TABLE Sports_request(
                        Roll_no int ,
                        Name varchar,
                        Branch varchar,
                        Sem Int,
                        Want_to_participate_in varchar
                );""")
    cur.execute("""CREATE TABLE Sports_request_accepted_or_rejected(
                        Roll_no int, 
                        Name varchar,
                        Sports_name varchar 

                );""")
    cur.execute("""CREATE TABLE Hostel(
                        Roll_no int unique NOT NULL,
                        Name varchar,
                        Branch varchar,
                        Sem Int,
                        fees_status varchar NOT NULL,
                        Room_no int
                );""")
    cur.execute(""" CREATE TABLE Hostel_rooms_status(
                        Room_no int unique,
                        No_of_spaces int

                );""")
    cur.execute("""CREATE TABLE Hostel_room_nos(
                        Starting_room_no int,
                        Ending_room_no int 
                );""")
    cur.execute("""CREATE TABLE Hostel_request(
                        Roll_no int unique,
                        Name varchar,
                        Branch varchar,
                        Sem Int
                );""")
    cur.execute("""INSERT INTO Admin_login(ID,Password) VALUES ('Deepak@1','Tewatia@1');""")
    cur.execute("""INSERT INTO Hostel_room_nos(Starting_room_no,Ending_room_no) VALUES (1,80);""")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Volleyball','Free','Volleyball Court')")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Basketball','Free','Baseketball Court')")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Football','Free','Main Ground')")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Kabbdi','Free','Shakuntalam')")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Table Tennis','Free','Shakuntalam')")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Badminton','Free','Shakuntalam')")
    cur.execute("INSERT INTO Sports_status_and_places(Sports_name,Sports_status,Sports_places) values ('Cricket','Free','Main Ground')")
    cur.execute("SELECT Ending_room_no from Hostel_room_nos")
    x=cur.fetchone()
    for i in range(1,x[0]+1):
        cur.execute("INSERT INTO Hostel_rooms_status(Room_no,No_of_spaces) VALUES(?,3)",(i,))
    connector.commit()  
except Exception as e:
    print(e)
else:
    print("Successfully Done!!")

### Import For Database ends with generating tables within it and inserting some values


### Lists used inside these function

SPORTS = ['Volleyball','Basketball','Football','Kabbdi','Table Tennis','Badminton','Cricket']
Cllg_branches = ['Btech.IT','Btech.CE','Btech.CIVIL','Btech.Mech','Btech.ECE','Btech.DataScience','Bsc.Maths','Bsc.Physics','Bsc.Chemistry']
Gender = ['Male','Female','Other']
Fee = ['Paid','Not Paid']
STATUS = ['Free','Occupied']
### Lists ends

### Functions Starts

###Making windows Center
def Make_Center(app_width,app_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    w = int(( screen_width / 2) - (app_width/2))
    h = int(( screen_height / 2 - 30) - (app_height/2))
    return [w,h]
###Making windows Center ends

### Rate Menu Functions
def About():
    tmsg.showinfo('About','This version is created by Deepak\nFor any query mail at deepaktewatia2000@gmail.com')

def Rate():
    tmsg.showinfo('Not now','For now you will not be able to rate us')   

### Rate Menu Functions ends 


### Menubutton in each starts to define it in a function then to use it

def Go_back(cmd):
    backmenu = Menu(root)
    backmenu.add_command(label='Go back',command=cmd)
    root.config(menu=backmenu)



def Go_backandmain(cmd):
    backmenu = Menu(root)
    backmenu.add_command(label='Go back',command=cmd)
    backmenu.add_command(label='Log Out',command=Main_Menu)

    root.config(menu=backmenu)

### menubutton code ends here 



### Admin block Start
def Admin_Submit_Student():
    name = name_111.get()
    branch = branch_111.get()
    sem = sem_111.get()
    roll_no = roll_no_111.get()
    phone_no = phone_no_111.get()

    if name =='' or branch == '' or sem == 0 or roll_no == 0 or len(str(phone_no))!= 10:
        tmsg.showinfo('Not Filled','All details are not Filled')
    elif sem >8 or sem < 0:
        tmsg.showinfo('No','Either you have entered sem less than 0 or it is greater than 8')
    else:
        try:
            cur.execute('INSERT INTO Student_details(Name,Branch,Sem,Roll_no,Phone_number) VALUES(?,?,?,?,?)',(name,branch,sem,roll_no,phone_no,))
            x = str(phone_no)[:6]+'@'+name[:3]
            cur.execute('INSERT INTO Student_login(Roll_no,Password) VALUES(?,?)',(roll_no,x,))
            connector.commit()
            Admin_Add_student()
        except sql.IntegrityError:
            tmsg.showinfo('Already Exists','Student already in your College no need to add again!')
        except Exception as e:
            tmsg.showinfo('Error',f'Either you have entered something wrong or there is some issue.\n{e}')
        else:
            tmsg.showinfo('Done','Data Entered Successfully \n Student login is also created!')

    
def Admin_Add_student():
    global root
    root.destroy()
    
    root = Tk()
    w,h = Make_Center(480,330)
    root.geometry(f'480x330+{w}+{h}')
    root.minsize(480,330)
    root.maxsize(480,330)
    root.title('Student Detail')

    Go_backandmain(Admin_function)
      

    name = Label(root,text="Student Name*:",font='lucida 20 bold',padx=5,pady=5)
    name.grid(row=1,column=2)
    branch = Label(root,text="Branch*:",font='lucida 20 bold',padx=5,pady=5)
    branch.grid(row=2,column=2)
    sem = Label(root,text="Sem*:",font='lucida 20 bold',padx=5,pady=5)
    sem.grid(row=3,column=2)
    roll_no = Label(root,text="Roll Number*:",font='lucida 20 bold',padx=5,pady=5)
    roll_no.grid(row=4,column=2)
    phone_no = Label(root,text="Phone Number*:",font='lucida 20 bold',padx=5,pady=5)
    phone_no.grid(row=5,column=2)

    global name_111,branch_111,sem_111,roll_no_111,phone_no_111

    name_111 = StringVar(root) 
    branch_111 = StringVar(root)
    sem_111 = IntVar(root)
    roll_no_111 = IntVar(root)
    phone_no_111 = IntVar(root)

    nameEntry = Entry(root,textvariable=name_111,font='lucida 16 ')
    nameEntry.grid(row=1,column=3)
    branchEntry = ttk.Combobox(root,textvariable=branch_111,font='lucida 14 ')
    branchEntry['values'] = Cllg_branches 
    branchEntry.grid(row=2,column=3)
    branchEntry.current()
    semEntry = Entry(root,textvariable=sem_111,font='lucida 16 ')
    semEntry.grid(row=3,column=3)
    roll_noValue = Entry(root,textvariable=roll_no_111,font='lucida 16 ')
    roll_noValue.grid(row=4,column=3)
    phone_noValue = Entry(root,textvariable=phone_no_111,font='lucida 16 ')
    phone_noValue.grid(row=5,column=3)

    Button(root,text='Submit',bg='blue',fg='white',command=Admin_Submit_Student,width=10,font='lucida 20 bold',relief=GROOVE,border=10).grid(row=6,column=3)
    Button(root,text='Close',bg='red',fg='white',command=quit,width=8,font='lucida 20 bold',relief=GROOVE,border=10).grid(row=6,column=2)

def Admin_Submit_Warden():
    Id = ID_w.get()
    name = Name_w.get()
    mobile = mobile_w.get()
    email = email_w.get()
    gender = gender_w.get()
    password = str(mobile)[:6] + '@'+name[:3]
    if Id =='' or name =='' or gender == '' or mobile==0:
        tmsg.showinfo('No','Please Important details ')
    elif len(str(mobile)) != 10:
        tmsg.showinfo('Not 10','Your Number is not of 10 digit')
    elif gender not in Gender:
        tmsg.showinfo('No','Please select gender from list given')
    else:        
        try:
            cur.execute('INSERT INTO Warden_login VALUES(?,?,?,?,?,?)',(Id,name,mobile,email,gender,password,))
            connector.commit()
            Admin_Add_Warden()
        except:
            tmsg.showinfo('Error','There is some issue in entering Data!')
        else:
            tmsg.showinfo('Done','Successfully Done!')


def Admin_Add_Warden():
    global root
    root.destroy() 
    root = Tk()
    w,h = Make_Center(420,320)
    root.geometry(f'420x320+{w}+{h}')
    root.minsize(420,320)
    root.maxsize(420,320)
    root.title('Add Warden Details')
    Go_backandmain(Admin_function)

    Label(root,text='ID*:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=1)
    Label(root,text='Name*:',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=1)
    Label(root,text='Mobile*:',font='lucida 20 bold',padx=5,pady=5).grid(row=2,column=1)
    Label(root,text='Email:',font='lucida 20 bold',padx=5,pady=5).grid(row=3,column=1)
    Label(root,text='Gender*:',font='lucida 20 bold',padx=5,pady=5).grid(row=4,column=1)


    global ID_w,Name_w,mobile_w,email_w,gender_w

    ID_w = StringVar(root)
    Name_w = StringVar(root)
    mobile_w = IntVar(root)
    email_w = StringVar(root)
    gender_w = StringVar(root)


    Id_wEntry = Entry(root,textvariable=ID_w,font='lucida 16 ')
    Id_wEntry.grid(row=0,column=2)
    NameEntry = Entry(root,textvariable=Name_w,font='lucida 16 ')
    NameEntry.grid(row=1,column=2)
    MobileEntry = Entry(root,textvariable=mobile_w,font='lucida 16')
    MobileEntry.grid(row=2,column=2)
    emailEntry = Entry(root,textvariable=email_w,font='lucida 16')
    emailEntry.grid(row=3,column=2)
    genderEntry = ttk.Combobox(root,textvariable=gender_w,font='lucida 14')
    genderEntry['values'] = Gender
    genderEntry.grid(row=4,column=2)
    genderEntry.current(0)
    Button(root,text='Close',bg='red',fg='white',command=quit,width=6,font='lucide 20 bold',relief=GROOVE,border=10).grid(row=5,column=1)
    Button(root,text='Create',bg='blue',fg='white',command=Admin_Submit_Warden,width=8,font='lucide 20 bold',relief=GROOVE,border=10).grid(row=5,column=2)


def Admin_Submit_Coach():
    Id = ID_c.get()
    name = Name_c.get()
    mobile = mobile_c.get()
    email = email_c.get()
    gender = gender_c.get()
    password = str(mobile)[:6] + '@'+name[:3]

    if name=='' or gender=='' or Id=='' or mobile==0 :
        tmsg.showinfo('No','Please fill Important details')
    elif len(str(mobile)) != 10:
        tmsg.showinfo('No','Filled Mobile is not of 10 digit')
    elif gender not in Gender:
        tmsg.showinfo('No','Please select gender from list')
    else:        
        try:
            cur.execute('INSERT INTO Coach_login VALUES(?,?,?,?,?,?)',(Id,name,mobile,email,gender,password,))
            connector.commit()
            Admin_Add_Coach()
        except Exception as e:
            tmsg.showinfo('Error',f'There is some issue in entering Data!\n {e}')
        else:
            tmsg.showinfo('Done','Successfully Done!')


def Admin_Add_Coach():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(420,320)
    root.geometry(f'420x320+{w}+{h}')
    root.minsize(420,320)
    root.maxsize(420,320)
    root.title('Add Coach Details')
    Go_backandmain(Admin_function)

    Label(root,text='ID*:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=1)
    Label(root,text='Name*:',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=1)
    Label(root,text='Mobile*:',font='lucida 20 bold',padx=5,pady=5).grid(row=2,column=1)
    Label(root,text='Email:',font='lucida 20 bold',padx=5,pady=5).grid(row=3,column=1)
    Label(root,text='Gender*:',font='lucida 20 bold',padx=5,pady=5).grid(row=4,column=1)

    global ID_c,Name_c,mobile_c,email_c,gender_c

    ID_c = StringVar(root)
    Name_c = StringVar(root)
    mobile_c = IntVar(root)
    email_c = StringVar(root)
    gender_c = StringVar(root)

    IdEntry = Entry(root,textvariable=ID_c,font='lucida 16 ')
    IdEntry.grid(row=0,column=2)
    NameEntry = Entry(root,textvariable=Name_c,font='lucida 16 ')
    NameEntry.grid(row=1,column=2)
    MobileEntry = Entry(root,textvariable=mobile_c,font='lucida 16')
    MobileEntry.grid(row=2,column=2)
    emailEntry = Entry(root,textvariable=email_c,font='lucida 16')
    emailEntry.grid(row=3,column=2)
    genderEntry = ttk.Combobox(root,textvariable=gender_c,font='lucida 14')
    genderEntry['values'] = Gender
    genderEntry.grid(row=4,column=2)
    genderEntry.current(0)

    Button(root,text='Close',bg='red',fg='white',command=quit,width=6,font='lucide 20 bold',relief=GROOVE,border=10).grid(row=5,column=1)
    Button(root,text='Create',bg='blue',fg='white',command=Admin_Submit_Coach,width=10,font='lucide 20 bold',relief=GROOVE,border=10).grid(row=5,column=2)


def Admin_Student_Search():
    cur.execute('SELECT * from Student_details where Roll_no=(?)',(roll_no_s.get(),))
    Data = cur.fetchone()
    if Data == None:
        tmsg.showinfo('Not Found','Student is not in your database!')
    else:
        Admin_Look_Student()
        tmsg.showinfo('Student Details',f'Name:{Data[0]} \nBranch:{Data[1]} \nSem:{Data[2]} \nRoll_no:{Data[3]} \nPhone_number:{Data[4]}')

def Admin_Look_Student():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(500,180)
    root.geometry(f'500x180+{w}+{h}')
    root.minsize(500,180)
    root.maxsize(500,180)

    root.title('Search')
    Go_backandmain(Admin_function)

    Label(root,text='Student Roll_no:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=1)

    global roll_no_s

    roll_no_s = StringVar(root)

    roll_noEntry = Entry(root,textvariable=roll_no_s,font='lucida 16')
    roll_noEntry.grid(row=0,column=2)

    Button(root,text='Close',bg='red',fg='white',command=quit,width=7,font='lucide 18 bold',relief=GROOVE,border=10).grid(row=1,column=1)
    Button(root,text='Search',bg='blue',fg='white',command=Admin_Student_Search,width=7,font='lucide 18 bold',relief=GROOVE,border=10).grid(row=1,column=2)

def Admin_Call_Delete():
    roll = roll_no_d.get()
    cur.execute('SELECT * From Student_details where Roll_no=(?)',(roll,))
    data = cur.fetchall()
    if data != []:
        cur.execute('DELETE from Student_details where Roll_no=(?)',(roll,))
        connector.commit()
        cur.execute('DELETE from Student_login where Roll_no=(?)',(roll,))
        connector.commit()
        Admin_Delete_Student()
        tmsg.showinfo('Done',"Successfully Deleted Student from Database\nIt's Login is also Deleted")
    else:
        tmsg.showinfo('NOT FOUND','Student is not in your Database')

def Admin_Delete_Student():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(500,180)
    root.geometry(f'500x180+{w}+{h}')
    root.minsize(500,180)
    root.maxsize(500,180)

    root.title('Delete')

    Label(root,text='Student Roll_no:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=1)

    Go_backandmain(Admin_function)

    global roll_no_d

    roll_no_d = StringVar(root)

    roll_noEntry = Entry(root,textvariable=roll_no_d,font='lucida 16')
    roll_noEntry.grid(row=0,column=2)

    Button(root,text='Close',bg='red',fg='white',command=quit,width=7,font='lucide 18 bold',relief=GROOVE,border=10).grid(row=1,column=1)
    Button(root,text='Delete',bg='blue',fg='white',command=Admin_Call_Delete,width=7,font='lucide 18 bold',relief=GROOVE,border=10).grid(row=1,column=2)

def Admin_Student_Change_Name_call():
    name =name_1161.get()
    roll_no = roll_no_1161.get()
    name_again = name_again_1161.get()
    cur.execute('SELECT * From Student_details where Roll_no = (?)',(roll_no,))
    data = cur.fetchall()
    if data != []:
        if name == name_again:
            try:
                cur.execute('UPDATE Student_details set Name=(?) where Roll_no=(?)',(name,roll_no,))
                connector.commit()
                Admin_Student_Change_Name()
            except Exception as e:
                tmsg.showinfo('Error',f'There is some error given below\n{e}')
            else:
                tmsg.showinfo('Updated','Updated Name Successfully!')
        else:
            tmsg.showinfo('Not Matched',"Entered Names Don't Match!")
    else:
        tmsg.showinfo('Not found','Student Roll no Not Found')

def Admin_Student_Change_Name():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(520,220)
    root.geometry(f'520x220+{w}+{h}')
    root.minsize(520,220)
    root.maxsize(520,220)

    root.title("Update Student's Name")
    Label(root,text='Enter Roll Number:',font='lucida 20 bold',padx=2,pady=2).grid(row=0,column=0)
    Label(root,text='Enter Name:',font='lucida 20 bold',padx=2,pady=2).grid(row=1,column=0)
    Label(root,text='Enter Name Again:',font='lucida 20 bold',padx=2,pady=2).grid(row=2,column=0)

    Go_backandmain(Admin_Student_Change)
    global roll_no_1161,name_1161,name_again_1161

    roll_no_1161 = IntVar(root)
    name_1161 = StringVar(root)
    name_again_1161 = StringVar(root)

    roll_noEntry = Entry(root,textvariable=roll_no_1161,font='lucida 16')
    roll_noEntry.grid(row=0,column=1)
    nameEntry = Entry(root,textvariable=name_1161,font='lucida 16')
    nameEntry.grid(row=1,column=1)
    name_againEntry = Entry(root,textvariable=name_again_1161,font='lucida 16')
    name_againEntry.grid(row=2,column=1)

    Button(root,text='Update',bg='blue',fg='white',font='lucida 18 bold',command=Admin_Student_Change_Name_call,width=10,relief=GROOVE,border=10).grid(row=3,column=1)
    Button(root,text='Close',bg='red',fg='white',font='lucida 18 bold',command=quit,width=10,relief=GROOVE,border=10).grid(row=3,column=0)

def Admin_Student_Change_Branch_call():
    roll_no = roll_no_1162.get()
    branch = branch_1162.get()
    branch_again = branch_again_1162.get()

    cur.execute('SELECT * From Student_details where Roll_no = (?)',(roll_no,))
    data = cur.fetchall()
    if data != []:
        if branch == branch_again :
            try:
                cur.execute('UPDATE Student_details set Branch=(?) where Roll_no=(?)',(branch,roll_no,))
                connector.commit()
                Admin_Student_Change_Branch()
            except Exception as e:
                tmsg.showinfo('Issue',f'Was not updated due to reason givemn below\n{e}')
            else:
                tmsg.showinfo('Updated','Successfully Updated')
        else:
            tmsg.showinfo('Match','Entered Branch do not match!')
    else:
        tmsg.showinfo('Not found','Student Roll no Not Found')

def Admin_Student_Change_Branch():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,200)
    root.geometry(f'450x200+{w}+{h}')
    root.minsize(450,200)
    root.maxsize(450,200)

    root.title("Change Student's Branch")

    Label(root,text='Roll Number:',font='lucida 20 bold',padx=2,pady=2).grid(row=0,column=0)
    Label(root,text='Branch Name:',font='lucida 20 bold',padx=2,pady=2).grid(row=1,column=0)
    Label(root,text='Branch Again:',font='lucida 20 bold',padx=2,pady=2).grid(row=2,column=0)

    Go_backandmain(Admin_Student_Change)

    global roll_no_1162,branch_1162,branch_again_1162

    roll_no_1162 = IntVar(root)
    branch_1162 = StringVar(root)
    branch_again_1162 = StringVar(root)

    roll_noEntry = Entry(root,textvariable=roll_no_1162,font='lucida 16')
    roll_noEntry.grid(row=0,column=1)
    branchEntry = ttk.Combobox(root,textvariable=branch_1162,font='lucida 14')
    branchEntry['values'] = Cllg_branches 
    branchEntry.grid(row=1,column=1)
    branchEntry.current()
    branch_againEntry = ttk.Combobox(root,textvariable=branch_again_1162,font='lucida 14')
    branch_againEntry['values'] = Cllg_branches
    branch_againEntry.grid(row=2,column=1) 
    branch_againEntry.current()

    Button(root,text='Close',bg='red',fg='white',font='lucida 18 bold',relief=GROOVE,border=10,command=quit).grid(row=3,column=0)
    Button(root,text='Update',bg='blue',fg='white',font='lucida 18 bold',relief=GROOVE,border=10,command=Admin_Student_Change_Branch_call,width=10).grid(row=3,column=1)

def Admin_Student_Change_Sem_Call():
    roll_no = roll_no_1163.get()
    sem = sem_1163.get()
    sem_again = sem_again_1163.get()

    cur.execute('SELECT * From Student_details where Roll_no = (?)',(roll_no,))
    data = cur.fetchall()
    if data != []:
        if sem == sem_again and (sem > 0 and sem <=8):
            try:
                cur.execute("UPDATE Student_details set Sem=(?) where Roll_no=(?)",(sem,roll_no,))
                connector.commit()
                Admin_Student_Change_Sem()
            except Exception as e:
                tmsg.showinfo('Issue',f'There is some Issue as given\n {e}')
            else:
                tmsg.showinfo('Updated','Successfully Updated Semester!')
        else:
            tmsg.showinfo('Match?','Entered Semester values do not match!\n or you have entered sem greater than 8 or less than 0')
    else:
        tmsg.showinfo('Not found','Student Roll no Not Found')

def Admin_Student_Change_Sem():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(500,200)
    root.geometry(f'500x200+{w}+{h}')
    root.minsize(500,200)
    root.maxsize(500,200)

    root.title("Update Student's Semester")

    Label(root,text='Roll Number:',font='lucida 20 bold',padx=2,pady=2).grid(row=0,column=1)
    Label(root,text='Semester:',font='lucida 20 bold',padx=2,pady=2).grid(row=1,column=1)
    Label(root,text='Semester(again):',font='lucida 20 bold',padx=2,pady=2).grid(row=2,column=1)

    Go_backandmain(Admin_Student_Change)
    
    global roll_no_1163,sem_1163,sem_again_1163

    roll_no_1163 = IntVar(root)
    sem_1163 = IntVar(root)
    sem_again_1163 = IntVar(root)

    roll_noEntry = Entry(root,textvariable=roll_no_1163,font='lucida 16',)
    roll_noEntry.grid(row=0,column=2)
    semEntry = Entry(root,textvariable=sem_1163,font='lucida 16',)
    semEntry.grid(row=1,column=2)
    sem_againEntry = Entry(root,textvariable=sem_again_1163,font='lucida 16',)
    sem_againEntry.grid(row=2,column=2)

    Button(root,text='Close',bg='red',fg='white',font='lucida 18 bold',command=quit,relief=GROOVE,border=10).grid(row=3,column=1)
    Button(root,text='Update',bg='blue',fg='white',font='lucida 18 bold',command=Admin_Student_Change_Sem_Call,relief=GROOVE,border=10,width=10).grid(row=3,column=2)

def Admin_Student_Change_Phone_Call():
    
    roll_no = roll_no_1164.get()
    phone = phone_1164.get()
    phone_again = phone_again_1164.get()

    cur.execute('SELECT * From Student_details where Roll_no = (?)',(roll_no,))
    data = cur.fetchall()
    if data != []:
        if phone == phone_again and len(str(phone)) ==10:
            try:
                cur.execute('UPDATE Student_details set Phone_number=(?) where Roll_no=(?)',(phone,roll_no,))
                connector.commit()
                Admin_Student_Change_Phone()
            except Exception as e:
                tmsg.showinfo('Issue',f'There is some issue while updating\n{e}')
            else:
                tmsg.showinfo('Updated','Successfully Updated Phone number!')
        else:
            tmsg.showinfo('Match?','Entered values do not match,Check again!\n or you have not entered 10 digit mobile number')
    else:
        tmsg.showinfo('Not found','Student Roll no Not Found')

def Admin_Student_Change_Phone():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,200)
    root.geometry(f'450x200+{w}+{h}')
    root.title("Update Student's Phone Number")

    Label(root,text='Roll Number:',font='lucida 20 bold',padx=2,pady=2).grid(row=0,column=1)
    Label(root,text='Mobile:',font='lucida 20 bold',padx=2,pady=2).grid(row=1,column=1)
    Label(root,text='Mobile(again):',font='lucida 20 bold',padx=2,pady=2).grid(row=2,column=1)

    Go_backandmain(Admin_Student_Change)

    global roll_no_1164,phone_1164,phone_again_1164

    roll_no_1164 = IntVar(root)
    phone_1164 = IntVar(root)
    phone_again_1164 = IntVar(root)

    roll_noEntry = Entry(root,textvariable=roll_no_1164,font='lucida 16')
    roll_noEntry.grid(row=0,column=2)
    phoneEntry = Entry(root,textvariable=phone_1164,font='lucida 16')
    phoneEntry.grid(row=1,column=2)
    phone_againEntry  = Entry(root,textvariable=phone_again_1164,font='lucida 16')
    phone_againEntry.grid(row=2,column=2)

    Button(root,text='Close',bg='red',fg='white',font='lucida 18 bold',command=quit,relief=GROOVE,border=10).grid(row=3,column=1)
    Button(root,text='Update',bg='blue',fg='white',font='lucida 18 bold',command=Admin_Student_Change_Phone_Call,relief=GROOVE,border=10,width=10).grid(row=3,column=2)



def Admin_Student_Change():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(400,480)
    root.geometry(f'400x480+{w}+{h}')
    root.minsize(400,480)
    root.maxsize(400,480)
    root.title('Change Student Details')

    f_1161 = Frame(root,bg='grey')
    Label(f_1161,text='Change Options',font='lucida 30 bold',justify='center',bg='grey').pack()
    f_1161.pack(fill=X)

    Go_backandmain(Admin_function)
 
    f_1162 = Frame(root)
    Button(f_1162,text='Name',font='lucida 20 bold',command=Admin_Student_Change_Name,width=18,relief=GROOVE,border=10).pack(pady=2)
    Button(f_1162,text='Branch',font='lucida 20 bold',command=Admin_Student_Change_Branch,width=18,relief=GROOVE,border=10).pack(pady=2)
    Button(f_1162,text='Semester',font='lucida 20 bold',command=Admin_Student_Change_Sem,width=18,relief=GROOVE,border=10).pack(pady=2)
    Button(f_1162,text='Phone Number',font='lucida 20 bold',command=Admin_Student_Change_Phone,width=18,relief=GROOVE,border=10).pack(pady=2)
    Button(f_1162,text='Close',bg='red',fg='white',font='lucida 20 bold',command=quit,width=10,relief=GROOVE,border=10).pack(pady=1)
    f_1162.pack(fill=BOTH,padx=10,pady=20)

def Admin_Searching(ID,Password):
    id=0
    pas=0
    querry = "SELECT * from Admin_login where ID='{}' and Password='{}'".format(ID, Password)
    cur.execute(querry);
    data_se = cur.fetchall()
    # print(data_se)
    for i in range(len(data_se)):
        if ID == data_se[i][0]:
            id=1
        if Password == data_se[i][1]:
            pas=1
    # if data_se:
    #     id=1
    #     pas=1
    return id,pas

def Admin_function():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(600,600)
    root.geometry(f'600x600+{w}+{h}')
    root.minsize(600,600)
    root.maxsize(600,600)
    root.title('Admin Block')
    f_11 = Frame(root,bg='grey')
    Label(f_11,text='Welcome To Admin Block!',font='lucida 30 bold',bg='grey',justify='center').pack()
    f_11.pack(fill=X)

    Go_backandmain(Admin_Login_Data)

    f_12 = Frame(root)
    Button(f_12,text='Add Student',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Add_student,width=20).pack()
    Button(f_12,text='Add Warden',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Add_Warden,width=20).pack()
    Button(f_12,text='Add Coach',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Add_Coach,width=20).pack()
    Button(f_12,text='Look for Student',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Look_Student,width=20).pack()
    Button(f_12,text='Delete Student',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Delete_Student,width=20).pack()
    Button(f_12,text='Update Student Detail',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Student_Change,width=20).pack()
    Button(f_12,text='Close',bg='red',fg='white',font='lucida 20 bold',relief=GROOVE,border=10,command=quit,width=10).pack()

    f_12.pack(fill=BOTH,pady=30)

def Admin_look_up():
    x_1 = Admin_Searching(IDValue_1.get(),PasswordValue_1.get())
    if x_1[0] == 0 and x_1[1] == 0:
        tmsg.showinfo('Ops!','Your Id and Password are wrong')
    elif x_1[0] == 1 and x_1[1] == 1:
        Admin_function()
    elif x_1[0] == 1 and x_1[1] == 0:
        tmsg.showinfo('Error','Your Password is Incorrect! check it again!')    

def Admin_Login_Data():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(420,180)
    root.geometry(f'420x180+{w}+{h}')
    root.minsize(420,180)
    root.maxsize(420,180)
    root.title('Admin Login')
    Go_back(Main_Menu)

    ID_1 = Label(root,text="ID:",font='lucida 20 bold',padx=5,pady=5)
    ID_1.grid(column=2)
    Password_1 = Label(root,text="Password:",font='lucida 20 bold',padx=5,pady=5)
    Password_1.grid(row=1,column=2)
    global IDValue_1,PasswordValue_1
    IDValue_1 = StringVar(root)
    PasswordValue_1 = StringVar(root)

    IDEntry_1 = Entry(root,textvariable=IDValue_1,font='lucida 16 ').grid(row=0,column=3)
    PasswordEntry_1 = Entry(root,textvariable=PasswordValue_1,font='lucida 16 ', show='*').grid(row=1,column=3)
    Button(root,text='Close',bg='red',fg='white',command=quit,font='lucida 18 bold',height=1,width=8,relief=GROOVE,border=10).grid(row=2,column=2)
    Button(root,text='Login',bg='blue',fg='white',command=Admin_look_up,font='lucida 18 bold',height=1,width=10,relief=GROOVE,border=10).grid(row=2,column=3)


### Admin block ends     

### Warden block starts

def Warden_Add_Student_Call():
    roll_no = roll_no_211.get()
    fee = fee_no_211.get()
    if roll_no == 0 and fee =='':
        tmsg.showinfo('NO','Please Both details')
    else:
        cur.execute("SELECT * from Hostel_rooms_status")
        data = cur.fetchall()
        Room_no=-1
        for i in range(1,len(data)+1):
            if data[i][1] != 0:
                Room_no=i
                No_of_spaces=data[i][1]
                break

        cur.execute('SELECT Name,Branch,Sem FROM Student_details where Roll_no=(?)',(roll_no,))
        Data = cur.fetchone()
        if Data != None:
            try:
                cur.execute('INSERT INTO Hostel values (?,?,?,?,?,?)',(roll_no,Data[0],Data[1],Data[2],fee,Room_no,))
                connector.commit()
                if Room_no!=-1:
                        cur.execute("UPDATE Hostel_rooms_status set No_of_spaces=(?) where Room_no=(?)",((No_of_spaces-1),Room_no,))
                        connector.commit()
                Warden_Add_Student()
            except Exception as e:
                tmsg.showinfo('Issue',f'There is some as given below\n {e}')
            else:
                if Room_no == -1:
                    tmsg.showinfo('Done','Waiting room is alloted!')
                else:
                    tmsg.showinfo('Done',f' {Room_no} number room is alloted')
        else:
            tmsg.showinfo('NOT FOUND','No such student with roll_no you have entered')

        


def Warden_Add_Student():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(520,180)
    root.geometry(f'520x180+{w}+{h}')
    root.minsize(520,180)
    root.maxsize(520,180)

    root.title('Fill Student Detail')

    Label(root,text="Student's Roll no* :",font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)
    Label(root,text='Fee(Paid/Not Paid)*:',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=0)

    Go_backandmain(Warden_function)

    global roll_no_211,fee_no_211

    roll_no_211 = IntVar(root)
    fee_no_211 = StringVar(root)

    roll_no = Entry(root,textvariable=roll_no_211,font='lucida 16')
    roll_no.grid(row=0,column=1)
    fee = ttk.Combobox(root,textvariable=fee_no_211,font='lucida 14')
    fee['values'] = Fee
    fee.grid(row=1,column=1)
    fee.current(1)

    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=2,column=0)
    Button(root,text='Add',bg='blue',fg='white',command=Warden_Add_Student_Call,relief=GROOVE,border=10,font='lucida 18 bold',width=10).grid(row=2,column=1)

def Warden_Delete_Student_Call():
    roll_no = roll_no_212.get()
    cur.execute('SELECT * from Hostel where Roll_no=(?)',(roll_no,))
    data = cur.fetchall()
    if data != []:
        cur.execute('DELETE From Hostel where Roll_no=(?)',(roll_no,))
        connector.commit()
        Warden_Delete_Student()
        tmsg.showinfo('Done','Student is removed from Hostel!')
    else:
        tmsg.showinfo('NOT Found','There is no such student in your hostel')

def Warden_Delete_Student():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,130)
    root.geometry(f'450x130+{w}+{h}')
    root.minsize(450,130)
    root.maxsize(450,130)

    root.title('Delete Student')

    Label(root,text='Roll Number:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)

    Go_backandmain(Warden_function)

    global roll_no_212

    roll_no_212 = IntVar(root)

    roll_no = Entry(root,textvariable=roll_no_212,font='lucida 16')
    roll_no.grid(row=0,column=1)

    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=1,column=0)
    Button(root,text='Delete',bg='blue',fg='white',command=Warden_Delete_Student_Call,relief=GROOVE,border=10,font='lucida 18 bold',width=10).grid(row=1,column=1)

def Warden_Delete_Room_Call():
    room_no = room_no_213.get() 
    cur.execute('SELECT * From Hostel_rooms_status where Room_no=(?)',(room_no,))
    data = cur.fetchall()
    if data != []:    
        cur.execute('DELETE From Hostel_rooms_status where Room_no=(?)',(room_no,))
        connector.commit()
        Warden_Delete_Room()
        tmsg.showinfo('Deleted',f'Room {room_no} is deleted from database!')
    else:
        tmsg.showinfo('Not Found','NO such Room in your Database')

def Warden_Delete_Room():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(490,130)
    root.geometry(f'490x130+{w}+{h}')
    root.minsize(490,130)
    root.maxsize(490,130)
    root.title('Delete Room')

    Label(root,text='Enter Room No.:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)

    Go_backandmain(Warden_function)

    global room_no_213

    room_no_213 = IntVar(root)

    room_no = Entry(root,textvariable=room_no_213,font='lucida 16')
    room_no.grid(row=0,column=1)

    Button(root,text='Close',bg='red',fg='white',command=quit,font='lucida 18 bold',relief=GROOVE,border=10,width=8).grid(row=1,column=0)
    Button(root,text='Delete',bg='blue',fg='white',command=Warden_Delete_Room_Call,font='lucida 18 bold',relief=GROOVE,border=10,width=10).grid(row=1,column=1)

def Warden_Add_Rooms_Call():
    try:
        for i in range(s_room_no_214.get(),e_room_no_214.get()+1):
            cur.execute("INSERT INTO Hostel_rooms_status(Room_no,No_of_spaces) VALUES(?,3)",(i,))
            connector.commit()
            Warden_Add_Rooms()
    except Exception as e:
        tmsg.showinfo('Issue',f'There is some issue as given below\n{e}')
    else:
        tmsg.showinfo('Done','Successfully Entered rooms in database')

def Warden_Add_Rooms():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(500,170)
    root.geometry(f'500x170+{w}+{h}')
    root.minsize(500,170)
    root.maxsize(500,170)
    root.title('Add Rooms')

    Label(root,text='Start Room No.:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)
    Label(root,text='End Room No.:',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=0)

    Go_backandmain(Warden_function)

    global s_room_no_214,e_room_no_214

    s_room_no_214 = IntVar(root)
    e_room_no_214 = IntVar(root)

    Start = Entry(root,textvariable=s_room_no_214,font='lucida 16')
    Start.grid(row=0,column=1)
    End = Entry(root,textvariable=e_room_no_214,font='lucida 16')
    End.grid(row=1,column=1)

    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=2,column=0)
    Button(root,text='Add',bg='blue',fg='white',command=Warden_Add_Rooms_Call,relief=GROOVE,border=10,width=10,font='lucida 18 bold').grid(row=2,column=1)



def Warden_Student_Requests():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(1220,600)
    root.geometry(f'1220x600+{w}+{h}')
    root.minsize(1220,600)
    root.maxsize(1220,600)

    Go_backandmain(Warden_function)

    root.title('Hostel Requests')

    cur.execute('SELECT * FROM Hostel_request')
    Data = cur.fetchall()
    if Data != []:
        Data.insert(0,['Roll No','Name','Branch','Semester'])
        Trow = len(Data)
        Tcolumn = len(Data[0])
        for i in range(Trow):
            for j in range(Tcolumn):
                e = Entry(root,width=20,font='lucida 20 bold')
                e.grid(row=i,column=j)
                e.insert(END,Data[i][j])

    else:
        tmsg.showinfo('Empty','There is no request!')


    

def Warden_Searching(ID,Password):
    id=0
    pas=0
    cur.execute("SELECT ID,Password from Warden_login ")
    data_se = cur.fetchall()
    for i in range(len(data_se)):
        if ID == data_se[i][0]:
            id=1
        if Password == data_se[i][1]:
            pas=1
    return id,pas

def Warden_function():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(600,670)
    root.geometry(f'600x670+{w}+{h}')
    root.minsize(600,670)
    root.maxsize(600,670)

    root.title('Warden Functions')
    Go_backandmain(Warden_Login_Data)


    f_21 = Frame(root,bg='grey')
    Label(f_21,text='Welcome To Warden Login!',font='lucida 30 bold',bg='grey',justify='center').pack()
    f_21.pack(fill=X)
    textlist = ['Add Student','Remove Student','Delete room','Add Rooms','Display all request']
    commandlist = [Warden_Add_Student,Warden_Delete_Student,Warden_Delete_Room,Warden_Add_Rooms,Warden_Student_Requests]

    f_22 = Frame(root)
    for i in range(len(textlist)):
        Button(f_22,text=textlist[i],command=commandlist[i],font='lucida 25 bold',relief=GROOVE,border=10,width=20,height=1).pack()
    Button(f_22,text='Close',bg='red',fg='white',command=quit,font='lucida 20 bold',relief=GROOVE,border=10,width=18).pack()
    f_22.pack(fill=BOTH,pady=20)

def Warden_Look_Up():
    x_2= Warden_Searching(IDValue_2.get(),PasswordValue_2.get())
    if x_2[0] == 0 and x_2[1] == 0:
        tmsg.showinfo('Ops!','Your Id and Password are wrong')
    elif x_2[0] == 1 and x_2[1] == 1:
        Warden_function()
    elif x_2[0] == 1 and x_2[1] == 0:
        tmsg.showinfo('Error','Your Password is Incorrect! check it again!')   

def Warden_Login_Data():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(420,180)
    root.geometry(f'420x180+{w}+{h}')
    root.minsize(420,180)
    root.maxsize(420,180)
    root.title('Warden Login')
    Go_back(Main_Menu)

    ID_2 = Label(root,text="ID:",font='lucida 20 bold',padx=5,pady=5).grid(column=2)
    Password_2 = Label(root,text="Password:",font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=2)
    global IDValue_2,PasswordValue_2
    IDValue_2 = StringVar(root)
    PasswordValue_2 = StringVar(root)

    IDEntry_2 = Entry(root,textvariable=IDValue_2,font='lucida 16 ').grid(row=0,column=3)
    PasswordEntry_2 = Entry(root,textvariable=PasswordValue_2,font='lucida 16 ', show='*').grid(row=1,column=3)
    Button(root,text='Close',bg='red',fg='white',command=quit,font='lucida 18 bold',height=1,width=8,relief=GROOVE,border=10).grid(row=2,column=2)
    Button(root,text='Login',bg='blue',fg='white',command=Warden_Look_Up,font='lucida 18 bold',height=1,width=10,relief=GROOVE,border=10).grid(row=2,column=3)


### Warden block Ends

### Coach block Starts

def Coach_Add_Student_Call():
    roll_no = roll_no_311.get()
    sports = sports_311.get()
    cur.execute('SELECT Name,Branch,Sem FROM Student_details where Roll_no=(?)',(roll_no,))
    Data = cur.fetchone()
    if roll_no==0 or sports =='':
        tmsg.showinfo('No','Please fill all details')
    elif Data == None:
        tmsg.showinfo('Not Found','Student is not in your college database')
    elif sports not in SPORTS:
        tmsg.showinfo('No','Please select sports name from list')
    else:
        try:
            cur.execute('INSERT INTO Sports values (?,?,?,?,?)',(roll_no,Data[0],Data[1],Data[2],sports,))
            connector.commit()
            Coach_Add_Student()
        except Exception as e:
            tmsg.showinfo('Issue',f'There is some issue given below\n{e}')
        else:
            tmsg.showinfo('Added',f'Student is added to {sports}')

def Coach_Add_Student():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(510,180)
    root.geometry(f'510x180+{w}+{h}')
    root.minsize(510,180)
    root.maxsize(510,180)

    Go_backandmain(Coach_Functions)
    root.title('Fill Student Details')

    Label(root,text='Student Roll_no:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)
    Label(root,text='Enrollment(sport):',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=0)

    global roll_no_311,sports_311

    roll_no_311 = IntVar(root)
    sports_311 = StringVar(root)

    roll_no = Entry(root,textvariable=roll_no_311,font='lucida 16')
    roll_no.grid(row=0,column=1)
    sports = ttk.Combobox(root,textvariable=sports_311,font='lucida 14')
    sports['values'] = SPORTS
    sports.grid(row=1,column=1)
    sports.current(0)

    Button(root,text='Close',bg='red',fg='white',font='lucida 18 bold',command=quit,width=8,relief=GROOVE,border=10).grid(row=2,column=0)
    Button(root,text='Add',bg='blue',fg='white',font='lucida 18 bold',command=Coach_Add_Student_Call,width=10,relief=GROOVE,border=10).grid(row=2,column=1)

def Coach_Delete_Student_Call():
    roll_no = roll_no_312.get()
    cur.execute('SELECT * From Sports where Roll_no=(?)',(roll_no,))
    data = cur.fetchall()
    if data != []:
        cur.execute('DELETE FROM Sports where Roll_no=(?)',(roll_no,))
        Coach_Delete_Student()
        tmsg.showinfo('Deleted',f'Successfully Deleted Student {roll_no}')
    else:
        tmsg.showinfo('Not found','No such student in your Sports database')

def Coach_Delete_Student():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,140)
    root.geometry(f'450x140+{w}+{h}')
    root.minsize(450,140)
    root.maxsize(450,140)

    root.title('Delete Student')

    Label(root,text='Roll Number:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)

    Go_backandmain(Coach_Functions)

    global roll_no_312

    roll_no_312 = IntVar(root)

    roll_no = Entry(root,textvariable=roll_no_312,font='lucida 16')
    roll_no.grid(row=0,column=1)

    Button(root,text='Close',bg='red',fg='white',font='lucida 18 bold',command=quit,width=8,relief=GROOVE,border=10).grid(row=1,column=0)
    Button(root,text='Delete',bg='blue',fg='white',font='lucida 18 bold',command=Coach_Delete_Student_Call,width=10,relief=GROOVE,border=10).grid(row=1,column=1)


def Coach_Update_Place_Call():
    place = s_place_313.get()
    name = s_name_313.get()
    if name not in SPORTS:
        tmsg.showinfo('NO','Please select sports name from list given')
    elif place == '':
        tmsg.showinfo('No','Please enter sports place ')
    else:        
        cur.execute('UPDATE Sports_status_and_places set Sports_places=(?) where Sports_name=(?)',(place,name,))
        Coach_Update_Place()
        tmsg.showinfo('Updated','Successfully Updated Sports Place')

def Coach_Update_Place():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,180)
    root.geometry(f'450x180+{w}+{h}')
    root.minsize(450,180)
    root.maxsize(450,180)

    root.title('Sports Place Update')

    Label(root,text='Sports Name:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)
    Label(root,text="New Place:",font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=0)

    Go_backandmain(Coach_Functions)
    global s_name_313,s_place_313

    s_name_313 = StringVar(root)
    s_place_313 = StringVar(root)

    s_name = ttk.Combobox(root,textvariable=s_name_313,font='lucida 14')
    s_name['values'] = SPORTS
    s_name.grid(row=0,column=1)
    s_name.current(0)
    s_place = Entry(root,textvariable=s_place_313,font='lucida 16')
    s_place.grid(row=1,column=1)

    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=2,column=0)
    Button(root,text='Update',bg='blue',fg='white',command=Coach_Update_Place_Call,relief=GROOVE,border=10,font='lucida 18 bold',width=10).grid(row=2,column=1)

def Coach_Update_Status_Call():
    status = s_status_314.get()
    name = s_name_314.get()

    if status not in STATUS or name not in SPORTS:
        tmsg.showinfo('NO','Please select from list')
    else:
        cur.execute('UPDATE Sports_status_and_places set Sports_status=(?) where Sports_name=(?)',(s_status_314.get(),s_name_314.get(),))
        Coach_Update_Status()
        tmsg.showinfo('Updated','Successfully Updated Sports Status')

def Coach_Update_Status():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(480,180)
    root.geometry(f'480x180+{w}+{h}')
    root.title('Update Sports Status')

    Label(root,text='Sports Name:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)
    Label(root,text='Free/Occupied:',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=0)

    Go_backandmain(Coach_Functions)

    global s_status_314,s_name_314

    s_status_314 = StringVar(root)
    s_name_314 = StringVar(root)

    status = ttk.Combobox(root,textvariable=s_status_314,font='lucida 14')
    status['values'] = STATUS
    status.grid(row=0,column=1)
    status.current(0)
    s_name = ttk.Combobox(root,textvariable=s_name_314,font='lucida 14')
    s_name['values'] = SPORTS
    s_name.grid(row=1,column=1)
    s_name.current(0)

    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=2,column=0)
    Button(root,text='Update',bg='blue',fg='white',command=Coach_Update_Status_Call,relief=GROOVE,border=10,font='lucida 18 bold',width=10).grid(row=2,column=1)


def Coach_Functions():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(500,500)
    root.geometry(f'500x500+{w}+{h}')
    root.minsize(500,500)
    root.maxsize(500,500)
    root.title('Coach Functions')
    Go_backandmain(Coach_Login_Data)

    f_31 = Frame(root,bg='grey')
    Label(f_31,text='Welcome to Coach login!',bg='grey',font='lucida 30 bold',justify='center').pack()
    f_31.pack(fill=X,pady=2)

    textlist = ['Add Student','Remove Student','Update Place','Update Status']
    commandlist = [Coach_Add_Student,Coach_Delete_Student,Coach_Update_Place,Coach_Update_Status]

    f_32 = Frame(root)
    for i in range(len(textlist)):
        Button(f_32,text=textlist[i],command=commandlist[i],font='lucida 25 bold',relief=GROOVE,border=10,width=20,height=1).pack()
    Button(f_32,text='Close',bg='red',fg='white',command=quit,font='lucida 20 bold',relief=GROOVE,border=10,width=18).pack()
    f_32.pack(fill=BOTH,pady=20)



def Coach_Searching(ID,Password):
    id=0
    pas=0
    cur.execute("SELECT ID,Password from Coach_login ");
    data_se = cur.fetchall()
    for i in range(len(data_se)):
        if ID == data_se[i][0]:
            id=1
        if Password == data_se[i][1]:
            pas=1
    return id,pas

def Coach_Look_Up():
    Data = Coach_Searching(IDValue_3.get(),PasswordValue_3.get())
    if Data[0] == 1 and Data[1] == 1:
        Coach_Functions()
    elif Data[0] == 1 and Data[1] == 0:
        tmsg.showinfo('Wrong','Your Password is Incorrect!')
    elif Data[0] == 0:
        tmsg.showinfo('Not found','You are not allowed to use coach login!')


def Coach_Login_Data():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(420,180)
    root.geometry(f'420x180+{w}+{h}')
    root.minsize(420,180)
    root.maxsize(420,180)
    root.title('Coach Login')
    Go_back(Main_Menu)

    ID_3 = Label(root,text="ID:",font='lucida 20 bold',padx=5,pady=5).grid(column=2)
    Password_3 = Label(root,text="Password:",font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=2)
    global IDValue_3,PasswordValue_3
    IDValue_3 = StringVar(root)
    PasswordValue_3 = StringVar(root)

    IDEntry_3 = Entry(root,textvariable=IDValue_3,font='lucida 16 ').grid(row=0,column=3)
    PasswordEntry_3 = Entry(root,textvariable=PasswordValue_3,font='lucida 16 ', show='*').grid(row=1,column=3)
    Button(root,text='Close',bg='red',fg='white',command=quit,font='lucida 18 bold',height=1,width=8,relief=GROOVE,border=10).grid(row=2,column=2)
    Button(root,text='Login',bg='blue',fg='white',command=Coach_Look_Up,font='lucida 18 bold',height=1,width=10,relief=GROOVE,border=10).grid(row=2,column=3)



### Coach block Ends


### Student block Starts

def Student_change_Password_call():
    roll_no = roll_no_4
    old_pass = old_411.get()
    Password = Password_411.get()
    Password_again = Password_again_411.get()
    cur.execute("SELECT * from Student_login where Password=(?) and Roll_no=(?)",(old_pass,roll_no,))
    data = cur.fetchall()
    if data != []:
        if Password == Password_again:
            try:
                cur.execute("UPDATE Student_login set Password=(?) where Roll_no=(?)",(Password,roll_no,))
                connector.commit()
                Student_change_Password()
            except Exception as e:
                tmsg.showinfo('Issue',f'Unable to update password \nIssue-> {e}')
            else:
                tmsg.showinfo('Done','Successfully Updated!')
        else:
            tmsg.showinfo('Match?','Entered passwords do not match!')
    else:
        tmsg.showinfo('Incorrect','Your old password is Incorrect')

def Student_change_Password():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(510,220)
    root.geometry(f'510x220+{w}+{h}')
    root.minsize(510,220)
    root.maxsize(510,220)

    root.title('Change Password')

    Label(root,text='Old Password:',font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=0)
    Label(root,text='New Password:',font='lucida 20 bold',padx=5,pady=5).grid(row=2,column=0)
    Label(root,text='Password again:',font='lucida 20 bold',padx=5,pady=5).grid(row=3,column=0)
    
    Go_backandmain(Student_Function)

    global old_411,Password_411,Password_again_411

    old_411 = StringVar(root)
    Password_411 = StringVar(root)
    Password_again_411 = StringVar(root)
    
    old_pass = Entry(root,textvariable=old_411,font='lucida 16',show='*')
    old_pass.grid(row=1,column=1)
    Password = Entry(root,textvariable=Password_411,font='lucida 16',show='*')
    Password.grid(row=2,column=1)
    Password_again = Entry(root,textvariable=Password_again_411,font='lucida 16',show='*')
    Password_again.grid(row=3,column=1) 
    

    Button(root,text='Close',bg='red',fg='white',command=quit,font='lucida 18 bold',height=1,width=8,relief=GROOVE,border=10).grid(row=4,column=0)
    Button(root,text='Change',bg='blue',fg='white',command=Student_change_Password_call,font='lucida 18 bold',height=1,width=10,relief=GROOVE,border=10).grid(row=4,column=1)


def Student_Check_Sports_Place_Call():
    s_name = sports_412.get()

    if s_name not in SPORTS:
        tmsg.showinfo('No','Please select from list')
    else:
        cur.execute("SELECT Sports_places from Sports_status_and_places where Sports_name=(?)",(s_name,))
        Data = cur.fetchall()
        if Data == []:
            tmsg.showinfo('Not Found','Either you have entered wrong or\nSports not in your college')
        else:
            Student_Check_Sports_Place()
            tmsg.showinfo('Done',f'Sports is played at {Data[0][0]}')

def Student_Check_Sports_Place():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,130)
    root.geometry(f'450x130+{w}+{h}')
    root.minsize(450,130)
    root.maxsize(450,130)

    root.title('Sports Place')

    Label(root,text='Sports Name:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)

    Go_backandmain(Student_Function)

    global sports_412
    sports_412 = StringVar(root)

    sports = ttk.Combobox(root,textvariable=sports_412,font='lucida 14')
    sports['values'] = SPORTS
    sports.grid(row=0,column=1)
    sports.current(0)
    
    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=1,column=0)
    Button(root,text='Check',bg='blue',fg='white',command=Student_Check_Sports_Place_Call,relief=GROOVE,border=10,width=10,font='lucida 18 bold').grid(row=1,column=1)

def Student_Check_Sports_Status_Call():
    s_name = sports_413.get() 

    if s_name not in SPORTS:
        tmsg.showinfo('No','Please select from list')
    else:
        cur.execute("SELECT Sports_status from Sports_status_and_places where Sports_name=(?)",(s_name,))
        Data = cur.fetchall()
        if Data == []:
            tmsg.showinfo('Not Found','Either you have entered wrong Sports name or\nSports not in your college')
        else:
            Student_Check_Sports_Status()
            tmsg.showinfo('Done',f'Sports is {Data[0][0]}')

def Student_Check_Sports_Status():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,130)
    root.geometry(f'450x130+{w}+{h}')
    root.minsize(450,130)
    root.maxsize(450,130)

    root.title('Sports Status')

    Label(root,text='Sports Name:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)

    Go_backandmain(Student_Function)

    global sports_413
    sports_413 = StringVar(root)

    sports = ttk.Combobox(root,textvariable=sports_413,font='lucida 14')
    sports['values'] = SPORTS
    sports.grid(row=0,column=1)
    sports.current(0)
    
    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=1,column=0)
    Button(root,text='Check',bg='blue',fg='white',command=Student_Check_Sports_Status_Call,relief=GROOVE,border=10,width=10,font='lucida 18 bold').grid(row=1,column=1)

def Student_request_Sports_Call():
    s_name  = s_name_414.get()
    if s_name not in SPORTS:
        tmsg.showinfo('No','Please select sports name from list')
    else:        
        cur.execute('SELECT Name,Branch,Sem FROM Student_details where Roll_no=(?)',(roll_no_4,))
        Data = cur.fetchone()

        try:
            cur.execute('INSERT INTO Sports_request VALUES (?,?,?,?,?)',(roll_no_4,Data[0],Data[1],Data[2],s_name,))
            connector.commit()
            Student_request_Sports()
        except Exception as e:
            tmsg.showinfo('Issue',f'There is some as given below while Inserting\n{e}')
        else:
            tmsg.showinfo('Done','Request has been sent Successfully!')

def Student_request_Sports():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(450,130)
    root.geometry(f'450x130+{w}+{h}')
    root.minsize(450,130)
    root.maxsize(450,130)

    root.title('Sports Participation')

    Label(root,text='Sports Name:',font='lucida 20 bold',padx=5,pady=5).grid(row=0,column=0)

    Go_backandmain(Student_Function)

    global s_name_414

    s_name_414 = StringVar(root)

    name = ttk.Combobox(root,textvariable=s_name_414,font='lucida 14')
    name['values'] = SPORTS
    name.grid(row=0,column=1)
    name.current(0)

    Button(root,text='Close',bg='red',fg='white',command=quit,relief=GROOVE,border=10,font='lucida 18 bold',width=8).grid(row=1,column=0)
    Button(root,text='Request',bg='blue',fg='white',command=Student_request_Sports_Call,relief=GROOVE,border=10,font='lucida 18 bold',width=10).grid(row=1,column=1)


def Student_Look_Hostel():
    cur.execute("SELECT * from Hostel_rooms_status")
    Data = cur.fetchall()
    for i in range(len(Data)):
        if Data[i][1] !=0:
            tmsg.showinfo('Rooms','Yes You can sent Request for taking Hostel.\nRooms are Empty.')
            break
    else:
        tmsg.showinfo('Oops!','Sorry no room is Empty in Hostel!')

def Student_Request_Hostel():
    x = tmsg.askquestion('Request','Do you want to send request for Hostel?')
    if x == 'yes':        
        cur.execute('SELECT Name,Branch,Sem FROM Student_details where Roll_no=(?)',(roll_no_4,))
        Data = cur.fetchone()

        try:
            cur.execute('INSERT INTO Hostel_request VALUES (?,?,?,?)',(roll_no_4,Data[0],Data[1],Data[2],))
            connector.commit()
        except Exception as e:
            tmsg.showinfo('Issue',f'There is some as given below while Inserting\n{e}')
        else:
            tmsg.showinfo('Done','Request has been sent Successfully!')

def Student_Function():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(600,600)
    root.geometry(f'600x600+{w}+{h}')
    root.minsize(600,600)
    root.maxsize(600,600)

    root.title('Student Functions')
    Go_backandmain(Student_Login_Data)

    f_41 = Frame(root,bg='grey')
    Label(f_41,text='Welcome To Student Login!',font='lucida 30 bold',bg='grey',justify='center').pack()
    f_41.pack(fill=X)
    
    f_42 = Frame(root)
    Button(f_42,text='Change Password',command=Student_change_Password,font='lucida 20 bold',width=20,relief=GROOVE,border=10,height=1).pack()
    Button(f_42,text='Check Sport Place',command=Student_Check_Sports_Place,font='lucida 20 bold',width=20,relief=GROOVE,border=10,height=1).pack()
    Button(f_42,text='Check Sport Status',command=Student_Check_Sports_Status,font='lucida 20 bold',width=20,relief=GROOVE,border=10,height=1).pack()
    Button(f_42,text='Request for sports',command=Student_request_Sports,font='lucida 20 bold',width=20,relief=GROOVE,border=10,height=1).pack()
    Button(f_42,text='Look for Hostel',command=Student_Look_Hostel,font='lucida 20 bold',width=20,relief=GROOVE,border=10,height=1).pack()
    Button(f_42,text='Request for Hostel',command=Student_Request_Hostel,font='lucida 20 bold',width=20,relief=GROOVE,border=10,height=1).pack()
    Button(f_42,text='Close',bg='red',fg='white',command=quit,font='lucida 20 bold',width=18,relief=GROOVE,border=10).pack()

    f_42.pack(fill=BOTH,pady=20)

def Student_Searching(ID,Password):
    id=0
    pas=0
    cur.execute("SELECT * from Student_login ");
    data_se = cur.fetchall()
    for i in range(len(data_se)):
        if ID == data_se[i][0]:
            id=1
        if Password == data_se[i][1]:
            pas=1
    return id,pas

def Student_look_up():
    global roll_no_4
    roll_no_4 = Roll_noValue_4.get()
     
    x = Student_Searching(Roll_noValue_4.get(),PasswordValue_4.get())
    if x[0] == 1 and x[1] == 1:
        Student_Function()
    elif x[0] == 0 :
        tmsg.showinfo('Issue','1.Either you have entered wrong Roll_no or\n2.Your Roll number is not in college Database')
    elif x[0] == 1 and x[1] == 0:
        tmsg.showinfo('Wrong','Your Password is wrong Check it again!')

def Student_Login_Data():
    global root
    root.destroy()
    root = Tk()
    w,h = Make_Center(470,180)
    root.geometry(f'470x180+{w}+{h}')
    root.minsize(470,180)
    root.maxsize(470,180)
    root.title('Student Login')
    Go_back(Main_Menu)

    Label(root,text="Roll Number:",font='lucida 20 bold',padx=5,pady=5).grid(column=2)
    Label(root,text="Password:",font='lucida 20 bold',padx=5,pady=5).grid(row=1,column=2)
    global Roll_noValue_4,PasswordValue_4
    Roll_noValue_4 = IntVar(root)
    PasswordValue_4 = StringVar(root)

    Roll_noEntry = Entry(root,textvariable=Roll_noValue_4,font='lucida 16 ')
    Roll_noEntry.grid(row=0,column=3)
    PasswordEntry_4 = Entry(root,textvariable=PasswordValue_4,font='lucida 16 ', show='*')
    PasswordEntry_4.grid(row=1,column=3)
    Button(root,text='Close',bg='red',fg='white',command=quit,font='lucida 18 bold',height=1,width=8,relief=GROOVE,border=10).grid(row=2,column=2)
    Button(root,text='Login',bg='blue',fg='white',command=Student_look_up,font='lucida 18 bold',height=1,width=10,relief=GROOVE,border=10).grid(row=2,column=3)


    root.mainloop()
### Student block Ends

### Functions Ends

###
# loop_admin=0
###
def Main_Menu():
    global root,loop
    if loop != 0:
        root.destroy()
    loop=1
    root = Tk()
    w,h = Make_Center(600,590)
    root.title('Smart College')
    root.geometry(f'600x590+{w}+{h}')
    root.minsize(600,590)
    root.maxsize(600,590)

    ### Adding a menu to rate us

    MenuBar = Menu(root)
    RateMenu = Menu(MenuBar,tearoff=0)
    RateMenu.add_command(label='About',command=About)
    RateMenu.add_command(label='Rate Us',command=Rate)
    MenuBar.add_cascade(label='Rate',menu=RateMenu)
    root.config(menu = MenuBar)
    ### Adding ends

    ###Main Menu Frame 

    f = Frame(root,bg='grey',height=80,width=500,pady=5,padx=5)
    l = Label(f,text='Welcome to Smart College!',font='lucida 30 bold',bg='grey',justify='center').pack()
    f.pack(fill=BOTH)


    f1 = Frame(root,height=420,width=500,padx=5,pady=5)
    Button(f1,text='Admin Login',font='lucida 20 bold',relief=GROOVE,border=10,command=Admin_Login_Data,height=2,width=20).pack()
    Button(f1,text='Warden Login',font='lucida 20 bold',relief=GROOVE,border=10,command=Warden_Login_Data,height=2,width=20).pack()
    Button(f1,text='Coach Login',font='lucida 20 bold',relief=GROOVE,border=10,command=Coach_Login_Data,height=2,width=20).pack()
    Button(f1,text='Student Login',font='lucida 20 bold',relief=GROOVE,border=10,command=Student_Login_Data,height=2,width=20).pack()
    Button(f1,text='Exit',font='lucida 20 bold',bg='red',fg='white',relief=GROOVE,border=10,command=quit,height=1,width=10).pack()

    f1.pack(fill=BOTH) 

    ###Main Menu Frame ends




    root.mainloop()


loop = 0
Main_Menu()


connector.close()