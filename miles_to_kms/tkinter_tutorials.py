import tkinter

window = tkinter.Tk()
window.title("My First Tkinter Program")
window.minsize(width=500, height=400)

my_label = tkinter.Label(text="I Am The Label", font=("Contourier", 20, "bold"))
my_label.pack()

def button_click():
    input_text = input.get()
    my_label['text'] = input_text
    print("I got clicked!")


button = tkinter.Button(text="click me", command=button_click)
button.pack()

input = tkinter.Entry()
input.pack()
print(input.get())
window.mainloop()
