import matplotlib.pyplot as plt
import numpy as np
import math, customtkinter, tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
root=customtkinter.CTk()
root.geometry("1000x600")

def GetandCheckValues():
    global mean
    global deviation
    global max_x
    global min_x
    mean=int(entry1.get())
    deviation=int(entry2.get())
    max_x=int(entry4.get())
    min_x=int(entry3.get())
    if max_x<min_x:
        output_text_box.insert("0.0", "Invalid X values. Maximum is bigger than minimum. Enter again")


def main(): 
    GetandCheckValues()
    y=[]
    x=[]
    x_of_line_to_mean=[]
    y_of_line_to_mean=[]
    count=min_x
    while count<max_x:
        x.append(count)
        y.append((1/(deviation*(2*math.pi)**0.5)) * (math.e)**(-0.5 * ((count-mean)/deviation)**2))
        count=count+0.01
    maxy=y[0]
    for i in range (len(y)-1):
        if y[i]>maxy:
            maxy=y[i]
    y_count=y[0]
    while y_count<=maxy:
        y_of_line_to_mean.append(y_count)
        y_count=y_count+0.01
        x_of_line_to_mean.append(mean)
    if y_of_line_to_mean[-1] != maxy:
        y_of_line_to_mean.append(maxy)
        x_of_line_to_mean.append(mean)

    fig,ax =plt.subplots()
    ax.plot(x,y)
    ax.plot(x_of_line_to_mean,y_of_line_to_mean, color="red", linestyle="--", linewidth=2)
    ax.set_title("Normal Distribution")
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    plt.show()




frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=60, fill="both", expand=True)

entry1=customtkinter.CTkEntry(master=frame, placeholder_text="Enter Mean:")
entry1.pack(pady=20, padx=10)

entry2=customtkinter.CTkEntry(master=frame, placeholder_text="Enter Deviation:")
entry2.pack(pady=20, padx=10)

entry3=customtkinter.CTkEntry(master=frame, placeholder_text="Enter Min x value:")
entry3.pack(pady=20, padx=10)

entry4=customtkinter.CTkEntry(master=frame, placeholder_text="Enter Max x value:")
entry4.pack(pady=20, padx=10)

button=customtkinter.CTkButton(master=frame, text="Visualise", command=main, fg_color="#592C82")
button.pack(pady=12, padx=10)

output_text_box=customtkinter.CTkTextbox(master=frame, width=200, height=100)
output_text_box.pack(pady=12, padx=10)


root.mainloop()