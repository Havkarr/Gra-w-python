from tkinter import *


def main():
    
    # Create window 
    window = Tk()
    # Set size of the window
    window.geometry("500x600")
    
    # Set images
    bg = PhotoImage(file = ".\\photos\\background.png")
    bird = PhotoImage(file=".\\photos\\Bird.png")
    leftSpike = PhotoImage(file = ".\\photos\\left_spike.png")
    rightSpike = PhotoImage(file = ".\\photos\\right_spike.png")

    # Show background with label
    label1 = Label(window, 
                   image = bg)
    label1.place(x=-2, y=0)

    label2 = Label(window, 
                   image = leftSpike,
                   bg = "#519FDE")
    label2.place(x=17, y=50)

    label3 = Label(window, 
                   image=bird,
                   bg = "#519FDE")
    label3.place(x=250, y=250)

    window.mainloop()


if __name__ == "__main__":
    main()