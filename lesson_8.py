# x = 5
# def xxx():
#     global x
#     x =+ 2
#     print(x)
# xxx()
# print(x)
# r = lambda r: r + 5
# print(r(5))
import tkinter
root = tkinter.Tk()
root.title("lambda")
def pec():
    x = 7
    y = 34
    z = x + y
    print(z)
Button = tkinter.Button(root, text = "нажми меня", command = pec)
Button.pack()
root.mainloop()
