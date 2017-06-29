from Tkinter import Tk
from Window import Window


#Metodo Principal
def main():

    root = Tk()
    root.geometry("250x150+300+100")
    app = Window(root)
    root.mainloop()


if __name__ == "__main__":

    main()