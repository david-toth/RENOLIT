from imports import *

root = Tk ()

database_path = "O:/Quality/QC Data Project/CleanDataBase.xlsx"
customer_path = "O:/Quality/QC Data Project/ARC customer list - copy.xlsx"

optionlist = [
				'10% Modulus & Elongation MD aged', "Color Lab DE*", "Elongation at Break MD aged",
				"Gloss 20° drive side", "Gloss 20° heat side", "Gloss 20° drive side", "Gloss 60° drive side",
				"Gloss 60° heat side", "Gloss 60° lacquer drive side", "Gloss 85° drive side",
			 	"Shrink (10'/70°) drive side", "Shrink (10'/80°) drive side", "Shrink (10'/100°) drive side",
				"Surface Tension corona", "Tensile stress at break MD aged", "Thickness drive side",
				"Thickness heat side"
]
article_list = []
start_time = time.time()
print("Loading Database...Wait time is approximately 3 minutes")
df = pd.read_excel(database_path)
print("Database Loaded in %s minutes" % (float((time.time() - start_time)/60)))

class RenolitGUI:
	def __init__(self, root):
		self.df = pd.read_excel(database_path, 'QC Data')
		self.selection_list = []
		self.qc_charac_list = []
		self.legend_list = []

		self.label = Label(root, text="ARC QC Data Analytics")
		self.label.configure(font=('Arial', 18, 'bold'))
		self.label.grid(column=1, row=0, sticky=(N),  padx=5, pady=5)

		# self.customer = StringVar()
		# self.customer.set(filter_customerlist[0])
		# self.customer_label = Label(root, text="Customers")
		# self.customer_label.configure(font=('Arial', 10, 'bold'))
		# self.customer_label.grid(column=1, row=1, sticky=(S,W), padx = (10,0))
		# self.customer_menu = Listbox(root,width = 45,selectmode=EXTENDED, takefocus=0)
		# for i in filter_customerlist:
		# 	self.customer_menu.insert(END, i)
		# self.customer_menu.bind("<<ListboxSelect>>", self.DoubleClick)
		# self.customer_menu.bind("<Button-3>", self.RemoveEntry)
		# self.customer_menu.grid(column=1, row=2, sticky=(N,W), padx = (10,0))
		# self.scrollbar = Scrollbar(root, orient=VERTICAL, command=self.customer_menu.yview)
		# self.scrollbar.grid(column=2, row=2, sticky='ns')
		# self.customer_menu.configure(yscrollcommand = self.scrollbar.set)

		# self.article = StringVar()
		# self.article.set(article_list[0])
		# self.article_label = Label(root, text="Article Number")
		# self.article_label.configure(font=('Arial', 10, 'bold'))
		# self.article_label.grid(column=1, row=3, sticky=(N,W), padx = (10,0))
		# self.article_option_menu = Listbox(root, width=45, selectmode=EXTENDED, takefocus=0)
		# for i in article_list:
		# 	self.article_option_menu.insert(END, i)
		# self.article_option_menu.bind("<<ListboxSelect>>", self.DoubleClick)
		# self.article_option_menu.bind("<Button-3>", self.RemoveEntry)
		# self.article_option_menu.grid(column=1, row=4, sticky=(N,W), padx = (10,0), pady=(0,10))
		# self.scrollbar2 = Scrollbar(root, orient=VERTICAL, command=self.article_option_menu.yview)
		# self.scrollbar2.grid(column=2, row=4, sticky='ns')
		# self.article_option_menu.configure(yscrollcommand = self.scrollbar2.set)

		self.characteristics = StringVar()
		self.characteristics.set(optionlist[0])
		self.characteristics_label = Label(root, text="QC Characteristics")
		self.characteristics_label.configure(font=('Arial', 10, 'bold'))
		self.characteristics_label.grid(column=1, row=3, sticky=(N,W), padx = (10,0))
		self.characteristics_option_menu = Listbox(root, width=45, selectmode=SINGLE, takefocus=0)
		for i in optionlist:
			self.characteristics_option_menu.insert(END, i)
		self.characteristics_option_menu.bind("<<ListboxSelect>>", self.DoubleClick)
		self.characteristics_option_menu.bind("<Button-3>", self.RemoveEntry)
		self.characteristics_option_menu.grid(column=1, row=4, sticky=(N,W), padx = (10,0), pady=(0,10))
		self.scrollbar3 = Scrollbar(root, orient=VERTICAL, command=self.characteristics_option_menu.yview)
		self.scrollbar3.grid(column=2, row=4, sticky='ns')
		self.characteristics_option_menu.configure(yscrollcommand = self.scrollbar3.set)

		# self.check_label = Label(root, text="Select filter(s):")
		# self.check_label.grid(column=4, row=1)
		#
		# self.var1 = IntVar()
		# self.checkbox_cust = Checkbutton(root, text='Customer', variable=self.var1)
		# self.checkbox_cust.grid(column=5, row=1, padx=5)
		#
		# self.var2 = IntVar()
		# self.checkbox_article = Checkbutton(root, text='Article No.', variable=self.var2)
		# self.checkbox_article.grid(column=6, row=1,padx=5)

		self.DateLabel = Label(root, text='Date range (YYYY-MM-DD):')
		self.DateLabel.grid(column=4, row=1, padx=(0,10))

		self.DateEntry1 = Entry(root)
		self.DateEntry1.grid(column=5, row=1, sticky='e')
		self.DateEntry1.focus()

		self.DateToLabel = Label(root, text='to')
		self.DateToLabel.grid(column=6, row=1)

		self.DateEntry2 = Entry(root)
		self.DateEntry2.grid(column=7, row=1, sticky='w', padx=(0,10))

		self.ArticleNumber = Label(root, text='Article Number:')
		self.ArticleNumber.grid(column=4, row=2, pady=10)

		self.ArticleNumber_Entry = Entry(root)
		self.ArticleNumber_Entry.grid(column=5, row=2, pady=10)

		self.UpperLimit = Label(root, text="Upper Limit:")
		self.UpperLimit.grid(column=4, row=3)

		self.UpperLimit_Entry = Entry(root)
		self.UpperLimit_Entry.grid(column=5, row=3)

		self.LowerLimit = Label(root, text="Lower Limit:")
		self.LowerLimit.grid(column=6, row=3, padx=(10,0))

		self.LowerLimit_Entry = Entry(root)
		self.LowerLimit_Entry.grid(column=7, row=3, padx=(0,10))

		self.calc_button = Button(root, text="Get Statistics", command=self.Statistics)
		self.calc_button.configure(width=15)
		self.calc_button.grid(column=4, row=4,  padx=10)

		self.trend = Button(root, text="Show Trend Line", command=self.TrendLine)
		self.trend.configure(width=15)
		self.trend.grid(column=5, row=4,  padx=10)

		self.quit_button = Button(root, text='Quit', command=self.Quit)
		self.quit_button.configure(width=15)
		self.quit_button.grid(column=7, row=0, padx=10)

		self.message = Message(root, height=15, width=15)
		self.message.grid(column=4, row=5, columnspan=3, rowspan=3)

	def Statistics(self):
		for selection in self.selection_list:
			if selection in optionlist:
				qc_characteristic = selection

		article_no = self.ArticleNumber_Entry.get()

		row = df.loc[(df['Charac.'] == qc_characteristic) & (df['PH Mat. No.'] == article_no)]
		row = row.set_index(['Dates'])
		first_date = str(self.DateEntry1.get())
		second_date = str(self.DateEntry2.get())
		row = row.loc[first_date:second_date]

		stats = row['Avg'].describe()
		self.message.config(text=str(stats))

	def TrendLine(self):
		for selection in self.selection_list:
			if selection in optionlist:
				qc_characteristic = selection

		article_no = self.ArticleNumber_Entry.get()

		row = df.loc[(df['Charac.'] == qc_characteristic) & (df['PH Mat. No.'] == article_no)]
		row = row.set_index(['Dates'])
		first_date = str(self.DateEntry1.get())
		second_date = str(self.DateEntry2.get())
		row = row.loc[first_date:second_date]
		print_data = row[['Order:', 'Charac.', 'Avg']]
		print(print_data)

		x_ = row.index.values
		y_ = row['Avg'].values

		try:
			upper_limit = float(self.UpperLimit_Entry.get())
			lower_limit = float(self.LowerLimit_Entry.get())
		except:
			upper_limit = 0
			lower_limit = 0

		data_points = row['Avg'].tolist()
		for i in data_points:
			if i > upper_limit or i < lower_limit:
				messagebox.showinfo(title='Warning', message='Warning: You have at least one value out of specification range.')
				break

		units = row['Measurement'].values

		fig, ax = plt.subplots()
		title = article_no
		main_plot = plt.plot(x_, y_, 'bo', label=str(qc_characteristic))
		ax.grid(True)
		try:
			upper_plot = plt.axhline(y=upper_limit, color='r', label='Upper Limit')
			lower_plot = plt.axhline(y=lower_limit, color='g', label='Lower Limit')
		except:
			pass
		legend_properties = {'weight': 'bold'}
		plt.legend(prop=legend_properties)
		plt.title(('Article:' + str(title)), fontweight='bold')
		plt.ylabel(str(units[0]), fontweight='bold')
		plt.xlabel('Date', fontweight='bold')
		ax.xaxis.axis_date()
		ax.axes.set_xlim(left=first_date, right=second_date)
		self.qc_charac_list = []
		self.selection_list = []
		fig.autofmt_xdate()
		mng = plt.get_current_fig_manager()
		mng.window.state('zoomed')
		plt.show()
		plt.close()

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
				self.message.config(text=j)
			print("---------")
		except:
			pass

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
			self.qc_charac_list = []
			self.legend_list = []
			print("------------")

	def UpdateDatabase(self):
		messagebox.showinfo(title='WARNING', message='If you update the database, all plots will be closed \
		and the software will be shutdown after the update.')

		figs = list(map(plt.figure, plt.get_fignums()))
		for i in figs:
			plt.close(i)
		df = pd.read_excel(database_path, "QC Data")
		raw_data = gl.glob("O:/QUALITY/QC Data Project/Raw Data/*")
		df_rawdata = pd.DataFrame()

		for file in tqdm(raw_data):
			temp_df = pd.read_excel(file)
			df_rawdata = df_rawdata.append(temp_df, ignore_index=True)
		df_rawdata = df_rawdata.drop_duplicates()

		if (1):
			raw_order, raw_charac, raw_poid, raw_rollno = df_rawdata['Order:'].tolist(), df_rawdata['Charac.'].tolist(), df_rawdata['PO ID'].tolist(), df_rawdata['PO lfn'].tolist()
			order, charac, po_id, roll_no = df["Order:"].tolist(), df['Charac.'].tolist(), df['PO ID'].tolist(), df['PO lfn'].tolist()

			for a,b,c,d in tqdm(zip(raw_order, raw_charac, raw_poid, raw_rollno)):
				for e,f,g,h in zip(order, charac, po_id, roll_no):
					if a==e and b==f and c==g and d == h:
						row = df_rawdata.loc[(df_rawdata["Order:"] == a) & (df_rawdata["Charac."] == b) & (df_rawdata["PO ID"] == c) & (df_rawdata["PO lfn"] == d)]
						index = row.index
						df_rawdata = df_rawdata.drop(index)

		year_list = []
		for i in range(len(df_rawdata.index)):
			i = 2018
			year_list.append(i)

		index = df_rawdata.columns.get_loc('Date create')
		new_index = index + 1

		df_rawdata.insert(loc=new_index, column='Year', value=year_list)

		dates = df_rawdata['Date create']
		dates = dates.str[:5]
		dates = dates.str.replace(".", "-")

		years = df_rawdata['Year']
		new_dates = dates.astype(str) + '-' + years.astype(str)
		day = new_dates.str[0:2]
		month = new_dates.str[3:5]
		year = new_dates.str[6:]

		new_dates = year.astype(str) + '-' + month.astype(str) + '-' + day.astype(str)
		df_rawdata['New Dates'] = new_dates
		datetime = pd.to_datetime(df_rawdata['New Dates'])
		date_list = datetime.tolist()
		df_rawdata = df_rawdata.drop(columns=['New Dates'])
		df_rawdata.insert(loc=(index-1), column='Dates', value=date_list)

		df_rawdata.to_excel('NewDataBase.xlsx')
		database_df = pd.read_excel('NewDataBase.xlsx')
		characteristics_list = database_df['Charac.'].tolist()

		for n, i in enumerate(characteristics_list):
			if i == 'GLOSS 20Ã‚Â° drive side' or i == 'GlOSS 20Ã‚Â° drive side':
				characteristics_list[n] = 'Gloss 20° drive side'
			if i == "GLOSS 20Ã‚Â° heat side" or i == "GlOSS 20Ã‚Â° heat side":
				characteristics_list[n] = "Gloss 20° heat side"
			if i == 'GLOSS 60Ã‚Â° drive side' or i == 'GlOSS 60Ã‚Â° drive side':
				characteristics_list[n] = "Gloss 60° drive side"
			if i == 'GLOSS 60Ã‚Â° heat side' or i == 'GlOSS 60Ã‚Â° heat side':
				characteristics_list[n] = "Gloss 60° heat side"
			if i == 'GLOSS 60Ã‚Â°  lacquer drive side' or i == 'GLOSS 60Ã‚Â°  lacquer drive side':
				characteristics_list[n] = "Gloss 60° lacquer drive side"
			if i == 'GlOSS 85Ã‚Â° drive side' or i == 'GLOSS 85Ã‚Â° drive side':
				characteristics_list[n] = "Gloss 85° drive side"
			if i == "Shrink(10'/70Ã‚Â°) drive side":
				characteristics_list[n] = "Shrink (10'/70°) drive side"
			if i == "Shrink(10'/80Ã‚Â°) drive side" or i == "Shrink (10'/80Ã‚Â°) drive side":
				characteristics_list[n] = "Shrink (10'/80°) drive side"
			if i == "Shrink(10'/100Ã‚Â°) drive side":
				characteristics_list[n] = "Shrink (10'/100°) drive side"

		characteristics_list = sorted(characteristics_list)
		database_df = database_df.drop(columns=['Charac.'])
		charac_index = database_df.columns.get_loc('Plan No.')
		database_df.insert(loc=(charac_index-1), column='Charac.', value=characteristics_list)
		CleanDataBase_df = pd.concat([df, database_df])

	def Quit(self):
		figs = list(map(plt.figure, plt.get_fignums()))
		for i in figs:
			plt.close(i)
		plt.ion()
		plt.close("all")
		root.destroy()

root.title("American RENOLIT Corp. - Quality Control BETA")
root.rowconfigure(0, weight =1)
root.rowconfigure(1, weight =1)
root.rowconfigure(2, weight =1)
root.rowconfigure(3, weight =1)
root.rowconfigure(4, weight =1)
root.rowconfigure(5, weight =1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)
root.rowconfigure(7, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.columnconfigure(6, weight=1)
my_gui = RenolitGUI(root)
root.mainloop()
