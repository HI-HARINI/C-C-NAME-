from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("Lucky Friend-1D")

label1=Label(root)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5, rely=0.3, anchor=CENTER)
label3=Label(root)
label3.place(relx=0.5, rely=0.7, anchor=CENTER)
label4=Label(root)
label4.place(relx=0.5, rely=0.8, anchor=CENTER)
list1=[]
list2=[]
print(list1)

entrybox=Entry(root)
entrybox.place(relx=0.5, rely=0.1,anchor=CENTER)
entrybox2=Entry(root)
entrybox2.place(relx=0.5, rely=0.2,anchor=CENTER)


def rn():
    value=entrybox.get()
    value2=entrybox2.get()
    list1.append(value)
    list2.append(value2)
    label2["text"]=list1
    label1["text"]=list2
    

def rm():
    length=len(list1)
    length2=len(list2)
    ranu1=random.randint(0, length)
    
    random1=list1[ranu1]
    random2=list2[ranu1]
    label3["text"]=random1
    label4["text"]=random2

button=Button(root,text="Display Country & City Name",command=rn)
button.place(relx=0.5, rely=0.4, anchor=CENTER)
button1=Button(root,text="Display Random Country & City Name",command=rm)
button1.place(relx=0.5, rely=0.6, anchor=CENTER)



root.mainloop()