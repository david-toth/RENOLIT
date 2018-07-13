from imports import *

root = Tk ()

database_path = "O:/Quality/QC Data Project/CleanDataBase.xlsx"
customer_path = "O:/Quality/QC Data Project/ARC customer list - copy.xlsx"

filter_customerlist = []
None_values = []

customer_xlsx = pd.ExcelFile(customer_path)
df_customers = pd.read_excel(customer_xlsx)
customerlist = df_customers['Name 1'].tolist()

newlist = [i for i in customerlist if i != 'DO NOT USE' \
and i != 'DO NOT USE THIS CUSTOMER NUMBER' and i != 'Do Not Use-Duplicate' and i != 'DONOT USE']

for i in newlist:
	if type(i) is str:
		i.upper()
		filter_customerlist.append(i)
	else:
		i = str(i)
		filter_customerlist.append(i)

filter_customerlist = sorted(filter_customerlist)
optionlist = [
				'10% Modulus & Elongation MD aged', "Color Lab DE*", "Elongation at Break MD aged",
				"Gloss 20° drive side", "Gloss 20° heat side", "Gloss 20° drive side", "Gloss 60° drive side",
				"Gloss 60° heat side", "Gloss 60° lacquer drive side", "Gloss 85° drive side",
			 	"Shrink (10'/ 70°) drive side", "Shrink (10'/ 80°) drive side", "Shrink (10'/ 100°) drive side",
				"Surface Tension Corona", "Tensile stress at break MD aged", "Thickness drive side",
				"Thickness heat side"
]
article_list = []
start_time = time.time()
print("Loading Database...Wait time is approximately 2 minutes")
article_xlsx = pd.ExcelFile(database_path)
df_articles = pd.read_excel(article_xlsx, 'QC Data')
articlelist = df_articles['PH Mat. No.'].tolist()
for i in articlelist:
	if type(i) is str and i not in article_list:
		article_list.append(i)
	else:
		i = str(i)
		if i not in article_list:
			article_list.append(i)
article_list = sorted(article_list)
print("Database Loaded in %s minutes" % (float((time.time() - start_time)/60)))

