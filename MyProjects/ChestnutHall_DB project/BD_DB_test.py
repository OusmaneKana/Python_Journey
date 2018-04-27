from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

import pymysql, pymysql.cursors

# Create a 'window' which is just a space to work on
# db = pymysql.connect("localhost","root","123456789","Chestnut_DB" )

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
tab_control.add(tab7, text='Media Release Consent Form')

first_name= Entry(tab1, width=10)
last_name= Entry(tab1, width=10)
date_of_birth= Entry(tab1, width=10)
ssn= Entry(tab1, width=10)
phone_number = Entry(tab1, width = 10)
email = Entry(tab1, width = 10)
current_address = Entry(tab1, width = 15)

emergency_contact_name = Entry(tab1, width = 15)
emergency_relationship = Entry(tab1, width = 15)
emergency_phone_number = Entry(tab1, width = 15)
emergency_cell_number = Entry(tab1, width = 15)
emergency_work_number = Entry(tab1, width = 15)
emergency_address = Entry(tab1, width = 15)




def Submit_Button():

    # with connection.cursor() as cursor:
    #
    #     sql = """INSERT INTO Student(student_id,
    #          first_name, last_name, date_of_birth, R_A, room_number)
    #          VALUES (5689, 'Hamza', 'Emrah', '1999-11-23', 'Ousmane', 531)"""
    #     cursor.execute(sql)
    #
    # connection.commit()

    if first_name.get()!= "":
        print("Ok voila bon")
    else:
        print("Missing input")

def layout():

    # Label(tab1, text = "Individual Information : NAU")
    # lbl1.grid(row = 1)

    Label(tab1, text = "Individual Information : NAU").grid(row = 1)

    #Row 2

    Label(tab1, text ="First Name: ").grid(row = 2)
    first_name.grid(row=2, column =1)
    Label(tab1, text ="Last Name: ").grid(row = 2, column=2)
    last_name.grid(row=2, column = 3)


    #Row 3
    Label(tab1, text ="Date of Birth: ").grid(row = 3)
    date_of_birth.grid(row=3, column = 1)
    Label(tab1, text ="Social Security Number: ").grid(row = 3, column=2)
    ssn.grid(row=3, column = 3)
    Label(tab1, text ="Gender: ").grid(row = 3, column=4)

    #Row 4
    Label(tab1, text="Phone Number: ").grid(row = 4)
    phone_number.grid(row = 4, column=1)
    Label(tab1, text="Email: ").grid(row = 4, column = 2)
    email.grid(row = 4, column=3)

    #Row 5
    Label(tab1, text="Current Adddress").grid(row = 5)
    current_address.grid(row  = 5, column=1)

    #Row6
    Label(tab1, text = "Emergency Contact").grid(row=6)

    Label(tab1, text = "Expected Move In: ").grid(row=7)
    combo = Combobox(tab1, width = 10)
    combo['values']=("Fall", "Spring", "Summer")
    combo.grid(row=7, column=1)




    # Create a potential submit button
    Button(tab1, text="Submit",fg="white", bg="red", command=Submit_Button).grid(row=8)

layout()
tab_control.pack(expand=1, fill='both')
window.mainloop()
