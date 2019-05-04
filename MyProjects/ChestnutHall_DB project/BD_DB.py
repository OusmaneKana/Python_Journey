from tkinter import *
from tkinter import ttk
import pymysql, pymysql.cursors

# Create a 'window' which is just a space to work on
db = pymysql.connect("localhost","root","Lollipop6!","Chestnut_Hall" )

connection = pymysql.connect(host = 'localhost',
                             user ='root',
                             password='Lollipop6!',
                             db = 'Chestnut_Hall',
                             cursorclass=pymysql.cursors.DictCursor)


window = Tk()
#The title on the top of the  window
window.title("Chestnut Resident Hall DB")
#window size
window.geometry('1000x550')
#create tabs
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Housing Application')
tab_control.add(tab2, text='Key Assignement')
tab_control.add(tab3, text='Residence Halls Contract Agreement')
tab_control.add(tab4, text='Inventory and Cleanliness Checklist')
tab_control.add(tab5, text='Missing Student Form')
tab_control.add(tab6, text='Release of Liability')
tab_control.add(tab7, text='Release of Liability')


e1= Entry(tab1)

date_of_birth= Entry(tab1)

ssn= Entry(tab1)

phone_number = Entry(tab1)

email = Entry(tab1)

current_address = Entry(tab1)

studentId = Entry(tab1)

e1.grid(row=2, column =1)

date_of_birth.grid(row=3, column = 1)

ssn.grid(row=3, column = 3)

phone_number.grid(row = 4, column=1)

email.grid(row = 4, column=3)

current_address.grid(row  = 5, column=1)

studentId.grid(row  = 6, column=1)



# Create a label to display on the window

lbl = Label(tab1, text = "Housing Application", font = ("Arial Bold", 10))
lbl.grid(column = 0)
lbl1 = Label(tab1, text = "Individual Information : NAU")
lbl1.grid(row = 1)

#Row 2

first_name_LBL  = Label(tab1, text ="First Name: ")
first_name_LBL.grid(row=2)


last_name_LBL  = Label(tab1, text ="Last Name: ")
last_name_LBL.grid(row = 2, column=2)
last_name= Entry(tab1, width=10)
last_name.grid(row=2, column = 3)

#Row 3
date_of_birth_LBL  = Label(tab1, text ="Date of Birth: ")
date_of_birth_LBL.grid(row = 3)

ssn_LBL  = Label(tab1, text ="Social Security Number: ")
ssn_LBL.grid(row = 3, column=2)


gender_LBL  = Label(tab1, text ="Gender: ")
gender_LBL.grid(row = 3, column=4)


#Row 4
phone_number_LBL = Label(tab1, text="Phone Number: ")
phone_number_LBL.grid(row = 4)

email_LBL = Label(tab1, text="Email: ")
email_LBL.grid(row = 4, column = 2)

#Row 5
current_address_LBL = Label(tab1, text="Current Adddress")
current_address_LBL.grid(row = 5)

studentId_LBL = Label(tab1, text="Student ID")
studentId_LBL.grid(row = 6)


# Create a potential submit button



#Define a function for the click action
def Submit_Button():


    with connection.cursor() as cursor:
    
        # sql = """INSERT INTO Student(student_id,
        #      first_name, last_name, date_of_birth, R_A, room_number)
        #      VALUES (5689, 'Hamza', 'Emrah', '1999-11-23', 'Ousmane', 531)"""
        sql = """INSERT INTO Student(student_id,
              first_name, last_name, date_of_birth, R_A, room_number)
              VALUES (1020, first_name, last_name, date_of_birth, 'Ousmane', 531)"""
        cursor.execute(sql)
    
    connection.commit()
    print(first_name)
    # if first_name.get() and last_name.get() and date_of_birth.get() and ssn.get() and current_address.get() and email.get() and current_address.get()  != "":
    #     print("Ok voila bon")
    # else:
    #     print("Missing input")


Submit_btn = Button(tab1, text="Submit",fg="white", bg="red", command=Submit_Button)
Submit_btn.grid(row=7, column=1)

tab_control.pack(expand=1, fill='both')
window.mainloop()


e1= Entry(tab1, width=10)
first_name = e1.get()

date_of_birth= Entry(tab1, width=10)

ssn= Entry(tab1, width=10)

phone_number = Entry(tab1, width = 10)

email = Entry(tab1, width = 10)

current_address = Entry(tab1, width = 15)

studentId = Entry(tab1, width = 15)