class RenolitGUI:
	def __init__(self, root):
		self.df = pd.read_excel(article_xlsx)
		self.selection_list = []

		self.label = Label(root, text="ARC QC Data Analytics")
		self.label.configure(font=('Arial', 18, 'bold'))
		self.label.grid(column=1, row=0, sticky=(N),  padx=5, pady=5)

		self.customer = StringVar()
		self.customer.set(filter_customerlist[0])
		self.customer_label = Label(root, text="Customers")
		self.customer_label.configure(font=('Arial', 10, 'bold'))
		self.customer_label.grid(column=1, row=1, sticky=(S,W), padx = (10,0))
		self.customer_menu = Listbox(root,width = 45,selectmode=EXTENDED, takefocus=0)
		for i in filter_customerlist:
			self.customer_menu.insert(END, i)
		self.customer_menu.bind("<<ListboxSelect>>", self.DoubleClick)
		self.customer_menu.bind("<Button-3>", self.RemoveEntry)
		self.customer_menu.grid(column=1, row=2, sticky=(N,W), padx = (10,0))
		self.scrollbar = Scrollbar(root, orient=VERTICAL, command=self.customer_menu.yview)
		self.scrollbar.grid(column=2, row=2, sticky='ns')
		self.customer_menu.configure(yscrollcommand = self.scrollbar.set)

		self.article = StringVar()
		self.article.set(article_list[0])
		self.article_label = Label(root, text="Article Number")
		self.article_label.configure(font=('Arial', 10, 'bold'))
		self.article_label.grid(column=1, row=3, sticky=(N,W), padx = (10,0))
		self.article_option_menu = Listbox(root, width=45, selectmode=EXTENDED, takefocus=0)
		for i in article_list:
			self.article_option_menu.insert(END, i)
		self.article_option_menu.bind("<<ListboxSelect>>", self.DoubleClick)
		self.article_option_menu.bind("<Button-3>", self.RemoveEntry)
		self.article_option_menu.grid(column=1, row=4, sticky=(N,W), padx = (10,0), pady=(0,10))
		self.scrollbar2 = Scrollbar(root, orient=VERTICAL, command=self.article_option_menu.yview)
		self.scrollbar2.grid(column=2, row=4, sticky='ns')
		self.article_option_menu.configure(yscrollcommand = self.scrollbar2.set)

		self.characteristics = StringVar()
		self.characteristics.set(optionlist[0])
		self.characteristics_label = Label(root, text="QC Characteristics")
		self.characteristics_label.configure(font=('Arial', 10, 'bold'))
		self.characteristics_label.grid(column=1, row=5, sticky=(N,W), padx = (10,0))
		self.characteristics_option_menu = Listbox(root, width=45, selectmode=SINGLE, takefocus=0)
		for i in optionlist:
			self.characteristics_option_menu.insert(END, i)
		self.characteristics_option_menu.bind("<<ListboxSelect>>", self.DoubleClick)
		self.characteristics_option_menu.bind("<Button-3>", self.RemoveEntry)
		self.characteristics_option_menu.grid(column=1, row=6, sticky=(N,W), padx = (10,0), pady=(0,10))
		self.scrollbar3 = Scrollbar(root, orient=VERTICAL, command=self.characteristics_option_menu.yview)
		self.scrollbar3.grid(column=2, row=6, sticky='ns')
		self.characteristics_option_menu.configure(yscrollcommand = self.scrollbar3.set)

		self.calc_button = Button(root, text="Get Statistics", command=self.Statistics)
		self.calc_button.configure(width=15)
		self.calc_button.grid(column=4, row=1,  padx=10)

		self.trend = Button(root, text="Show Trend Line", command=self.TrendLine)
		self.trend.configure(width=15)
		self.trend.grid(column=5, row=1,  padx=10)

		self.predict = Button(root, text="Predictive Tools", command=self.Predictions)
		self.predict.configure(width=15)
		self.predict.grid(column=6, row=1,  padx=10)

		self.progressbar = Progressbar(root, orient=HORIZONTAL, length=200)
		self.progressbar.configure(mode='indeterminate')
		self.progressbar.grid(column=5, row=6, sticky='se')
		self.progressbar_label = Label(root, text='Progress:')
		self.progressbar_label.grid(column=4, row=6, sticky='se')

		messagebox.showinfo(title="Welcome", message="Welcome to the ARC Quality Control Analysis Software. \
		Please note that no analytical tools are available at this time, as the program is under construction.")

	def Statistics(self):
		messagebox.showinfo(title="Get Statistics", message="Statistics are not yet available.")


	def TrendLine(self):
		messagebox.showinfo(title="Show Trend Line", message="The trend line feature is not yet available.")

	def Predictions(self):
		messagebox.showinfo(title='Predictive Tools', message="Predictive features are not yet available.")

	def on_customer_menu(idx, val):
		print('Customer menu idx: %s, value: %s' % (idx, val))

	def on_article_menu(idx, val):
		print('Article menu idx: %s, value: %s' % (idx, val))

	def on_characteristics_menu(idx, val):
		print('Characteristics menu idx: %s, value: %s' % (idx, val))

	def DoubleClick(self, event):
		widget = event.widget
		try:
			selection = widget.curselection()
			for i in selection:
				value = widget.get(i)
				if value not in self.selection_list:
					self.selection_list.append(value)
				else:
					pass 
			for j in self.selection_list:
				print(j)
			print("---------")
		except IndexError:
			return
		if self is self.customer_menu:
			return on_customer_menu(idx, widget.get(idx))
		if self is self.article_option_menu:
			return on_article_menu(idx, widget.get(idx))
		if self is self.characteristics_option_menu:
			return on_characteristics_menu(idx, widget.get(idx))

	def RemoveEntry(self, event):
		widget = event.widget
		if (0):
			try:
				selection = widget.curselection()
				for i in selection:
					value = widget.get(i)
					self.selection_list.remove(value)
				for j in self.selection_list:
					print(j)
				print("---------")
			except IndexError:
				return
			if self is self.customer_menu:
				return on_customer_menu(idx, widget.get(idx))
			if self is self.article_option_menu:
				return on_article_menu(idx, widget.get(idx))
			if self is self.characteristics_option_menu:
				return on_characteristics_menu(idx, widget.get(idx))
		if (1):
			self.selection_list = []
			print("------------")

root.title("American RENOLIT Corp. - Quality Control BETA")
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

my_gui = RenolitGUI(root)
root.mainloop()
