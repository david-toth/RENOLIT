from imports import *

def Combine_Data():
	"""
	Function that collects several Excel files and concatonates
	them into one large file. Use the first 'if' block you want to write
	directly to an Excel file -- WARNING: VERY SLOW. However, to save time,
	use the second 'if' block, which writes to a CSV file instead.
	"""

	if (0):
		raw_data = gl.glob("O:/QUALITY/QC Data Project/Raw Data/*")
		print(raw_data)
		excel_file = ExcelWriter('CombinedData.xlsx')
		all_data = pd.DataFrame()
		for i in raw_data:
			df = pd.read_excel(i)
			all_data = all_data.append(df, ignore_index=True)
			print(all_data)
			all_data.to_excel(excel_file)
		excel_file.save()
	if (1):
		raw_data = gl.glob("O:/QUALITY/QC Data Project/Raw Data/*")
		print(raw_data)
		all_data = pd.DataFrame()
		for i in raw_data:
			df = pd.read_excel(i)
			all_data = all_data.append(df, ignore_index=True)
			print(all_data)
			all_data.to_csv('CombinedData.csv')

def RemoveCharacters():
	'''
	Function that cleans up mis-copied characteristic names in the database.
	Primarily interested in degree symbol (°) errors.
	'''

	database_path = "C:/Users/usftdt0/Documents/CleanDataBase.xlsx"
	database_xlsx = pd.ExcelFile(database_path)
	database_df = pd.read_excel(database_xlsx)
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
	new_df = pd.DataFrame({'Charac.': characteristics_list})
	new_df.to_excel('ModCharac.xlsx')

# Combine_Data()
RemoveCharacters()
