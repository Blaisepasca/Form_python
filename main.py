from tkinter import *
root = Tk()
root.geometry("500x350")

Label(root, text= "Python Registration Form" , font="arial 15 bold").grid(row=0 , column=3)

name = Label(root, text="Name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
emergency = Label(root, text="emergency")
payementmood = Label(root, text="payement mood")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payementmood.grid(row=5, column=2)

namevalue = StringVar
phonevalue =StringVar
gendervalue = StringVar
emergencyvalue = StringVar
payementmood = StringVar

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
payementmoodentry = Entry(root, textvariable=payementmoodvalue)

root.mainloop()