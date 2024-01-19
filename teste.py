from customtkinter import *

window = CTk()

width= window.winfo_screenwidth()   
height= window.winfo_screenheight()
height -= (height / 10)   

window.geometry("%dx%d" % (width, height))
window.configure(fg = "#123456")

window.geometry(f"{width}x{height}")



def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = CTkOptionMenu(window, values=["Visível", "Invisível"],
                                         command=optionmenu_callback, fg_color="#340303", button_color="#2b0202",button_hover_color="#000000")
optionmenu.set("Visível")
optionmenu.pack()

def switch_event():
    print("switch toggled, current value:", switch_var.get())

switch_var = StringVar(value="on")
switch = CTkSwitch(window, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.pack()


tabview = CTkTabview(master=window)
tabview.pack(padx=20, pady=20)

tabview.add("tab 1")  # add tab at the end
tabview.add("tab 2")  # add tab at the end
tabview.set("tab 2")  # set currently visible tab

button = CTkButton(master=tabview.tab("tab 1"))
button.pack(padx=20, pady=20)

progressbar = CTkProgressBar(window, orientation="horizontal")
progressbar.configure(mode="indeterminate")
progressbar.configure(indeterminate_speed=2)
progressbar.pack()
progressbar.start()


def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = IntVar(value=0)
radiobutton_1 = CTkRadioButton(window, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = CTkRadioButton(window, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)

radiobutton_1.pack()
radiobutton_2.pack()


def segmented_button_callback(value):
    print("segmented button clicked:", value)

segmented_button_var = StringVar(value="Value 1")
segmented_button = CTkSegmentedButton(window, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segmented_button_var)

segmented_button.pack()

def slider_event(value):
    print(value)

slider = CTkSlider(window, from_=0, to=100, command=slider_event)
slider.pack()

toplevel = CTkToplevel()  # master argument is optional 



def button_click_event():
    toplevel.focus()
    dialog = CTkInputDialog(text="Type in a number:", title="Test")
    print("Number:", dialog.get_input())


button = CTkButton(window, text="Open Dialog", command=button_click_event)
button.pack(padx=20, pady=20)







window.mainloop()