from imports import *

class RenolitGUI:
    def __init__(self, master):
        # Creation of master page
        self.master = master
        master.title("Renolit Quality Control")
        # Creation of Label on page
        self.label = Label(master, text="Quality Control Data Project")
        self.label.pack()
        # Creation of button to perform a function
        self.calc_button = Button(master, text="Calculation", command=self.calculate)
        self.calc_button.pack()
        # Creation of a button to close page
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
        # Creation of drop-down option menu
        optionList = ('A', 'B')
        self.v = StringVar()
        self.v.set(optionList[0])
        self.option_menu = OptionMenu(master, self.v, *optionList)
        self.option_menu.pack()
        
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
        plt.close()

root = Tk()
my_gui = RenolitGUI(root)
root.geometry("500x500")
root.mainloop()
