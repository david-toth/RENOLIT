from imports import *
root = Tk ()
root.title("American RENOLIT Corp. - Quality Control v0.1")
root.rowconfigure(0, weight =1)
root.rowconfigure(1, weight =1)
root.rowconfigure(2, weight =1)
root.rowconfigure(3, weight =1)
root.rowconfigure(4, weight =1)
root.rowconfigure(5, weight =1)
root.rowconfigure(6, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
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
	if type(i) is str:
		i.upper()
		filter_customerlist.append(i)
	else:
		i = str(i)
		filter_customerlist.append(i)
filter_customerlist = sorted(filter_customerlist)

optionlist = ['0','Elongation', 'Gloss', 'Shrinkage', 'Tensile', 'Thickness', 'Surface Tension Corona', '10% Modulus']
img = "C:/Users/usftdt0/Pictures/Renolit.jpg"
None_values = []
print("Loading Database...")
article_xlsx = pd.ExcelFile(database_path)
df_articles = pd.read_excel(article_xlsx, 'QC Data')
articlelist = df_articles['PH Mat. No.'].tolist()
articlelist = sorted(articlelist)
print("Database Loaded!")

class RenolitGUI:
	def __init__(self, root):
		self.label = Label(root, text="ARC QC Data Analytics")
		self.label.configure(font=('Arial', 18, 'bold'))
		self.label.grid(column=1, row=0, sticky=(N),  padx=5, pady=5)

		self.customer = StringVar()
		self.customer.set(filter_customerlist[0])
		self.customer_label = Label(root, text="Customers")
		self.customer_label.configure(font=('Arial', 10, 'bold'))
		self.customer_label.grid(column=1, row=1, sticky=(N,W), padx = (10,0))
		self.customer_menu = Combobox(root, textvariable = self.customer, values = filter_customerlist)
		self.customer_menu.grid(column=1, row=2, sticky=(N,W), padx = (10,0))

		self.characteristics = StringVar()
		self.characteristics.set(optionlist[0])
		self.characteristics_label = Label(root, text="QC Characteristics")
		self.characteristics_label.configure(font=('Arial', 10, 'bold'))
		self.characteristics_label.grid(column=1, row=3, sticky=(N,W), padx = (10,0))
		self.characteristics_option_menu = Combobox(root, textvariable = self.characteristics, values = optionlist)
		self.characteristics_option_menu.grid(column=1, row=4, sticky=(N,W), padx = (10,0))

		self.article = StringVar()
		self.article.set(articlelist[0])
		self.article_label = Label(root, text="Article Number")
		self.article_label.configure(font=('Arial', 10, 'bold'))
		self.article_label.grid(column=1, row=5, sticky=(N,W), padx = (10,0))
		self.article_option_menu = Combobox(root, textvariable=self.article, values = articlelist)
		self.article_option_menu.grid(column=1, row=6, sticky=(N,W), padx = (10,0), pady=(0,10))

		self.calc_button = Button(root, text="Get Statistics", command=self.Statistics)
		self.calc_button.configure(width=15)
		self.calc_button.grid(column=3, row=3,  padx=10)

		self.trend = Button(root, text="Show Trend Line", command=self.TrendLine)
		self.trend.configure(width=15)
		self.trend.grid(column=4, row=3,  padx=10)

		self.predict = Button(root, text="Predictive Tools", command=self.Predictions)
		self.predict.configure(width=15)
		self.predict.grid(column=5, row=3,  padx=10)

		self.progressbar = Progressbar(root, orient=HORIZONTAL, length=200, mode = 'indeterminate')
		self.progressbar.grid(column=4, row=5)
		self.progressbar_label = Label(root, text='Progress:')
		self.progressbar_label.grid(column=3, row=5)
		
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
