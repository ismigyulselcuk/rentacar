from tkinter import *
import tkcalendar as d
from tkinter import ttk
import sqlite3

araba = sqlite3.connect("araba.db")
ar = araba.cursor()

calendar = d.DateEntry
ag = ["18", "19", "20", "21", "22", "23", "24", "25+"]
vlist1 = ["Blagoevgrad",
          "Burgas",
          "Dobrich",
          "Gabrovo",
          "Haskovo",
          "Kardzhali",
          "Kyustendil",
          "Lovech",
          "Montana",
          "Plovdiv",
          "Razgrad",
          "Ruse",
          "Shumen",
          "Silistra",
          "Sliven",
          "Smolyan",
          "Sofia",
          "Stara Zagora",
          "Targovishte",
          "Varna",
          "Veliko Tarnovo"]


vlist = ["00:00", "00:15", "00:30",
         "00:45", "01:00", "01:15", "01:30", "01:45", "02:00", "02:15", "02:30", "02:45",
         "03:00", "03:15", "03:30", "03:45", "04:00", "04:15", "04:30", "04:45", "05:00",
         "05:15", "05:30", "05:45", "06:00", "06:15", "06:30", "06:45", "07:00", "07:15",
         "07:30", "07:45", "08:00", "08:15", "08:30", "08:45", "09:00", "09:15", "09:30",
         "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00",
         "12:15", "12:30", "12:45"
         "13:00", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45",
         "15:00", "15:15", "15:30", "15:45", "15:00", "15:15", "15:30", "15:45", "16:00",
         "16:15", "16:30", "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15",
         "18:30", "18:45", "19:00", "19:15", "19:30", "19:45", "20:00", "20:15", "20:30",
         "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30", "22:45", "23:00",
         "23:15", "23:30", "23:45"]
root = Tk()
root.title("www.rentacar.com")
root.configure(bg="sky blue")


def openNewWindow():
    root1 = Toplevel(root)
    root1.title("www.Rentacar.com")
    root1.configure(bg="sky blue")

   # arabaa = araba.cursor()
    #araba.commit()

   # arabaa.execute("""Create Table adresses(
    #            car_name text,
    #            car_place in,
    #           car_doors integer,
    #            manuel_speed text,
     #           Auto_speed text,
      #          Air_con text,
       #         Disel text)""")

    klas = Label(root1, text="Car class")

    klas.grid()
    a = StringVar()
    b = StringVar()
    c = StringVar()
    d = StringVar()
    e = StringVar()
    f = StringVar()
    aa = StringVar()
    bb = StringVar()
    cc = StringVar()
    dd = StringVar()
    economical = Checkbutton(root1, text="Economical", variable=a, onvalue="on", bg="sky blue")
    economical.grid(row=2, sticky=W)
    compact = Checkbutton(root1, text="Compact", variable=b, bg="sky blue")
    compact.grid(row=3, sticky=W)
    estate = Checkbutton(root1, text="Estate", variable=c, bg="sky blue")
    estate.grid(row=4, sticky=W)
    minivan = Checkbutton(root1, text="Minivan", variable=d, bg="sky blue")
    minivan.grid(row=5, sticky=W)
    jeep = Checkbutton(root1, text="Jeep", variable=e, bg="sky blue")
    jeep.grid(row=6, sticky=W)
    electric = Checkbutton(root1, text="Electric", variable=f, bg="sky blue")
    electric.grid(row=7, sticky=W)
    obor = Label(root1, text="Equipment")
    obor.grid()
    air = Checkbutton(root1, text="Air conditioning", variable=aa, bg="sky blue")
    air.grid(row=9, sticky=W)
    speed = Checkbutton(root1, text="Automatic speeds", variable=bb, bg="sky blue")
    speed.grid(row=10, sticky=W)
    manuel = Checkbutton(root1, text="Manual speeds", variable=cc, bg="sky blue")
    manuel.grid(row=11, sticky=W)
    diesel = Checkbutton(root1, text="Diesel", variable=dd, bg="sky blue")
    diesel.grid(row=12, sticky=W)
    label= Label(root1,text=a.get())
    label.grid()


