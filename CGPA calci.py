from tkinter import *
from tkinter.ttk import Combobox
root=Tk()
root.title("CGPA Calculator")
root.geometry("1400x700+50+50")

l1=Label(text="NAME  : ").place(x=50,y=30)
l2=Label(text="REG NO  : ").place(x=50,y=70)
l3=Label(text="SECTION  : ").place(x=50,y=110)
l4=Label(text="COURSE  : ").place(x=50,y=150)

e1=Entry(borderwidth=3)
e1.focus()
e1.place(x=120,y=30)
e2=Entry(borderwidth=3).place(x=120,y=70)
e3=Entry(borderwidth=3).place(x=120,y=110)
e4=Entry(borderwidth=3).place(x=120,y=150)

l5=Label(text="SEMESTER 1",font=("Arial",15)).place(x=590,y=10)
l5=Label(text="SEMESTER 2",font=("Arial",15)).place(x=1090,y=10)
l5=Label(text="SUBJECTS").place(x=400,y=60)
l5=Label(text="SUBJECTS").place(x=900,y=60)
l5=Label(text="GRADES").place(x=545,y=60)
l5=Label(text="GRADES").place(x=1045,y=60)
l5=Label(text="CREDIT SCORE").place(x=670,y=60)
l5=Label(text="CREDIT SCORE").place(x=1170,y=60)

#Label of Sem 1

l6=Label(text="SUBJECT 1  :").place(x=400,y=100)
l7=Label(text="SUBJECT 2  :").place(x=400,y=140)
l8=Label(text="SUBJECT 3  :").place(x=400,y=180)
l9=Label(text="SUBJECT 4  :").place(x=400,y=220)
l10=Label(text="SUBJECT 5  :").place(x=400,y=260)
l11=Label(text="SUBJECT 6  :").place(x=400,y=300)
l12=Label(text="SUBJECT 7  :").place(x=400,y=340)
l13=Label(text="SUBJECT 8  :").place(x=400,y=380)
l14=Label(text="SUBJECT 9  :").place(x=400,y=420)

#Label of Sem 2

l15=Label(text="SUBJECT 1  :").place(x=900,y=100)
l16=Label(text="SUBJECT 2  :").place(x=900,y=140)
l17=Label(text="SUBJECT 3  :").place(x=900,y=180)
l18=Label(text="SUBJECT 4  :").place(x=900,y=220)
l19=Label(text="SUBJECT 5  :").place(x=900,y=260)
l20=Label(text="SUBJECT 6  :").place(x=900,y=300)
l21=Label(text="SUBJECT 7  :").place(x=900,y=340)
l22=Label(text="SUBJECT 8  :").place(x=900,y=380)
l23=Label(text="SUBJECT 9  :").place(x=900,y=420)

# Grades of Sem 1

grade=['O','A','A+','B','B+','C','D','E','FAIL']
e6=Combobox(root,values=grade).place(x=500,y=100)
e7=Combobox(root,values=grade).place(x=500,y=140)
e8=Combobox(root,values=grade).place(x=500,y=180)
e9=Combobox(root,values=grade).place(x=500,y=220)
e10=Combobox(root,values=grade).place(x=500,y=260)
e11=Combobox(root,values=grade).place(x=500,y=300)
e12=Combobox(root,values=grade).place(x=500,y=340)
e13=Combobox(root,values=grade).place(x=500,y=380)
e14=Combobox(root,values=grade).place(x=500,y=420)

#Credit score of sem 1

e61=Spinbox(from_ = 0, to = 5).place(x=650,y=100)
e62=Spinbox(from_ = 0, to = 5).place(x=650,y=140)
e63=Spinbox(from_ = 0, to = 5).place(x=650,y=180)
e64=Spinbox(from_ = 0, to = 5).place(x=650,y=220)
e65=Spinbox(from_ = 0, to = 5).place(x=650,y=260)
e66=Spinbox(from_ = 0, to = 5).place(x=650,y=300)
e67=Spinbox(from_ = 0, to = 5).place(x=650,y=340)
e68=Spinbox(from_ = 0, to = 5).place(x=650,y=380)
e69=Spinbox(from_ = 0, to = 5).place(x=650,y=420)

# Grades of Sem 2

e15=Combobox(root,values=grade).place(x=1000,y=100)
e16=Combobox(root,values=grade).place(x=1000,y=140)
e17=Combobox(root,values=grade).place(x=1000,y=180)
e18=Combobox(root,values=grade).place(x=1000,y=220)
e19=Combobox(root,values=grade).place(x=1000,y=260)
e20=Combobox(root,values=grade).place(x=1000,y=300)
e21=Combobox(root,values=grade).place(x=1000,y=340)
e22=Combobox(root,values=grade).place(x=1000,y=380)
e23=Combobox(root,values=grade).place(x=1000,y=420)

#Credit score of sem 2

e71=Spinbox(from_ = 0, to = 5).place(x=1150,y=100)
e72=Spinbox(from_ = 0, to = 5).place(x=1150,y=140)
e73=Spinbox(from_ = 0, to = 5).place(x=1150,y=180)
e74=Spinbox(from_ = 0, to = 5).place(x=1150,y=220)
e75=Spinbox(from_ = 0, to = 5).place(x=1150,y=260)
e76=Spinbox(from_ = 0, to = 5).place(x=1150,y=300)
e77=Spinbox(from_ = 0, to = 5).place(x=1150,y=340)
e78=Spinbox(from_ = 0, to = 5).place(x=1150,y=380)
e79=Spinbox(from_ = 0, to = 5).place(x=1150,y=420)

B1 = Button(text="CALCULATE TGPA",font=("Times New Roman",13)).place(x=400,y=497)
L1 = Label(text="--->>").place(x=560,y=500)
E1 = Entry(width=25,borderwidth=3).place(x=600,y=503)

B2 = Button(text="CALCULATE TGPA",font=("Times New Roman",13)).place(x=900,y=497)
L2 = Label(text="--->>").place(x=1060,y=500)
E2 = Entry(width=25,borderwidth=3).place(x=1100,y=503)

B3 = Button(text="CALCULATE CGPA",font=("Times New Roman",17)).place(x=620,y=580)
L3 = Label(text="--->>").place(x=860,y=580)
L3 = Label(text="--->>").place(x=860,y=600)
E3 = Text(width=15,height=3,borderwidth=3)
#E3.insert(INSERT,"")
E3.place(x=920,y=575)

l100 = Label(text="PRESS 'SUBMIT' TO STORE YOUR RESULT :",font=("Times New Roman",12)).place(x=20,y=300)
b100 = Button(text="SUBMIT", font=("Times New Roman",13)).place(x=130,y=340)

root.mainloop()