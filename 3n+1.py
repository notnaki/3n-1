from math import trunc
import matplotlib.pyplot as plt
from tkinter import *

root = Tk()
root.geometry("200x150")
root.title("3n+1")




value = Entry(root, width=10)
value.pack()
value.get()

def click():
    global X
    mylbl = Label(root, text=value.get())
    mylbl.pack()
    X = value.get()
    root.destroy()
    
    

myButton = Button(root, text="Please enter a number :", command = click)
myButton.pack()


root.mainloop()


X = int(X)



time = 0
x_gr = 0

x = []

y = []
 
while True:
    print(trunc(X))
    if X == 1:
        break
    x.append(x_gr)
    
    x_gr += 1
    
    if X%2 == 0:
        X = X/2
        y.append(trunc(X))
    else:
        X = X*3 + 1
        y.append(trunc(X))


print(y)
print(x)


plt.plot(x,y,marker="o")
 

plt.xlabel('x')

plt.ylabel('y')
 

plt.title('3n + 1')
plt.yticks(y)

plt.show()

