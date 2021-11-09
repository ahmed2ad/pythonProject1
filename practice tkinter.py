from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window =Tk()

window.geometry('1290x740')

window.config(bg='sandy brown')

window.title('تخصصات كلية علوم وهندسة الحاسب الآلي بجامعة حفر الباطن')


mlable =Label(text="الرجاء اختيار التخصص ",fg = 'white' , bg = 'peru', font='Raleway').pack()


bg = ImageTk.PhotoImage(file="uhb3.jpeg")

# Create a canvas
canvas = Canvas(window,width= 100, height= 100)
canvas.pack(fill= "both", expand=True)

# Display image
canvas.create_image(550, 280 ,image=bg, anchor="nw")

def dsc():
    messagebox.showinfo('تخصص علوم البيانات','علوم البيانات هو تخصص يقوم بإستخدام الاساليب العلمية والخزارزميات والذكاء الصناعي ومعالجة البيانات وتحليلها لاستخراج معلومات قيمة ومفيدة  ')
mbutton = Button(text= "علوم البيانات" , height = 5, width = 20 ,fg='sandy brown' ,bg='saddle brown', command=dsc  ).place(x=850 , y=250)


def cyb():
    messagebox.showinfo('تخصص الأمن السيبراني','الأمن السيبراني هو تخصص يهدف الى حماية انظمة الحاسب الآلي من السرقة او الضرر الذي يلحق بالأجهزة ')
mbutton2 = Button(text= "الأمن السيبراني" , height = 5, width = 20, fg='sandy brown' ,bg='saddle brown', command=cyb ).place(x=400 , y=250)


def cse():
    messagebox.showinfo('تخصص علوم وهندسة الحاسب الآلي','علوم وهندسة الحاسب الألي هو تخصص يلم بالمعارف والمهارات اللازمة لتصميم وتطوير نظم الحاسب الآلي وحل مشاكل الحوسبة بمختلف انواعها ')
mbutton3 = Button(text="علوم وهندسة الحاسب الآلي", height = 5, width = 20, fg='sandy brown' ,bg='saddle brown',command=cse ).place(x=850, y=450)


def swe():
    messagebox.showinfo('تخصص هندسة البرمجيات','هندسة البرمجيات هو تخصص يمكنك من تقديم مبادئ واساليب هندسية سليمة من اجل إبتكار برامج عالية الجودة وتطويرها وتشغيلها ')
mbutton4 = Button(text= "هندسة البرمجيات" , height = 5, width = 20,fg='sandy brown' ,bg='saddle brown', command=swe ).place(x=400 , y=450)




window.mainloop()
