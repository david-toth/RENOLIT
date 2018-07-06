from imports import *

class RenolitGUI:
	def __init__(self, master):
		self.master = master
		master.title("Renolit Quality Control")

		self.label = Label(master, text="Quality Control Data Project")
		self.label.configure(font=(18))
		self.label.pack()

		self.calc_button = Button(master, text="Get Statistics", command=self.Statistics)
		self.calc_button.pack()

		self.trend = Button(master, text="Show Trend Line", command=self.TrendLine)
		self.trend.pack()

		optionlist = ['Elongation', 'Gloss', 'Shrinkage', 'Tensile', 'Thickness', 'Surface Tension Corona', '10% Modulus']
		self.v = StringVar()
		self.v.set(optionlist[0])
		self.option_menu = OptionMenu(master, self.v, *optionlist)
		self.option_menu.pack()

		self.close_button = Button(master, text="Close", command=master.quit)
		self.close_button.pack()

		img = "C:/Users/usftdt0/Pictures/Renolit.jpg"
		self.image = ImageTk.PhotoImage(Image.open(img))
		self.image_label = Label(master, image=self.image)
		self.image_label.configure(background = 'white')
		self.image_label.pack(side='bottom', fill='both', expand='yes')

	def Statistics(self):
		if str(self.v.get()) == 'Elongation':
			print("Elongation")
		else:
			pass
		if str(self.v.get()) == 'Gloss':
			print("Gloss")
		else:
			pass
		if str(self.v.get()) == 'Shrinkage':
			print("Shrinkage")
		else:
			pass
		if str(self.v.get()) == 'Tensile':
			print("Tensile")
		else:
			pass
		if str(self.v.get()) == 'Thickness':
			print("Thickness")
		else:
			pass
		if str(self.v.get()) == 'Surface Tension Corona':
			print("Surface Tension Corona")
		else:
			pass
		if str(self.v.get()) == '10% Modulus':
			print("10% Modulus")
		else:
			pass
			
	def TrendLine(self):
		pass

root = Tk()
my_gui = RenolitGUI(root)
root.configure(background='white')
root.geometry("1000x1000")
root.mainloop()