def openNewWindow1():
    root2 = Toplevel(root)
    root2.title("www.Rentacar.com")
    root2.configure(bg="sky blue")

    araba = sqlite3.connect("araba.db")
    ar= araba.cursor()
    def submit():
        araba = sqlite3.connect("araba.db")
        ar = araba.cursor()

        ar.execute("Insert into adreses Values(:car_name, :car_place, :car_doors,:manuel_speed,:Auto_speed, :Air_con, "
                   ":Disel, :Tipe_car, :Driver)",
                    {'car_name': carneme1.get(),
                     'car_place': numberofplace1.get(),
                     'car_doors': numberofdoors1.get(),
                     'manuel_speed': manspeed.get(),
                     'Auto_speed':autospeed1.get(),
                     'Air_con': aircon1.get(),
                     'Disel': disel1.get(),
                     'Tipe_car': cartipe1.get(),
                     'Driver': driver1.get()
        })
        araba.commit()
        araba.close()

        carneme1.delete(0, END)
        numberofplace1.delete(0, END)
        numberofdoors1.delete(0, END)
        manspeed.delete(0, END)
        autospeed1.delete(0, END)
        aircon1.delete(0, END)
        disel1.delete(0, END)
        cartipe1.delete(0,END)
        driver1.delete(0,END)

        root2.mainloop()
    def query():
        araba = sqlite3.connect("araba.db")
        ar = araba.cursor()

        ar.execute("Select *, oid from adreses")
        records= ar.fetchall()
        print_records= ""
        for record in records:
            print_records += str(record[0])+ "  "+ str(record[1])+ " " +str(record[2])+ " "+str(record[3])+\
                             " " +str(record[4])+ " " + str(record[5])+ " "+str(record[6])+"\t" +str(record[7])\
                             + " " +str(record[8])+" " +str(record[9])+ "\n"

        showdata1 = Label(root2, text= print_records,bg="sky blue")
        showdata1.grid(row= 12, column=1, columnspan=2)
        araba.commit()
        araba.close()
    def delete():

            araba = sqlite3.connect("araba.db")
            ar = araba.cursor()
            ar.execute("Delete from adreses where oid=" +delbox.get())
            delbox.delete(0,END)

            araba.commit()
            araba.close()
    carname = Label(root2, text="Car", bg="sky blue")
    carname.grid(row=1, column=1)
    carneme1 = Entry(root2)
    carneme1.grid(row=1, column=2)
    numberofplace = Label(root2, text="Number of place", bg="sky blue")
    numberofplace.grid(row=2, column=1)
    numberofplace1 = Entry(root2)
    numberofplace1.grid(row=2, column=2)
    numberofdoors = Label(root2, text="Number of doors", bg="sky blue")
    numberofdoors.grid(row=3, column=1)
    numberofdoors1 = Entry(root2)
    numberofdoors1.grid(row=3, column=2)
    manspeed1 = Label(root2, text="Manuel speed", bg="sky blue")
    manspeed1.grid(row=4,column=1)
    manspeed = Entry(root2)
    manspeed.grid(row=4, column=2)
    autospeed = Label(root2, text="Auto speed", bg="sky blue")
    autospeed.grid(row=5,column=1)
    autospeed1 = Entry(root2)
    autospeed1.grid(row=5, column=2)
    aircon = Label(root2, text="Air conditioner", bg="sky blue")
    aircon.grid(row=6,column=1)
    aircon1 = Entry(root2)
    aircon1.grid(row=6, column=2)
    disel = Label(root2, text="Disel", bg="sky blue")
    disel.grid(row=7,column=1)
    disel1 = Entry(root2)
    disel1.grid(row=7, column=2)
    submmit= Button(root2, text= "Save your car", command=submit, width=50)
    submmit.grid(row=10, column=1,columnspan=2)
    showdata= Button(root2,text= "Show all Cars", command= query,width=50)
    showdata.grid(row=11, column=1,columnspan=2)
    dlt = Button(root2, text="Delete record", command= delete, width=50)
    dlt.grid(row=15, column=1, columnspan=2)
    delbox = Entry(root2)
    delbox.grid(row=14, column=2)
    delbox1= Label(root2, text="Car ID")
    delbox1.grid(row=14,column=1)
    cartipe= Label(root2, text='Tipe of car')
    cartipe.grid(row=8, column=1)
    cartipe1= Entry(root2)
    cartipe1.grid(row=8,column=2)
    driver= Label(root2, text='Driver')
    driver.grid(row=9, column=1)
    driver1= Entry(root2)
    driver1.grid(row=9,column=2)
   # submmit1= Label(root2, text="Your save succses", bg="sky blue")
    #submmit1.grid(row=8, column=2,pady=20)

mylabel = Label(root, text="Book Online for the Best Rates with Isi")
mylabel.grid(pady=20, column=2)

text = Label(root, text="Couse your pick-up location")
text.grid(row=1, column=1)

myentry = ttk.Combobox(0, value=vlist1)
myentry.grid(row=2, column=1, pady=10)

text = Label(root, text="Coose your return location")
text.grid(row=3, column=1)

myentry1 = ttk.Combobox(root, value=vlist1)
myentry1.grid(row=4, column=1, pady=10)

cal = d.DateEntry(0, dateformat=3, width=12, background='dark blue', foreground='white', borderwidth=4, Calendar=2018)
cal.grid(row=2, column=2, pady=10)

cal1 = d.DateEntry(0, dateformat=3, width=12, background='dark blue', foreground='white', borderwidth=4, Calendar=2018)
cal1.grid(row=4, column=2, pady=10)


Age = ttk.Combobox(0, values=ag)
Age.set("Age")
Age.grid(row=5, column=3)

variablee = StringVar(root)
variablee.set(vlist[0])
variablee1 = StringVar(root)
variablee1.set(vlist[0])
time = OptionMenu(root, variablee, *vlist)
time.grid(row=2, column=3)

time = OptionMenu(root, variablee1, *vlist)
time.grid(row=4, column=3)

button = Button(root, text='Select my car', width=25, command=openNewWindow)
button.grid(row=6, column=1)
button = Button(root, text='Register a new car', width=25, command=openNewWindow1)
button.grid(row=6, column=2)

root.mainloop()
