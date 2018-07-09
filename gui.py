from imports import *
root = Tk ()
root.title("American RENOLIT Corp. - Quality Control")
root.geometry('500x250')
# Paths, lists, etc.
database_path = "C:/Users/usftdt0/Documents/CleanDataBase.xlsx"
customer_path = "C:/Users/usftdt0/Documents/ARC customer list.xlsx"
customer_xlsx = pd.ExcelFile(customer_path)
df_customers = pd.read_excel(customer_xlsx)
customerlist = df_customers['Name 1'].tolist()
newlist = [i for i in customerlist if i != 'DO NOT USE' \
and i != 'DO NOT USE THIS CUSTOMER NUMBER' and i != 'Do Not Use-Duplicate' and i != 'DONOT USE']
filter_customerlist = []
for i in newlist:
	i.upper()
	filter_customerlist.append(i)
filter_customerlist = sorted(filter_customerlist)
optionlist = ['Elongation', 'Gloss', 'Shrinkage', 'Tensile', 'Thickness', 'Surface Tension Corona', '10% Modulus']
img = "C:/Users/usftdt0/Pictures/Renolit.jpg"
print("Loading Database...")
article_xlsx = pd.ExcelFile(database_path)
df_articles = pd.read_excel(article_xlsx, 'QC Data')
articlelist = df_articles['PH Mat. No.'].tolist()
articlelist = sorted(articlelist)
print("Database Loaded!")
# print(articlelist)
class RenolitGUI:
	def __init__(self, master):
		self.master = Frame(root, width=500, height=250, padding=(5,5,5,5))
		self.master.grid(column=0, row=0, sticky=(N,S,E,W))
		# self.frame = Frame(self.master, borderwidth=5, width=500, height=250)
		# self.frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))

		self.label = Label(self.master, text="ARC QC Data Analytics")
		self.label.configure(font=(18))
		self.label.grid(column=1, row=0, sticky=(N), padx=5, pady=5)

		self.customer = StringVar()
		self.customer.set(filter_customerlist[0])
		self.customer_label = Label(self.master, text="Customers")
		self.customer_label.grid(column=0, row=1, columnspan=2, sticky=(N,W))
		self.customer_menu = Combobox(self.master, textvariable = self.customer, values = filter_customerlist)
		self.customer_menu.grid(column=0, row=2, columnspan=2, sticky=(N,W))

		self.characteristics = StringVar()
		self.characteristics.set(optionlist[0])
		self.characteristics_label = Label(self.master, text="QC Characteristics")
		self.characteristics_label.grid(column=0, row=3, columnspan=2, sticky=(N,W))
		self.characteristics_option_menu = Combobox(self.master, textvariable = self.characteristics, values = optionlist)
		self.characteristics_option_menu.grid(column=0, row=4, columnspan=2, sticky=(N,W))

		self.article = StringVar()
		self.article.set(articlelist[0])
		self.article_label = Label(self.master, text="Article Number")
		self.article_label.grid(column=0, row=5, columnspan=2, sticky=(N,W))
		self.article_option_menu = Combobox(self.master, textvariable=self.article, values = articlelist)
		self.article_option_menu.grid(column=0, row=6, columnspan=2, sticky=(N,W))

		self.calc_button = Button(self.master, text="Get Statistics", command=self.Statistics)
		self.calc_button.configure(width=15)
		self.calc_button.grid(column=1, row=7, columnspan=1, sticky=(N,W))

		self.trend = Button(self.master, text="Show Trend Line", command=self.TrendLine)
		self.trend.configure(width=15)
		self.trend.grid(column=2, row=7, columnspan=1, sticky=(N,W), padx=5,pady=5)

		self.predict = Button(self.master, text="Predictive Tools", command=self.Predictions)
		self.predict.configure(width=15)
		self.predict.grid(column=3, row=7, columnspan=1, sticky=(N,W))

		# self.image = ImageTk.PhotoImage(Image.open(img))
		# self.image_label = Label(self.master, image=self.image)
		# self.image_label.configure(background = 'white')
		# self.image_label.grid()

	def Statistics(self):
		if str(self.characteristics.get()) == 'Elongation':
			print("Elongation")
		else:
			pass
		if str(self.characteristics.get()) == 'Gloss':
			print("Gloss")
		else:
			pass
		if str(self.characteristics.get()) == 'Shrinkage':
			print("Shrinkage")
		else:
			pass
		if str(self.characteristics.get()) == 'Tensile':
			print("Tensile")
		else:
			pass
		if str(self.characteristics.get()) == 'Thickness':
			print("Thickness")
		else:
			pass
		if str(self.characteristics.get()) == 'Surface Tension Corona':
			print("Surface Tension Corona")
		else:
			pass
		if str(self.characteristics.get()) == '10% Modulus':
			print("10% Modulus")
		else:
			pass

	def TrendLine(self):
		pass

	def Predictions(self):
		pass

my_gui = RenolitGUI(root)
root.mainloop()
