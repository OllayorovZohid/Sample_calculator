import tkinter

from matplotlib.ft2font import BOLD
from numpy import size

expression = ''
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ''
    equation.set(expression)

if __name__ == "__main__":
    window = tkinter.Tk()
    window.geometry('330x300')
    window.title('Calculator')
    equation = tkinter.StringVar()
    expression_field = tkinter.Entry (window, textvariable=equation,font=BOLD,width=32).place(x=20,y=10)
    button_1 = tkinter.Button(window,command=lambda :press(1), text='1',width=6,height=3,bg='white',fg='blue').place(x=20,y=40)
    button_2 = tkinter.Button(window,command=lambda :press(2),text='2',width=6,height=3,bg='white',fg='blue').place(x=80,y=40)
    button_3 = tkinter.Button(window,command=lambda :press(3),text='3',width=6,height=3,bg='white',fg='blue').place(x=140,y=40)
    button_C = tkinter.Button(window,command=lambda :clear(),text='C',width=6,height=3,bg='white',fg='red').place(x=200,y=40)
    button_CE = tkinter.Button(text='CE',width=6,height=3,bg='white',fg='red').place(x=260,y=40)
    button_4 = tkinter.Button(window,command=lambda :press(4),text='4',width=6,height=3,bg='white',fg='blue').place(x=20,y=100)
    button_5 = tkinter.Button(window,command=lambda :press(5),text='5',width=6,height=3,bg='white',fg='blue').place(x=80,y=100)
    button_6 = tkinter.Button(window,command=lambda :press(6),text='6',width=6,height=3,bg='white',fg='blue').place(x=140,y=100)
    button_qoshish = tkinter.Button(window,command=lambda :press('+'),text='+',width=6,height=3,bg='white',fg='blue').place(x=200,y=100)
    button_kopaytirish = tkinter.Button(window,command=lambda :press('*'),text='*',width=6,height=3,bg='white',fg='blue').place(x=260,y=100)
    button_7 = tkinter.Button(window,command=lambda :press(7),text='7',width=6,height=3,bg='white',fg='blue').place(x=20,y=160)
    button_8 = tkinter.Button(window,command=lambda :press(8),text='8',width=6,height=3,bg='white',fg='blue').place(x=80,y=160)
    button_9 = tkinter.Button(window,command=lambda :press(9),text='9',width=6,height=3,bg='white',fg='blue').place(x=140,y=160)
    button_ayiruv = tkinter.Button(window,command=lambda :press('-'),text='-',width=6,height=3,bg='white',fg='blue').place(x=200,y=160)
    button_bolish = tkinter.Button(window,command=lambda :press('/'),text='/',width=6,height=3,bg='white',fg='blue').place(x=260,y=160)
    button_nol = tkinter.Button(window,command=lambda :press(0),text='0',width=14,height=3,bg='white',fg='blue').place(x=20,y=220)
    button_nuqta = tkinter.Button(window,command=lambda :press('.'),text='.',width=6,height=3,bg='white',fg='blue').place(x=140,y=220)
    button_teng = tkinter.Button(window,command=equalpress,text='=',width=15,height=3,bg='white',fg='blue').place(x=200,y=220)
    window.mainloop()