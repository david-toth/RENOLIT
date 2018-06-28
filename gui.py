from imports import *

class RenolitGUI:
    def __init__(self, master):
        self.master = master
        master.title("Renolit Quality Control")

        self.label = Label(master, text="Quality Control Data Project")
        self.label.pack()

        self.calc_button = Button(master, text="Calculation", command=self.calculate)
        self.calc_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def calculate(self):
        x = []
        for i in range(100):
            x.append(i)
        y = []
        for i in range(100):
            y.append(i**2)
        np_y = np.array(y)
        np_x = np.array(x)
        plt.scatter(np_x, np_y)
        plt.show()
    def close(self):
        plt.close()

root = Tk()
my_gui = RenolitGUI(root)
root.geometry("500x500")
root.mainloop()
